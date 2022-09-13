import pickle
import re
import pdfplumber
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse


def extractTextPdf(path):
    """Reads a PDF file and extracts the text data from each of the pages
    Args:
        path (str): Path or FilePointer pointing to the pdf file
    Returns:
        str: Extracted text from the specified pdf file
    """
    text = ""
    with pdfplumber.open(path) as pdfFile:
        for page in pdfFile.pages:
            text += page.extract_text()
    return text



def cleanResumeText(resumeText):
    """Cleans the text in resume by removing URLs, hashtags, special letters,
    and punctuations
    Args:
        resumeText (str): The text to clean
    Returns:
        str: Cleaned resume text
    """

    resumeText = re.sub("http\S+\s*", " ", resumeText)  # Remove URLs
    resumeText = re.sub("RT|cc", " ", resumeText)  # Remove RT and cc
    resumeText = re.sub("#\S+", "", resumeText)  # Remove hashtags
    resumeText = re.sub("@\S+", "  ", resumeText)  # Remove mentions
    resumeText = re.sub("[%s]" % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""),
                         " ", resumeText)  # Remove punctuations
    resumeText = re.sub(r"[^\x00-\x7f]", " ", resumeText) 
    resumeText = re.sub('\s+', ' ', resumeText)  # Remove extra whitespace
    return resumeText


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode()), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
