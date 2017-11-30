from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect


def home_page(request):
    template = loader.get_template("academy/home_page.html")
    context = {}
    return HttpResponse(template.render(context))


def add_candidate(request):
    pass
