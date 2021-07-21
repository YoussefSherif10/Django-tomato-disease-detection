from django.urls import path
from . import views

app_name='project'
urlpatterns=[
    path('^$', views.firstpage.as_view(), name="firstpage"),
    path('state', views.state , name = "state"),
]

