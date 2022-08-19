from django.urls import path

from . import views

urlpatterns = [
    path('', views.WatchdogsListView.as_view(),name='home'),
    path('post/new/', views.WatchdogsCreateView.as_view(),name='post_new'),
    path('post/<slug:slug>/', views.WatchdogsDetailView.as_view(),name='post_detail'),
    path('post/<int:pk>/edit/', views.WatchdogsUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/', views.WatchdogsDeleteView.as_view(),name='post_delete'),

]