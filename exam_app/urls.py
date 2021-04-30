from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout',views.logout),
    path('wishes', views.wishes),
    path('wishes/new',views.new_wish),
    path('wishes/create',views.create_wish),
    path('wishes/<int:w_id>/edit', views.edit_wish),
    path('wishes/<int:w_id>/update', views.update_wish),
    path('wishes/<int:w_id>/delete', views.delete_wish),
    path('wishes/<int:w_id>/granted', views.grant_wish),
    path('wishes/<int:w_id>/like', views.like_wish),
    path('wishes/<int:w_id>/unlike', views.unlike_wish),
    path('stats', views.stats),
]