from django.shortcuts import render
from django.http import HttpResponse
from L2prac_app.models import Uinfo
from L2prac_app.forms import NewUserForm
# Create your views here.

def home(request):
    home_dict={'home':"You're seeing text from the views/home"}
    return render(request,'L2prac_app/home.html',context=home_dict)

def users(request):
    user_list = Uinfo.objects.order_by('fname')
    user_dict = {'usersinfo':user_list}
    return render(request,'L2prac_app/users.html',context=user_dict)

def formUser(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print("Error! Invalid Form")
    return render(request,'L2prac_app/forms.html',{'form':form})
