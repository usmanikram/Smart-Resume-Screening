from django.db import models

# Create your models here.
class Users(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    company_contact = models.CharField(max_length=200)
    company_address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique = True)
    password = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname +' '+self.lastname

class Job(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, limit_choices_to={'is_approved': True})
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
#    resume = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(null = True)


    def __str__(self):
        return self.title

class Resume(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, null = True)
    file_path = models.FileField(upload_to='uploads/resume/')


class Report(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    file_path = models.FileField()


class Feedback(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Candidate(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    resume = models.FileField()


    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Qualification(models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    programme = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    
class Experience(models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)


class Skills(models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class Certification(models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    issued_by = models.CharField(max_length=200)


class Project(models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

