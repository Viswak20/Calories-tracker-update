"""
URL configuration for projectname project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appname import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',views.signup,name='signup'),
    path('',views.base,name='base'),
    path('login',views.login,name='login'),
    path('totalcaloriescalculating',views.totalcaloriescalculating,name='totalcaloriescalculating'),
    path('homepage/<int:id>',views.homepage,name='homepage'),
    path('forgetpassword',views.forgetpassword,name='forgetpassword'),
    path('caloriestracker',views.caloriestracker,name='caloriestracker'),
    path('addmeals',views.addmeals,name='addmeals'),
    path('addmeals2',views.addmeals2,name='addmeals2'),
    path('addmeals3',views.addmeals3,name='addmeals3'),
    path('dater',views.dater,name="dater"),
    path('dater2',views.dater2,name="dater2"),
    path('dater3',views.dater3,name="dater3"),

]
