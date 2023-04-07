from rest_framework.generics import CreateAPIView, ListAPIView

from .serializer import InvoiceSerializer, UserSerializer, User


class ClientList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class InvoiceCreate(CreateAPIView):
    serializer_class = InvoiceSerializer
