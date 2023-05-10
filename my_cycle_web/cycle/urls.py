from django.urls import path
from cycle.views import index, login, logout, register,sendMail,contact

app_name = 'cycle'
urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout/', logout, name='logout'),
    path('sendMail/', sendMail, name='sendMail'),
    path('contact/', contact, name='contact'),
]