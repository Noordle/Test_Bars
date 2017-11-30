from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from academy.models import Candidate

class CandidateCreate(CreateView):
    model = Candidate
    success_url = ('/home/candidate/success')
    fields = ['name', 'email', 'planet', 'age']


def home_page(request):
    template = loader.get_template("academy/home_page.html")
    context = {}
    return HttpResponse(template.render(context))

def add_can(request):
    template = loader.get_template('academy/success_add_can.html')
    context = {}
    return HttpResponse(template.render(context))
