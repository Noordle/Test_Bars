from academy import views
from django.conf.urls import url


urlpatterns = [
    url(r'^candidate/(?P<cand_id>[0-9]+)/test/results/$', views.results, name='results'),
    url(r'^candidate/(?P<cand_id>[0-9]+)/test/$', views.test, name='test'),
    url(r'^candidate/', views.CandidateCreate.as_view(), name="new_can"),
    url(r'^$', views.home_page, name="home_page"),
    # url(r'^jedi/', jedi, name="add_jedi"),

]
