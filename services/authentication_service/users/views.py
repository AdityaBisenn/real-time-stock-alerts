import logging
from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer

# Configure logger
logger = logging.getLogger(__name__)

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        logger.info(f"New user registered: {response.data}")
        return response

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        logger.info("Login attempt received.")
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = RefreshToken.for_user(user)
                logger.info(f"User {user.username} logged in successfully.")
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                })
            logger.warning("Invalid login credentials.")
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        logger.error(f"Login validation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        try:
            token = request.data.get('token')
            if not token:
                logger.warning("Logout attempt without token.")
                return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            refresh_token = RefreshToken(token)
            refresh_token.blacklist()
            logger.info("User logged out successfully.")
            return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Logout failed: {str(e)}")
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

class ValidateView(APIView):
    def post(self, request):
        try:
            token = request.data.get('token')
            if not token:
                logger.warning("Validation attempt without token.")
                return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

            access_token = AccessToken(token)
            user_id = access_token['user_id']

            logger.info(f"Token validation successful for user_id: {user_id}")
            return Response({'user_id': user_id}, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Token validation failed: {str(e)}")
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        
class ProfileView(APIView):
    def get(self, request):
        try:
            user = request.user
            logger.info(f"Profile request for user {user.username}")
            return Response({
                'username': user.username,
                'email': user.email,
                'user_id': user.id
            })
        except Exception as e:
            logger.error(f"Profile request failed: {str(e)}")
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
