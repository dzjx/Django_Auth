from django.conf.urls import url
from login import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout_view, name='logout'),

]
