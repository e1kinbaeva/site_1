from django.shortcuts import render

# Create your views here.
from apps.base.models import *
from apps.contacts.models import *

def index(request):
    about = About.objects.latest('id')
    settings = Settings.objects.latest('id')
    rewards = Rewards.objects.all()
    positions = Positions.objects.all()
    works = Works.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()
    research = Research.objects.latest('id')
    interests = Interests.objects.all()
    blogs = Blogs.objects.all()
    journal = Journal.objects.all()
    expert = Expert.objects.all()
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contacts = Contacts.objects.create(name = name,email=email,phone=phone,message=message)    
    return render(request, 'demo-academic.html', locals())