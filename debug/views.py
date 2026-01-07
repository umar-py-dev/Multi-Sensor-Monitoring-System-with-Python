from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DebugLog 
from .serializers import DebugSerializer

@api_view(['GET'])
def debug_log(request):
    
    dataset = DebugLog.objects.all().order_by('-created_at')
    serialized = DebugSerializer(dataset, many=True)
    
    return Response(serialized.data)