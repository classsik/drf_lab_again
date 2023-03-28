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


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_tours(_):
    tours = Tour.objects.all()
    serializer = TourSerializer(tours, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_tour(_, pk):
    try:
        tour = Tour.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TourSerializer(tour)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAdminUser,))
def add_tour(request):
    serializer = TourSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes((IsAdminUser,))
def edit_tour(request, pk):
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


@api_view(['DELETE'])
@permission_classes((IsAdminUser,))
def delete_tour(request, pk):
    try:
        tour = Tour.objects.get(pk=pk)
        tour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_cart(_, pk):
    try:
        cart = Cart.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes((IsAuthenticated,))
def edit_cart(request, pk):
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


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_cart(_, pk):
    try:
        cart = Cart.objects.get(pk=pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes((IsAdminUser,))
def get_excursions(_):
    excursions = Exscursion.objects.all()
    serializer = ExscursionSerializer(excursions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAdminUser,))
def get_excursion(_, pk):
    try:
        excursion = Exscursion.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ExscursionSerializer(excursion)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAdminUser,))
def add_excursion(request):
    serializer = ExscursionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes((IsAdminUser,))
def edit_excursion(request, pk):
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


@api_view(['DELETE'])
@permission_classes((IsAdminUser,))
def delete_excursion(request, pk):
    try:
        excursion = Exscursion.objects.get(pk=pk)
        excursion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes((IsAdminUser,))
def get_countries(_):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAdminUser,))
def get_country(_, pk):
    try:
        country = Country.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CountrySerializer(country)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAdminUser,))
def add_country(request):
    serializer = CountrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes((IsAdminUser,))
def edit_country(request, pk):
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


@api_view(['DELETE'])
@permission_classes((IsAdminUser,))
def delete_country(request, pk):
    try:
        country = Country.objects.get(pk=pk)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
