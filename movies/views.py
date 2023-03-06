from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.models import Movie
from movies.serializers import MovieSerializer
from users.permissions import IsAdminOrReadOnly

class MovieView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
