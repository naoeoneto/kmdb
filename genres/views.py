from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from genres.models import Genre
from movies.serializers import GenreSerializer
from users.permissions import IsAdminOrReadOnly


class GenreView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
