from django.db import models



# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=1000)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    linkedin=models.CharField(max_length=100)
    school=models.CharField(max_length=100)
    board=models.CharField(max_length=100)
    score=models.CharField(max_length=100)
    intermediate=models.CharField(max_length=100)
    board1=models.CharField(max_length=100)
    percentage=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    cgpa=models.CharField(max_length=100)
    technical_skills=models.CharField(max_length=1000)

   
    projects=models.CharField(max_length=1000)
    certifications_workshops=models.CharField(max_length=1000)
    internships=models.CharField(max_length=1000)
    achievements=models.CharField(max_length=1000)
    strengths=models.CharField(max_length=1000)
    hobbies=models.CharField(max_length=1000)
    date_of_birth=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    language_known=models.CharField(max_length=100)
    
    about_you=models.CharField(max_length=1000)
