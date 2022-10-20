from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .auth_users.views import SignUpView, UserViewSet
from .Review_and_Comments.views import CommentViewSet, ReviewViewSet
from .Categories_Genres_Titles.views import (
    CategoriesViewSet,
    GenresViewSet,
    TitlesViewSet,
)


app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'auth', SignUpView, basename='auth')
router_v1.register(r'users', UserViewSet)

router_v1.register(
    'titles',
    TitlesViewSet,
    basename='titles'
)

router_v1.register(
    'genres',
    GenresViewSet,
    basename='genres'
)

router_v1.register(
    'categories',
    CategoriesViewSet,
    basename='categories'
)

router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='ReviewsView'
)

router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='ReviewsView'
)

router_v1.register(
    r'titles/(P<titles_id>\.+)/(?P<review_id>.+)/comments',
    CommentViewSet,
    basename='CommentsView'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
