from .models import Tour, Exscursion, Country, Cart
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from .serializers import TourSerializer, CartSerializer, ExscursionSerializer, CountrySerializer
from rest_framework.authtoken.models import Token


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def logout(request):
    Token.objects.get(user=request.user).delete()

    return Response(status=status.HTTP_200_OK, data={
        "data": {
            "message": "logout"
        }})

@api_view(['GET', "POST"])
@permission_classes((AllowAny,))
def add_get_tours(request):
    if request.method == 'GET':
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if request.user.is_superuser:
            serializer = TourSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['PATCH', "GET", "DELETE"])
@permission_classes((AllowAny,))
def get_edit_delete_tour(request, pk):
    if request.method == 'GET':
        try:
            tour = Tour.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TourSerializer(tour)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        if request.user.is_superuser:
            try:
                tour = Tour.objects.get(pk=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = TourSerializer(data=request.data, instance=tour, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        if request.user.is_superuser:
            try:
                tour = Tour.objects.get(pk=pk)
                tour.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', 'PATCH', "DELETE"])
@permission_classes((IsAuthenticated,))
def get_edit_delete_cart(request, pk):
    if request.method == 'GET':
        try:
            cart = Cart.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        try:
            cart = Cart.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(data=request.data, instance=cart, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            cart = Cart.objects.get(pk=pk)
            cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', "POST"])
@permission_classes((IsAdminUser,))
def add_get_excursions(request):
    if request.method == 'GET':
        excursions = Exscursion.objects.all()
        serializer = ExscursionSerializer(excursions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ExscursionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes((IsAdminUser,))
def get_edit_delete_excursion(request, pk):
    if request.method == 'GET':
        try:
            excursion = Exscursion.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ExscursionSerializer(excursion)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        try:
            excursion = Exscursion.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ExscursionSerializer(data=request.data, instance=excursion, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            excursion = Exscursion.objects.get(pk=pk)
            excursion.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
@permission_classes((IsAdminUser,))
def add_get_countries(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', "PATCH", "DELETE"])
@permission_classes((IsAdminUser,))
def get_edit_delete_country(request, pk):
    if request.method == 'GET':
        try:
            country = Country.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CountrySerializer(country)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        try:
            country = Country.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CountrySerializer(data=request.data, instance=country, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            country = Country.objects.get(pk=pk)
            country.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

