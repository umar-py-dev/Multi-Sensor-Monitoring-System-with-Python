from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response 
from .models import Data
from .serializers import DataSerializer



@api_view(['GET'])
def get_sensor_data(request, sensor_id_url, device_id_url):
    
    dataset = Data.objects.filter(sensor_id__id=sensor_id_url,
                                  sensor_id__device_id = device_id_url
                                  ).order_by('-created_at')
    
    paginator = PageNumberPagination()
    paginator.page_size = 10 
    
    # ye btai ga ke konsa page manga gya he:
    result_page = paginator.paginate_queryset(dataset, request)
    serializer = DataSerializer(result_page, many=True)
    
    return paginator.get_paginated_response(serializer.data)
    # .get_paginated_response, json ko properly pages ki shakal me render kre ga
    # or btay ga: current page num, previous page, next page etc...


class DataFilterView(ListAPIView):
    queryset = Data.objects.all().order_by('-created_at')
    serializer_class = DataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'created_at': ['gte', 'lte'],
        'sensor_id': ['exact'],
        'sensor_id__device_id': ['exact']
    }

