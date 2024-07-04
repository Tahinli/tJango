from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_token import views as user_token_views

router = DefaultRouter()
router.register(r"", user_token_views.UserTokenViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
