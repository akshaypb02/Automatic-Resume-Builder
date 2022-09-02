from django.shortcuts import render
from .models import Profile 
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io

def index(request):
    if request.method=="POST":
        email=request.POST.get("email","")
        password=request.POST.get("password","")
        profile=Profile(email=email,password=password)
        profile.save()
    return render(request,"index.html")
# Create your views here.
def accept(request):
    if request.method=="POST":
        
        name=request.POST.get("name","")
        address=request.POST.get("address","")
        phone=request.POST.get("phone","")
        email=request.POST.get("email","")
        school=request.POST.get("school","")
        board=request.POST.get("board","")
        score=request.POST.get("score","")
        intermediate=request.POST.get("intermediate","")
        board1=request.POST.get("board1","")
        percentage=request.POST.get("percentage","")
        degree=request.POST.get("degree","")
        college=request.POST.get("college","")
        branch=request.POST.get("branch","")
        cgpa=request.POST.get("cgpa","")
        technical_skills=request.POST.get("technical_skills","")
        projects=request.POST.get("projects","")
        certifications_workshops=request.POST.get("certifications_workshops","")
        internships=request.POST.get("internships","")
        achievements=request.POST.get("achievements","")
        strengths=request.POST.get("strengths","")
        hobbies=request.POST.get("hobbies","")
        date_of_birth=request.POST.get("date_of_birth","")
        father_name=request.POST.get("father_name","")
        mother_name=request.POST.get("mother_name","")
        language_known=request.POST.get("language_known","")
        about_you=request.POST.get("about_you","")
    
        profile=Profile(name=name,address=address,phone=phone,email=email,school=school,board=board,score=score,intermediate=intermediate,board1=board1,percentage=percentage,degree=degree,college=college,branch=branch,cgpa=cgpa,technical_skills=technical_skills,projects=projects,certifications_workshops=certifications_workshops,internships=internships,achievements=achievements,strengths=strengths,hobbies=hobbies,date_of_birth=date_of_birth,father_name=father_name,mother_name=mother_name,language_known=language_known,about_you=about_you)
        profile.save()
    return render(request,"accept.html")

def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    template=loader.get_template("resume.html")
    html=template.render({'user_profile':user_profile})
    option={
        'page-size':'Letter',
        'encoding':'UTF-8'
        }
        
    pdf=pdfkit.from_string(html,False,option)
    response=HttpResponse(pdf,content_type='application/pdf')

    response['Content-Disposition']='attachments'
    return response









def list(request):
    profile=Profile.objects.all()
    return render(request,"list.html",{'profile':profile})