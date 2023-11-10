from django.shortcuts import render
from .models import Product

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profile, Product

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# function based views
def home(request):
    return render(request, 'CRUD/home.html')

@csrf_exempt
def create(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        email_add = request.POST['email']
        
        # get the data submitted to form and save to db
        new_profile = Profile(username=user_name, email=email_add)
        new_profile.save()
        # to call it in home.html to show message
        success = 'Profile created successfully.'
        return HttpResponse(success)
    
# class based view
class ProductListView(ListView):
    model = Product
    # <app>/<model>_<viewtype>.html
    template_name = 'CRUD/home.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    fields = ['productName', 'qty']
    success_url = '/'

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['productName', 'qty']
    success_url = '/'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/'
