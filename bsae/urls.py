from django.urls import path
from .views import *

app_name = 'onlineeducation'

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('profiles/', ProfileList.as_view(), name="profile-list"),
    path('profiles/create/', ProfileCreate.as_view(), name="profile-create"),
    path('watch/<str:profile_id>/', MovieList.as_view(), name="movie-list"),
    path('title/',MovieLanguage.as_view(),name='movielanguage'),
    path('watch/detail/<str:movie_id>/', MovieDetail.as_view(), name="movie-detail"),
    path('watch/play/<str:movie_id>/', PlayMovie.as_view(), name="play-movie"),
    path("quiz/totalinternalreflection/",totalinternalreflection,name='totalinternamreflection'),
    path("quiz/emf/",emf,name='emf'),
]
