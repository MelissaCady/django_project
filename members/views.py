from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members, Projects
# Create your views here.


def index(request):
  mymembers = Members.objects.all().values()
  myprojects = Projects.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
    'myprojects': myprojects
  }
  return HttpResponse(template.render(context, request))
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  z = request.POST['project']
  member = Members(firstname=x, lastname=y)
  project = Projects(name_project=z)
  member.save()
  project.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  project = Projects.objects.get(id=id)
  member.delete()
  project.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  myproject = Projects.objects.all().values()
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
    'myproject': myproject,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  name_project = request.POST['projectn']
  member = Members.objects.get(id=id)
  project = Projects.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  project.name_project = name_project
  member.save()
  return HttpResponseRedirect(reverse('index'))

def home(request):
  template = loader.get_template('home.html')
  context = {
    'firstname': 'Linus',
  }
  return HttpResponse(template.render(context, request))

def userPage(request, id):
  member = Members.objects.get(id=id)
  template = loader.get_template('userpage.html')
  context = {
    'member': member,
  }
  return HttpResponse(template.render(context, request))

def base_site(request):
  template = loader.get_template('base_site.html')
  context = {
    
  }
  return HttpResponse(template.render(context, request))

