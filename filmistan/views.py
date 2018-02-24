from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from film import settings
from .models import Film, Genre
from django.utils import timezone
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from film.settings import MEDIA_ROOT
from django.template.defaultfilters import stringfilter
from django import template
from django.db.models import Q
from django.views.generic import ListView
import string
import re
from django.db import connection
from django.core.paginator import Paginator
from django.db import models
register = template.Library()

@register.filter
@stringfilter
def trim(value):
    return value.strip()

def Index(request):
    films = Film.objects.all()
    fff = Film.objects.all().filter(createDate__lte=timezone.now()).order_by('createDate')

    genres = Genre.objects.all()
    return rdrindx(request)
    #return render(request, "Untitled-1.html", {'films': films, 'genres': genres,'fff':fff})



def kayit(request):
    if request.method == "POST":
        form = forms.kayıtformu(request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            return HttpResponseRedirect('/login/')
    else:
        form = forms.kayıtformu()
    return render_to_response('index/register2323.html',
                              locals(),
                              context_instance=RequestContext(request))

class Filmcek(ListView):
    template_name = 'Filmler.html'
    model = Film

    def get_context_data(self, **kwargs):
        e = get_object_or_404(Film, pk=self.args[0])
        context = super(Filmcek, self).get_context_data(**kwargs)
        #context['genres'] = Genre.objects.all()
        # context['films'] = Film.objects.all().filter(genre=self.genre)
        context['film'] = e
        #Film.objects.get_object_or_404(Film  title=self.args[0])
        # context['festival_list'] = Festival.objects.all()
        # And so on for more models
        return context

class paginat(ListView):
    template_name = 'Untitled-1.html'
    model = Film

    def get_context_data(self, **kwargs):
        e = self.args[0]
        context = super(paginat, self).get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        a = Film.objects.all()
        context['genres'] = Genre.objects.all()
        f2 = Film.objects.all().filter(createDate__lte=timezone.now()).order_by('-createDate')
        f1 = Film.objects.all().filter(rating__lte=10).order_by('-rating')
        paginator = Paginator(a, 20)
        context['fff'] = f1
        context['f2'] = f2
        context['films'] = paginator.page(e).object_list
        #Film.objects.get_object_or_404(Film  title=self.args[0])
        # context['festival_list'] = Festival.objects.all()
        # And so on for more models
        return context

class FilmList(ListView):
    template_name = 'Untitled-1.html'
    model = Genre

    def get_context_data(self, **kwargs):
        self.genre = get_object_or_404(Genre, title=self.args[0].replace('_', ' '))

        f2 = Film.objects.all().filter(genre=self.genre).filter(createDate__lte=timezone.now()).order_by('-createDate')
        f1 = Film.objects.all().filter(genre=self.genre).filter(rating__lte=10).order_by('-rating')

        context = super(FilmList, self).get_context_data()
        context['fff'] = f1
        context['f2'] = f2

        context['genres'] = Genre.objects.all()
        context['films'] = Film.objects.all().filter(genre=self.genre)
        # context['festival_list'] = Festival.objects.all()
        # And so on for more models
        return context

"""""
    def get_queryset(self):
        self.genre = get_object_or_404(Genre, title=self.args[0])
        return Film.objects.filter(genre=self.genre)
"""""


def rdrindx(request):
    return redirect('/page/1')


def Login(request):
    next = request.GET.get('next', '/index/')
    if request.method == "POST":
        username = request.POST['inputEmail3']
        password = request.POST['inputPassword3']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "index/login.html", {'redirect_to': next})


def password_reset(request):
    return render(request, "resetpw/password_reset_form.html", {})


def password_reset_done(request):
    return render(request, "resetpw/password_reset_done.html", {})


def password_reset_confirm(request):
    return HttpResponseRedirect("password_reset_done")


def info(request):
    return render(request, "hakkımızda.html", {})

@login_required
def Profile(request):
    return render(request, 'profil.html', {})


@login_required
def filmler(request):
    film = Film.objects.all()
    return render(request, "film_lists.html", {'film': film})


def Logout(request):
    logout(request)
    return HttpResponseRedirect("/index/")




def fragmanlar(request):
    return render(request, "Fragmanlar.html", {'fragmanlar': fragmanlar})
