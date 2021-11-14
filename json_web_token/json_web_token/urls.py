
from django.contrib import admin
from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("getToken/",TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path("refreshToken/",TokenRefreshView.as_view(),name='token_refresh'),
    path("verifyToken/",TokenVerifyView.as_view(),name='token_verify'),
    path("studentapifunctionbased/", views.FunctionBasedStudentAPI),
    path("studentapifunctionbased/<int:pk>", views.FunctionBasedStudentAPI),
    path("studentapiclassbased/", views.ClassBasedStudentAPI.as_view()),
    path("studentapiclassbased/<int:pk>", views.ClassBasedStudentAPI.as_view()),
]
