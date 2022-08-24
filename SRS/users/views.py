from django.shortcuts import render, redirect
from .forms import CreateJobForm,CreateJobFormForResume
from base.models import Resume,Candidate,Job,Qualification,Experience,Skills,User
from pyresparser import ResumeParser
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def Logout(request):
    logout(request)
    return redirect('login')


# Create your views here.
@login_required(login_url='loginuser')
def dashboard(request):
    context = {"segment" : "dashboard"}
    return render(request, 'dashboard.html', context)

def editprofile(request):
    context = {"segment" : "editprofile"}
    return render(request, 'editprofile.html', context)

def jobs(request,pk):
    job = Job.objects.filter(user_id=pk)
    context = {"segment" : "jobs", "job": job}
    return render(request, 'jobs.html', context)

# def createjob(request):
#     context={"segment": "createjob"}
#     return render(request, 'createjob.html',context)
def createjob(request,pk):
    if request.method == 'POST':
        jobform = CreateJobForm(request.POST , request.FILES)
        resumeform = CreateJobFormForResume(request.POST , request.FILES)
        files = request.FILES.getlist('file_path')
        if jobform.is_valid():
            j = jobform.save()
            for f in files:   
                r = Resume(job_id=j, file_path=f)
                r.save()
                # ETL Pipeline
                data = ResumeParser(r.file_path.path).get_extracted_data()
                c = Candidate(job_id=r.job_id,name=data['name'],contact=data['mobile_number'],email=data['email'],resume=r.file_path)
                c.save()
                q = Qualification(candidate_id=c, programme = data['degree'], institution = data['degree'] )
                q.save()
                e = Experience(candidate_id=c, company_name = data['experience'], role = data['experience'] )
                e.save()
                s = Skills(candidate_id=c, name = data['skills'])
                s.save()
    else:
        jobform = CreateJobForm()
        resumeform = CreateJobFormForResume()
    context = {'jobform':jobform ,'resumeform':resumeform}
    return render(request,'createjob.html',context)

def viewjobs(request):
    context={"segment":"viewjobs"}
    return render(request, 'viewjobs.html')

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

def viewjobdetails(request,pk):
    job = Job.objects.get(id=pk)
    u = job.user_id
    user = User.objects.get(email=u)
    context={"segment":"viewjobdetails", 'job':job , 'user': user}
    return render(request, 'viewjobdetails.html',context)

def editjob(request):
    context={"segment":"editjob"}
    return render(request, 'editjob.html',context)