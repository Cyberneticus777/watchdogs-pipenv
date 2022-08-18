from django.shortcuts import render
from django.views.generic import ListView, DetailView,UpdateView
from django.views.generic.edit import CreateView
from . models import Post
# Create your views here.

class WatchdogsListView(ListView):
    model = Post
    template_name = 'watchdogs/home.html'


class WatchdogsDetailView(DetailView):
    model = Post
    template_name = 'watchdogs/post_detail.html'
    #context_object_name = 'custom'

class WatchdogsCreateView(CreateView):
    model = Post
    template_name = 'watchdogs/post_new.html'
    fields = ('autor','titulo','conteudo')

class WatchdogsUpdateView(UpdateView):
    model = Post
    template_name = 'watchdogs/post_edit.html'
    fields = ('titulo','conteudo')