from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer


def getOrdersList(request):
    order = Order.objects.all().order_by('-updated')
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)


def getOrderDetail(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)


def createOrder(request):
    data = request.data
    order1 = Order.objects.create(
        body=data['body']
    )
    serializer = OrderSerializer(order1, many=False)
    return Response(serializer.data)

def updateOrder(request, pk):
    data = request.data
    order1 = Order.objects.get(id=pk)
    serializer = OrderSerializer(instance=order1, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteOrder(request, pk):
    order1 = Order.objects.get(id=pk)
    order1.delete()
    return Response('Order was deleted!')
