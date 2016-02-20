from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register', views.regsiter, name='register'),
    url(r'^logout', views.logout, name='logout')
]
