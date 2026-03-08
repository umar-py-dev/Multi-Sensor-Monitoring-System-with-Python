from rest_framework.decorators import api_view

from rest_framework.pagination import PageNumberPagination
from .models import DebugLog 
from .serializers import DebugSerializer

@api_view(['GET'])
def debug_log(request):
    
    dataset = DebugLog.objects.all().order_by('-created_at')
    paginator = PageNumberPagination()
    paginator.page_size = 25
    
    # ye btai ga ke konsa page manga gya he:
    result_page = paginator.paginate_queryset(dataset, request)
    serializer = DebugSerializer(result_page, many=True)
    
    return paginator.get_paginated_response(serializer.data)