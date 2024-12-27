from django.urls import path
from. import views


urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('homePage',views.homePage,name="homePage"),
    path('attendance', views.attendance,name='attendance' ),
    path('resoures', views.resoures,name="resoures"),
    path('myprof', views.myprof,  name='myprof'),
    path('eventsfinal', views.eventsfinal, name="eventsfinal"),
    path('networking', views.networking, name="networking")

    
]