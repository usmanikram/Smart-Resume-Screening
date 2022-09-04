from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateJobForm,CreateJobFormForResume,EditUserForm
from base.models import Resume,Candidate,Job,Qualification,Experience,Skill,User
from pyresparser import ResumeParser
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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


def editjob(request): 
    context={"segment":"editjob"}
    return render(request, 'editjob.html',context)
