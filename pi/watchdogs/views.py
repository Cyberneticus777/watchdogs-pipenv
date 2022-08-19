#from pyexpat.errors import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView,UpdateView, DeleteView
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

class WatchdogsCreateView(SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'watchdogs/post_new.html'
    fields = ('autor','titulo','slug','conteudo')
    success_message = "%(field)s - criado com sucesso"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )

class WatchdogsUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'watchdogs/post_edit.html'
    fields = ('titulo','conteudo')
    success_message = "%(field)s - alterado com sucesso"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )


class WatchdogsDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'watchdogs/post_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(WatchdogsDeleteView,self).delete(request, *args, **kwargs)