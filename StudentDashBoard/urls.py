from django.urls import path,include
from django.views.generic import TemplateView
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
    path('frontend/', TemplateView.as_view(template_name='StudentDashBoard/frontend.html'), name='frontend'),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh')]
