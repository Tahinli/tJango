from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views as user_views

router = DefaultRouter()
router.register(r"  ", user_views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
