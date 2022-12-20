from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = "core/index.html"


def teste(request, id):
    teste = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 3, 1, 2]
    return "teste.html"
