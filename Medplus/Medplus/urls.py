"""
URL configuration for Medplus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from login import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home1, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_page/', views.admin_page, name='admin_page'),

    path('oprt/',views.operator,name='oprt'),
    path('add/', views.add, name='add'),
    path('remove/', views.remove, name='remove'),
    path('search/', views.search, name='search'),
    path('billing/', views.billing, name='billing'),
    path('amount/', views.amount, name='amount'),
    path('medlist/', views.medicines_list, name='medlist'),


    path('logout/', views.logout, name='logout'),

    path('welcome/', views.welcome, name='welcome'),

    path('operator/', views.operator, name='operator'),
    path('totalsales/', views.totalsales, name='totalsales'),
    path('datewise/', views.datewise, name='datewise'),
    path('operatorwise/', views.operatorwise, name='operatorwise'),
    path('betweendates/', views.betweendates, name='betweendates'),

    path('addoperator/', views.addoperator, name='addoperator'),
    path('deleteoperator/', views.deleteoperator, name='deleteoperator'),

    path('log/',views.log,name='log'),
    path('welcome1/',views.welcome1,name='welcome1'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)