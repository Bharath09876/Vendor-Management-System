from .import views
from django.urls import path,include

urlpatterns = [
    path('', views.landing_page),
    path('index', views.home),
    path('register',views.register_main),#register landing page
    path('login',views.login),#register landing page


]
