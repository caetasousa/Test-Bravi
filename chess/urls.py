from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from chess.piece.views import PieceId, PieceMove

router = routers.DefaultRouter()

router.register('piece-id', PieceId, basename='piece-id')
router.register('piece-move', PieceMove, basename='piece-move')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
]