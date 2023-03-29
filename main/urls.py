from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('login', obtain_auth_token),
    path('logout', views.logout),

    path('tours', views.add_get_tours),
    path('tours/<int:pk>', views.get_edit_delete_tour),

    path('excursions', views.add_get_excursions),
    path('excursions/<int:pk>', views.get_edit_delete_excursion),

    path('countries', views.add_get_countries),
    path('countries/<int:pk>', views.get_edit_delete_country),

    path('cart/<int:pk>', views.get_edit_delete_cart),
]
