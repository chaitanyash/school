from django.conf.urls import url,include
from . import views
from schoolapi.views import *

urlpatterns = [
    url(r'^department/$', departmentApi),
    url(r'^course/$', courseApi),
    url(r'^login_page/$', views.LoginPage),
    
]
