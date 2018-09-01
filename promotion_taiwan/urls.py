from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = 'promotion_taiwan'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
]
