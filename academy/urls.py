from academy.views import *
from django.conf.urls import url


urlpatterns = [
    url(r'^$', home_page, name="home_page"),
    url(r'^candidates/', add_candidate, name="add_can"),
    # url(r'^jedi/', jedi, name="add_jedi"),

]
