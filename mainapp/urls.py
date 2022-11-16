from django.urls import path
from . import views

app_name='mainapp'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('carlisting', views.carlisting_view, name='carlisting'),
    path('car-detail/<int:id>', views.cardetail_view, name='car-detail'),
    path('search', views.search_view, name='search'),
    path('bookings', views.bookings_view, name='bookings'),
    path('testimonials', views.testimonial_view, name='testimonial'),
    path('login', views.login_request, name='login'),
    path('create-account', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
]