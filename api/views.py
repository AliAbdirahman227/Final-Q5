from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Order
from .serializers import OrderSerializer
from api import serializers
from .utils import updateOrder, getOrderDetail, deleteOrder, getOrdersList, createOrder
# Create your views here.


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/order/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of order'
        },
        {
            'Endpoint': '/order/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single order object'
        },
        {
            'Endpoint': '/order/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new order with data sent in post request'
        },
        {
            'Endpoint': '/order/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing order with data sent in post request'
        },
        {
            'Endpoint': '/order/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting order'
        },
    ]
    return Response(routes)



@api_view(['GET', 'POST'])
def getOrders(request):

    if request.method == 'GET':
        return getOrdersList(request)

    if request.method == 'POST':
        return createOrder(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getOrder(request, pk):

    if request.method == 'GET':
        return getOrderDetail(request, pk)

    if request.method == 'PUT':
        return updateOrder(request, pk)

    if request.method == 'DELETE':
        return deleteOrder(request, pk)

