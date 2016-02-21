from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^createTask', views.createTask, name='createTask'),
    url(r'^deleteTask/(?P<task_id>[0-9]+)', views.deleteTask, name='deleteTask'),
    url(r'^toggleTask/(?P<task_id>[0-9]+)', views.toggleTask, name='toggleTask')
]

