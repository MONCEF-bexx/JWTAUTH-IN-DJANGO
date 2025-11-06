from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
router = DefaultRouter()

router.register(r'students',views.StudentViewSet, basename = 'student')
router.register(r'teachers',views.TeacherViewSet,basename = 'teacher')
urlpatterns = [
    path('',include(router.urls)),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh')]
