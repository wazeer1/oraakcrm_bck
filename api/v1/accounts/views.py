from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .serializers import *
from accounts.models import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny



@api_view(["POST"])
@permission_classes((AllowAny,))
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        if UserProfile.objects.filter(user=user).exists():
            user_profile = UserProfile.objects.get(user=user)
            response_data = {
                "StatusCode": 6000,
                "data": {
                    "message" : "Logged in successfully",
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh),
                    "user_type":  user_profile.user_type,
                    "user_role": user_profile.user_role,
                }
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                "StatusCode": 6000,
                "data": {
                    "message" : "User profile not found",
                }
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)