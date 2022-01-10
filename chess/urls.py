from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from chess.piece.views import  PieceId

router = routers.DefaultRouter()

router.register('piece-id', PieceId, basename='piece-id')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
]