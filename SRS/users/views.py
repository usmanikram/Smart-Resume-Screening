from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateJobForm,CreateJobFormForResume,EditUserForm
from base.models import Resume,Candidate,Job,Qualification,Experience,Skill,User
from pyresparser import ResumeParser
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .ml import extractTextPdf, cleanResumeText
import os, pickle

def Logout(request):
    logout(request)
    messages.success(request, 'Logout Successful.')
    return redirect('loginuser')


# Create your views here.
@login_required(login_url='loginuser')
def dashboard(request):
    context = {"segment" : "dashboard"}
    return render(request, 'dashboard.html', context)


@login_required(login_url='loginuser')
def editprofile(request,pk):
    user = User.objects.get(id=pk)
    context = {"segment" : "editprofile", "user":user}
    return render(request, 'editprofile.html', context)

@login_required(login_url='loginuser')
def update(request,pk):
    cname = request.POST['cname']
    cc = request.POST['contact']
    ca = request.POST['ca']
    email = request.POST['email']
    fname =  request.POST['fname']
    lname = request.POST['lname']
    empdesi = request.POST['design']
    empcontact = request.POST['empcontact']
    user = User.objects.get(id=pk)
    user.company_name = cname
    user.company_contact = cc
    user.company_address = ca
    user.email = email
    user.firstname = fname
    user.lastname = lname 
    user.designation = empdesi
    user.contact = empcontact
    user.save()
    context = {"user":user, "segment" : "editprofile"}
    return render(request, 'editprofile.html',context)

@login_required(login_url='loginuser')
def jobs(request,pk):
    job = Job.objects.filter(user_id=pk)
    context = {"segment" : "jobs", "job": job}
    return render(request, 'jobs.html', context)

# def createjob(request):
#     context={"segment": "createjob"}
#     return render(request, 'createjob.html',context)
@login_required(login_url='loginuser')
def createjob(request,pk):
    if request.method == 'POST':
        jobform = CreateJobForm(request.POST , request.FILES)
        resumeform = CreateJobFormForResume(request.POST , request.FILES)
        files = request.FILES.getlist('resume')
        if jobform.is_valid():
            j = jobform.save(commit=False)
            j.user_id = request.user
            j.save()
            for f in files:   
                r = Resume(job_id=j, resume=f)
                r.save()
                #ETL Pipeline
                data = ResumeParser(r.resume.path).get_extracted_data()
                c = Candidate(job_id=r.job_id,name=data['name'],contact=data['mobile_number'],email=data['email'],resume=r.resume)
                c.save()
                q = Qualification(candidate_id=c, programme = data['degree'], institution = data['degree'] )
                q.save()
                e = Experience(candidate_id=c, company_name = data['experience'], role = data['experience'] )
                e.save()
                s = Skill(candidate_id=c, name = data['skills'])
                s.save()
            return redirect ('jobs', pk)
    else:
        jobform = CreateJobForm()
        resumeform = CreateJobFormForResume()
    context = {'jobform':jobform ,'resumeform':resumeform}
    return render(request,'createjob.html',context)



@login_required(login_url='loginuser')
def viewjobdetails(request,pk):
    job = Job.objects.get(id=pk)
    u = job.user_id
    user = User.objects.get(email=u)
    can_count = Candidate.objects.filter(job_id=pk).count()
    candidates = Candidate.objects.filter(job_id=pk)
    context={"segment":"viewjobdetails", 'job':job , 'user': user, 'can_count': can_count, 'candidates': candidates}
    return render(request, 'viewjobdetails.html',context)

@login_required(login_url='loginuser')
def editjob(request, pk):
    job = Job.objects.get(id=pk) 
    context={"segment":"editjob", "job":job}
    return render(request, 'editjob.html',context)


@login_required(login_url='loginuser')
def updatejob(request,pk):
    job_description = request.POST['description']
    job_qualification = request.POST['qualification']
    job_experience = request.POST['experience']
    job_skills = request.POST['skills']
    job = Job.objects.get(id=pk)
    job.description = job_description
    job.qualification = job_qualification
    job.experience = job_experience
    job.skills = job_skills
    job.save()
    context = { "segment" : "jobs"}
    return render(request, 'jobs.html',context)


@login_required(login_url='loginuser')
def deletejob(request, pk):
    job = Job.objects.get(id=pk)
    job.delete()
    return redirect ('jobs', pk)


def reports(request,pk):
    context = {"segment" : "reports"}
    return render(request, 'reports.html', context)

def feedback(request):
    context = {"segment" : "feedback"}
    return render(request, 'feedback.html', context)
    
def addfeedback(request):
    context = {"segment" : "addfeedback"}
    return render(request, 'addfeedback.html', context)

def insights(request):
    context = {"segment" : "insights"}
    return render(request, 'insights.html', context)

def settings(request):
    context = {"segment" : "settings"}
    return render(request, 'settings.html', context)

def finalreport(request):
    return render(request, 'finalreport.html')

def viewjobs(request):
    context={"segment":"viewjobs"}
    return render(request, 'viewjobs.html',context)



def shortlist(request,pk):
    c = Candidate.objects.filter(job_id=pk)
    j = Job.objects.get(id=pk)
    modulePath = os.path.dirname(__file__)
    path1 = os.path.join(modulePath, 'model/onevrest_knn_model.pkl')
    path2 = os.path.join(modulePath, 'model/onevrest_knn_labelencoder.pkl')
    path3 = os.path.join(modulePath, 'model/onevrest_knn_tfidfvectorizer.pkl')

    with open(path1, "rb") as modelFile:
        model = pickle.load(modelFile)

    with open(path2, "rb") as labelencoderFile:
        le = pickle.load(labelencoderFile)

    with open(path3, "rb") as tfidfvectorizerFile:
        vectorizer = pickle.load(tfidfvectorizerFile)

    for cand in c:
        r = cand.resume
        resumeText = extractTextPdf(r)
        cleanedText = cleanResumeText(resumeText)
        textFeatures = vectorizer.transform([cleanedText])
        pred = model.predict(textFeatures)
        prediction = le.inverse_transform(pred)[0]
        cand.category = prediction
        cand.save()

        title = j.title

        if prediction in title:
            cand.is_shortlisted = True
            cand.save()


    context={"segment":"viewjobs"}
    return render(request, 'viewjobs.html',context)

