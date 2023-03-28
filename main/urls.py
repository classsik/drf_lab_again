from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('login', obtain_auth_token),
    path('logout', views.logout),

    path('tours', views.get_tours),
    path('tours/<int:pk>', views.get_tour),
    path('tours/create', views.add_tour),
    path('tours/<int:pk>/edit', views.edit_tour),
    path('tours/<int:pk>/delete', views.delete_tour),

    path('excursions', views.get_excursions),
    path('excursions/<int:pk>', views.get_excursion),
    path('excursions/create', views.add_excursion),
    path('excursions/<int:pk>/edit', views.edit_excursion),
    path('excursions/<int:pk>/delete', views.delete_excursion),

    path('countries', views.get_countries),
    path('countries/<int:pk>', views.get_country),
    path('countries/create', views.add_country),
    path('countries/<int:pk>/edit', views.edit_country),
    path('countries/<int:pk>/delete', views.delete_country),

    path('cart/<int:pk>', views.get_cart),
    path('cart/<int:pk>', views.edit_cart),
]
