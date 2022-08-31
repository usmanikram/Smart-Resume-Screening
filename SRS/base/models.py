from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class MyUserManager(BaseUserManager):
    use_in_migrations = True

# python manage.py createsuperuser
    def create_user(self,firstname, lastname,contact, designation, company_name, company_contact, company_address, email, password, creation_date, is_approved, is_staff):
        user = self.model(
                          firstname = firstname,                         
                          lastname = lastname,                         
                          contact = contact,                         
                          designation = designation,                         
                          company_name = company_name,                         
                          company_contact = company_contact,       
                          company_address = company_address,             
                          email = email,                    
                          password = password,                         
                          creation_date = creation_date,                         
                          is_approved = is_approved,              
                          is_staff = is_staff
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # python manage.py createsuperuser
    def create_superuser(self, firstname, lastname,email, password):
        user = self.create_user(
                          firstname = firstname,                         
                          lastname = lastname,                           
                          email = email,                    
                          password = password,
                          contact = None,
                          designation = None,
                          company_name = None,
                          company_contact = None,
                          company_address = None,
                          creation_date= None,
                          is_approved=True,
                          is_staff=True
                          )
        user.is_active=True
        user.is_staff=True
        user.is_approved=True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    contact = models.CharField(max_length=200, null = True )
    designation = models.CharField(max_length=200, null = True)
    company_name = models.CharField(max_length=200, null = True)
    company_contact = models.CharField(max_length=200, null = True)
    company_address = models.CharField(max_length=200, null = True)
    email = models.EmailField(max_length=200, unique = True)
    password = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = MyUserManager()

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS must contain all required fields on your User model, 
    # but should not contain the USERNAME_FIELD or password as these fields will always be prompted for.
    REQUIRED_FIELDS = ['firstname','lastname',]

    class Meta:
        app_label = "base"
        db_table = "UserModel"

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj=None):
        return self.is_staff

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return self.is_staff

    


        
# Create your models here.
# class Users(models.Model):
#     firstname = models.CharField(max_length=200)
#     lastname = models.CharField(max_length=200)
#     contact = models.CharField(max_length=200)
#     designation = models.CharField(max_length=200)
#     company_name = models.CharField(max_length=200)
#     company_contact = models.CharField(max_length=200)
#     company_address = models.CharField(max_length=200)
#     email = models.EmailField(max_length=200, unique = True)
#     password = models.CharField(max_length=200)
#     creation_date = models.DateTimeField(auto_now_add=True)
#     is_approved = models.BooleanField(default=False)

#     def __str__(self):
#         return self.firstname +' '+self.lastname

class Job(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_approved': True})
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class Resume(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, null = True)
    resume = models.FileField(upload_to='uploads/resume/')


class Report(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    report = models.FileField()


class Feedback(models.Model):
    job_id = models.OneToOneField(Job, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    rating = models.CharField(max_length=1)

    def __str__(self):
        return self.title

class Candidate(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    resume = models.FileField()


    def __str__(self):
        return self.name


class Qualification(models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    programme = models.CharField(max_length=200, null=True)
    institution = models.CharField(max_length=200,null=True)
    
class Experience(models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200,null=True)
    role = models.CharField(max_length=200,null=True)


class Skill(models.Model):
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

