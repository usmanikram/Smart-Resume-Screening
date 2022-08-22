from pyresparser import ResumeParser
#import spacy
#nlp = spacy.load('en_core_web_sm')
#print(nlp._path)

def get_resume_data(fi):

    data = ResumeParser(fi).get_extracted_data()
    return data
