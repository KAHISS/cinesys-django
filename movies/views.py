from django.shortcuts import render

from utils.movies import gerar_filme_aleatorio
from movies.models import Critic


def index(request):
    return render(request, 'movies/pages/home.html', context={
        'movies': Critic.objects.all(),
    })
