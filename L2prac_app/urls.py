from django.conf.urls import url
from L2prac_app import views

urlpatterns = [
    url(r'^$',views.users,name='users'),
]
