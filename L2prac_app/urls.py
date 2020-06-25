from django.conf.urls import url
from L2prac_app import views

#Template tagging

app_name = 'L2prac_app'

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^users/$',views.users,name='users'),
    url(r'^form/$',views.formUser,name='formUser'),
]
