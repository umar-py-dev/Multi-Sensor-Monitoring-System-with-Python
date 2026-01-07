from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from .models import AppUsers
from .serializers import LoginSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    
    serializer = LoginSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    
    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    try:
        user = AppUsers.objects.get(name=username)
    except AppUsers.DoesNotExist:
        return Response({'error': 'Bhai jan username galata a.'}, status=404)
    
    if check_password(password, user.password) == False:
        return Response({'error': 'Password galat a pyn!'}, status=404)
    
    
    token = RefreshToken.for_user(user)
    
    return Response({
        'access': str(token.access_token),
        'refresh': str(token),
        'role': (user.role)
    })
    
    
    