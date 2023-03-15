# Django imports
from django.urls import path


# Views imports
from apps.users.api.api import (
    user_api_view,
    user_detail_view,
    Login,
    Logout
)


# Urls
urlpatterns = [
    path(
        'user/',
        user_api_view,
        name='usuario_api_view'
    ),
    path(
        'user/<int:pk>/',
        user_detail_view,
        name='user_detail_api_view'
    ),
    path(
        'login/',
        Login.as_view(),
        name='login'
    ),
    path(
        'logout/',
        Logout.as_view(),
        name='logout'
    )
]