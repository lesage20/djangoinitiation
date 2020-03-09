from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('about-us', views.aboutus, name='about-us'),
    path('flight-homepage.html', views.flighthomepage, name='flighthomepage'),
    path('hotel-homepage.html', views.hotelhomepage, name='hotelhomepage'),
    path('tour-homepage.html', views.tourhomepage, name='tourhomepage'),
    path('cruise-homepage.html', views.cruisehomepage, name='cruisehomepage'),
    path('car-homepage.html', views.carhomepage, name='carhomepage'),
    path('landing-page.html', views.landingpage, name='landingpage'),

    path('flight-listing-right-sidebar.html',
         views.flight_listing_right_sidebar, name='flight-listing-left-sidebar'),

    path('flight-listing-left-sidebar.html',
         views.flight_listing_left_sidebar, name='flight-listing-left-sidebar'),

    path('flight-grid-right-sidebar.html',
         views.flight_grid_right_sidebar, name='flight-grid-right-sidebar'),

    path('flight-grid-left-sidebar.html',
         views.flight_grid_left_sidebar, name='flight-grid-left-sidebar'),

    path('flight-detail-right-sidebar.html',
         views.flight_detail_right_sidebar, name='flight-detail-right-sidebar'),

    path('flight-detail-left-sidebar.html',
         views.flight_detail_left_sidebar, name='flight-detail-left-sidebar'),

]
