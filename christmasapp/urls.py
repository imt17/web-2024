
from django.urls import path

from christmasapp import views
from secret_santa import views as secret_santa_views

urlpatterns = [
    path('', views.index, name='index'),
    path('secret_santa', secret_santa_views.secret_santa, name='secret_santa'),
]