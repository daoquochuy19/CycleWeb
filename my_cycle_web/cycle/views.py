from imaplib import _Authenticator
from multiprocessing import context
# from pyexpat.errors import messages
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import News, Products, SayCustomer
from .forms import EmailForm,UserRegistrationForm
from cycle.forms import LoginForm
from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.core.mail import send_mail,BadHeaderError
from email.message import EmailMessage
from django.conf import settings


def index(request):
    myProducts= Products.objects.all().values()
    mySayCustomer= SayCustomer.objects.all().values()
    myNews= News.objects.all().values()
    template = loader.get_template('index.html')
    context= {
        'myProducts':myProducts,
        'mySayCustomer':mySayCustomer,
        'myNews':myNews,
    }
    # return render(request, 'index.html')
    return HttpResponse(template.render(context, request))


def sendMail(request):
    if request.method == 'POST':
        receiver_email = request.POST.get('email', '')
        name_receiver = request.POST.get('name', '')
        subject = 'Sending an email with Django'
        message = 'Thank you for your interest in our products. We will send you the latest notification'
        from_email = settings.EMAIL_HOST_USER
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, [receiver_email])
                print("gui thanh cong")
                return HttpResponseRedirect('/contact')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return HttpResponse('Fail to send message.')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    # return render(request, 'login.html')
    if request.method=="POST":
        user_name = request.POST['username']
        matkhau = request.POST['password']
        my_user = authenticate(username=user_name, password=matkhau)
        if my_user is not None:
            auth_login(request, my_user)
            print('login thanh cong!!!!!')
            return HttpResponseRedirect('/') 
        else:
            messages.success(request, ("Incorrect account or password"))
            return HttpResponseRedirect('login')
    return render(request, 'login.html', context={'form':LoginForm()})    


def register(request):
    # return render(request, 'register.html')
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)    
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
        else:           
            for error in list(form.errors.values()):
                # messages.error(request, error)
                print(request,error)

    form = UserRegistrationForm()
    return render(
        request=request,
        template_name="register.html",
        context={"form": form}
    )


def logout(request):    
    auth.logout(request)
    return HttpResponseRedirect('/')




