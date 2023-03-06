from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView
from users.permissions import IsAdmin

from .models import User
from .serializers import UserSerializer


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]
    
    serializer_class = UserSerializer

    def get_queryset(self):     
        return User.objects.all()
    
    def perform_create(self, serializer):
        return serializer.save()
