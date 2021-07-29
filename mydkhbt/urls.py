from django.urls import path
from . import views
from mydkhbt import views as mydkhbt_views

urlpatterns = [
    path('', views.list, name='mydkhbt'),
    path('<int:id>/', views.post, name='postdkhbt'),
    path('updkhbt/', mydkhbt_views.up, name='updkhbt')
]
