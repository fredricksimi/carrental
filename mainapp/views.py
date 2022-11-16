from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle, Brands, Fueltype, BookVehicle, Testimonial
from .forms import MyCustomSignupForm, User, BookVehicleForm, TestimonialForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == "POST":
        form = MyCustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mainapp:login')
    else:
        form = MyCustomSignupForm()
    return render(request, 'mainapp/create-account.html', {'form':form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('mainapp:home')
    form = AuthenticationForm()
    return render(request=request, template_name="mainapp/login.html", context={'login_form':form})

def logout_view(request):
    logout(request)
    return redirect('mainapp:home')

def home_view(request):
    return render(request, 'mainapp/index.html')

def about_view(request):
    return render(request, 'mainapp/about.html')

def carlisting_view(request):
    cars = Vehicle.objects.all()
    brands = Brands.objects.all()
    fuels = Fueltype.objects.all()
    context = {
        'cars': cars,
        'brands': brands,
        'fueltype':fuels
        }
    return render(request, 'mainapp/car-listing.html', context)

def search_view(request):
    brand = request.GET['brandname']
    fueltype = request.GET['fuelname']
    vehicles = Vehicle.objects.filter(vehicle_brand__name=brand, fuel_type__name=fueltype)
    thebrands = Brands.objects.all()
    thefuels = Fueltype.objects.all()
    context = {
        'vehicles':vehicles,
        'thebrands':thebrands,
        'thefuels':thefuels
        }
    return render(request, 'mainapp/vehicle-search.html', context)

def cardetail_view(request, id):
    the_car = get_object_or_404(Vehicle, id=id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BookVehicleForm(request.POST or None)
            if form.is_valid():
                newform = form.save(commit=False)
                newform.customer = request.user
                newform.vehicle = the_car
                newform.save()
                redirect('mainapp:car-detail', id)
                form = BookVehicleForm()
        else:
            form = BookVehicleForm()
    context = {'car':the_car, 'form':form}
    return render(request, 'mainapp/car-detail.html', context)

def bookings_view(request):
    if request.user.is_authenticated:
        user_bookings = BookVehicle.objects.filter(customer__username=request.user.username)
    context = {
        'user_bookings':user_bookings
    }
    return render(request, 'mainapp/bookings.html', context)

def testimonial_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TestimonialForm(request.POST or None)
            if form.is_valid():
                newform = form.save(commit=False)
                newform.customer = request.user
                newform.save()
                redirect('mainapp:testimonial')
                form = TestimonialForm()
        else:
            form = TestimonialForm()
    context = {
        'form':form
    }
    return render(request, 'mainapp/testimonial.html', context)