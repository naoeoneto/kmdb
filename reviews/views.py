from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdminOrCriticOrReadOnly
from django.shortcuts import get_object_or_404
from movies.models import Movie

class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCriticOrReadOnly]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'pk'


    def perform_create(self, serializer):
        movie_req = self.kwargs.get('movie_id')
        my_movie = get_object_or_404(Movie, id=movie_req)
        return serializer.save(movie_id=my_movie.id, critic=self.request.user)
