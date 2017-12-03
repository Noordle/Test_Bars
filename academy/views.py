from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from academy.models import Candidate, Test, Question, Jedi, CandidateAnswer
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings
from django.db.models import Count, F


class CandidateCreate(CreateView):
    model = Candidate
    fields = ['name', 'email', 'planet', 'age']

    def get_success_url(self):
        return reverse('academy:test', kwargs={'cand_id': self.object.id})


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
        'questions': questions,
    }
    return HttpResponse(template.render(context))


def results(request, cand_id):
    candidate = Candidate.objects.get(id=cand_id)
    test = Test.objects.get(planet=candidate.planet)
    candidate_answers = dict(request.POST)
    CandidateAnswer.objects.create(candidate=candidate, test=test, answer=candidate_answers)
    template = loader.get_template("academy/test_results.html")
    context = {
        'candidate_answers': candidate_answers,
        'candidate': candidate
    }
    return HttpResponse(template.render(context))


def jedi_list(request):
    jedis = Jedi.objects.annotate(number_padavans=Count('candidate'))
    template = loader.get_template("academy/jedi_list.html")
    context = {
        'active_jedis': jedis.filter(number_padavans__gt=0),
        'empty_jedis': jedis.filter(number_padavans=0),
    }
    return HttpResponse(template.render(context))


def jedi_view(request, jedi_id):
    jedi = Jedi.objects.get(id=jedi_id)
    jedi_cands = Candidate.objects.filter(planet=jedi.planet, jedi=None)
    answers = {c.id: c.candidateanswer_set.get(test__planet=jedi.planet).answer for c in jedi_cands}
    jedi_cands = jedi_cands.values()
    for jc in jedi_cands:
        jc['answer'] = answers[jc['id']]
    template = loader.get_template("academy/jedi_view.html")
    context = {
        'jedi': jedi,
        'jedi_cands': jedi_cands
    }
    return HttpResponse(template.render(context))


def add_jedi(request, cand_id):
    if request.method == 'POST':
        candidate = Candidate.objects.get(id=cand_id)
        jedi_id = request.POST['jedi_id']
        jedi = Jedi.objects.get(id=jedi_id)
        if jedi.candidate_set.count() < 3:
            candidate.jedi_id = jedi_id
            candidate.save()
            send_notification(candidate)
            return HttpResponseRedirect(reverse("academy:jedi_view", kwargs={'jedi_id': jedi_id}))
        else:
            return HttpResponse("You have to many padavans")


def send_notification(candidate):
    email = EmailMessage('Congratulations', 'Now, you are my padavan. Ha-ha-ha', settings.EMAIL_HOST_USER, to=[candidate.email])
    email.send()
