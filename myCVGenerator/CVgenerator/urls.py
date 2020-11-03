from django.urls import path
from . import views


urlpatterns = [
    path('', views.accept, name='index'),
    path('<int:id>/', views.cv, name='cv')
]
