from samapp.models import *
from django.http import HttpResponse
from django.http import *
from django.shortcuts import render,redirect
from django.http import Http404
from django.views.generic import ListView
from .forms import RegistrationForm
from .forms import CountClothes
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate                             
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from samapp.forms import SignUpForm

@login_required
def index(request):
    return render(request, 'samapp/index.html', {})

def home(request):
    return render(request, 'samapp/home.html', {})



def det(request):
    l = city_areamap.objects.all()
    return render(request, 'samapp/det.html', {'fin':l})


def laundry_search(request, id, id1):
    
    laun = laundries.objects.filter(city_areamapid = id,sector_id = id1)
    img_src = sectors.objects.filter(id =  id1)
    return render(request, 'samapp/laundry_search.html', {'laundry_search':laun, 'img_src':img_src})

def shop_view(request, id):
    #lid = laundries.objects.(laundry.id = id)
    every = dress_servicemap.objects.filter(laundry_id = id)
    #lan = dress_servicemap.objects.filter(every.laundry_id)
    return render(request, 'samapp/shop.html', {'shop': every})

def count_clothes(request):
    form = CountClothes(initial = {'NumberOfsareesIroning':'0'})
    return render(request, 'samapp/count_clothes.html', {'form':form})  

def fast_delivery(request):
    return render(request, 'samapp/fast_delivery.html', {})

def total_cost(request):
    return render(request, 'samapp/total_cost.html', {})

def register(request):
    print("entered register view")
    print(request)
    form_class = RegistrationForm
    form = form_class(request.POST);
    if request.method == 'POST':
        a = orders();
        #return HttpResponseRedirect('<h1>ugfruiwhfiuoreh4</h1>')   
        if form.is_valid():
            print(request.POST.get)
            add = request.POST.get['Address']
            mob = request.POST.get['Mob']
            f = orders(address = add, phno = mob)
            f.save()
          
    else:
        form = RegistrationForm()
    return render(request, 'samapp/registration.html', {'form':form})
def success_message(request):
    return render(request, 'samapp/congr.html', {})
def ratings(request):
   return render(request, 'samapp/ratings.html', {})
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            raw_password = request.POST.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'samapp/signup.html', {'form': form})
