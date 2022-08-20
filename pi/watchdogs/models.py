from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                            .filter(status='publicado')

class Post(models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado', 'Publicado'),
    )
    titulo = models.CharField(max_length=255)
    slug   = models.SlugField(max_length=255)
    autor  = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    conteudo  = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado    = models.DateTimeField(auto_now_add=True)
    alterado  = models.DateTimeField(auto_now=True)
    status    = models.CharField(max_length=10,
                                choices=STATUS,
                                default='rascunho')

    objects   = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.slug])

    def get_absolute_url_update(self):
        return reverse('post_edit',args=[self.pk])

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo

@receiver(post_save,sender=Post)
def insert_slug(sender,instance,**kwargs):
    if kwargs.get('created',False):
        print('Criando slug')
    if not instance.slug:
        instance.slug = slugify(instance.titulo)
        return instance.save()

# Create your models here.

"""
Post.objects.bulk_create([
    Post(titulo='Testando o shell do Django 2 com bulk 1',slug='testando-o-shell-do-django-21',conteudo='Testando o shell do Django',autor=user),
    Post(titulo='Testando o shell do Django 3 com bulk 2',slug='testando-o-shell-do-django-22',conteudo='Testando o shell do Django',autor=user),
    Post(titulo='Testando o shell do Django 4 com bulk 3',slug='testando-o-shell-do-django-23',conteudo='Testando o shell do Django',autor=user),
])
"""