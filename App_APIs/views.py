from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class MyModelList(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

class MyModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'MyModel': reverse('mymodel-list', request=request, format=format),
        # Add more endpoints here as needed
    })