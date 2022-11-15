from django.urls import path, re_path
from women.views import *


urlpatterns = [
    path("", index),  # http://127.0.0.1:8000/
    path("cats/<slug:cat>/", categories),  # http://127.0.0.1:8000/cats/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]

# handler404 = pageNotFound
# handler404 позволяет написать для страницы 404 свой обработчик
