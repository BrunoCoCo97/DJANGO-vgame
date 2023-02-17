from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.getVgames),
    path('post/', views.postVgames),
    path('put/<int:pk>/', views.putVgames),
    path('delete/<int:pk>/', views.deleteVgames),
]