from .import views
from django.urls import path,include


urlpatterns = [
    path('',views.login_view,name="login"),
    path('home',views.home,name="home"),
]
