from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from academy.models import Candidate, Test, Question
from django.urls import reverse


class CandidateCreate(CreateView):
    model = Candidate
    fields = ['name', 'email', 'planet', 'age']

    def get_success_url(self):
        return reverse('test', args=(self.object.id,))


def home_page(request):
    template = loader.get_template("academy/home_page.html")
    context = {}
    return HttpResponse(template.render(context))


def test(request, cand_id):
    candidate = Candidate.objects.get(id=cand_id)
    question_list = Test.objects.filter(planet=candidate.planet)
    questions = Question.objects.filter(test=question_list)
    template = loader.get_template("academy/test.html")
    context = {
        'candidate': candidate,
        'question_list': question_list,
        'questions' : questions,
    }
    return HttpResponse(template.render(context))

def results(request, cand_id):
    template = loader.get_template("academy/test_results.html")

    context = {

    }