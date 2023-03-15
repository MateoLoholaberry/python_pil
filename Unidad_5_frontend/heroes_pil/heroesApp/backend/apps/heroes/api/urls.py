# Django imports
from django.urls import path

# Views imports
from apps.heroes.api.views import HeroApiView, HeroDetailApiView


# Urls
urlpatterns = [
    path(
        'heroes/', HeroApiView.as_view(), name='heroes_api'
    ),
    path(
        'heroes/<int:pk>',HeroDetailApiView.as_view(), name='heroes_deatail_api'
    )
]