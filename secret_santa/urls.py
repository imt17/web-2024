from django.urls import path
from secret_santa import views
from christmasapp import views as christmas_views

urlpatterns = [
    path('secret_santa', views.secret_santa, name='secret_santa'),
    path('', christmas_views.index, name='index'),
]