# Django imports
from django.urls import path

# Views
from heroes.views import (
    HeroApiView,
    CreateHeroApiView,
    HeroDetailApiView,
    hero_api_view,
    )

# urls
urlpatterns = [
    path('heroes-list/', HeroApiView.as_view(), name='heroes_list'),
    path('create-heroe/', CreateHeroApiView.as_view(), name='create'),
    path('detail-heroe/<int:pk>/', HeroDetailApiView.as_view(), name='detail')
]