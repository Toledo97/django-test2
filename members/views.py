from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    myMembers  = Member.objects.all().values()
    template = loader.get_template('all-members.html')
    context = {
        'myMembers': myMembers,
    }
    return HttpResponse(template.render(context, request))

def details(request,id):
    myMember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myMember': myMember
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    myMembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': myMembers,
    }
    return HttpResponse(template.render(context,request))