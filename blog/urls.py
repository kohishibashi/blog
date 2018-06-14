from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('upload/',views.UploadView.as_view(), name='upload'),
    path('detail/<int:pk>/',views.DetailView.as_view(), name='detail'),
]
