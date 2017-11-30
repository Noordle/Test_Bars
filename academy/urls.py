from academy import views
from django.conf.urls import url


urlpatterns = [
    url(r'^candidate/success', views.add_can, name='add_can'),
    url(r'^candidate/', views.CandidateCreate.as_view(), name="new_can"),
    url(r'^$', views.home_page, name="home_page"),
    # url(r'^jedi/', jedi, name="add_jedi"),

]
