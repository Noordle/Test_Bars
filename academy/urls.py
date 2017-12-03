from academy import views
from django.conf.urls import url


urlpatterns = [
    url(r'^candidate/(?P<cand_id>[0-9]+)/test/results/$', views.results, name='results'),
    url(r'^candidate/(?P<cand_id>[0-9]+)/test/$', views.test, name='test'),
    url(r'^candidate/(?P<cand_id>[0-9]+)/jedi/$', views.add_jedi, name='add_jedi'),
    url(r'^candidate/', views.CandidateCreate.as_view(), name="new_candidate"),
    url(r'^jedi/(?P<jedi_id>[0-9]+)/$', views.jedi_view, name="jedi_view"),
    url(r'^jedi/', views.jedi_list, name="jedi_list"),
    url(r'^$', views.home_page, name="home_page"),

]

