from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register("sutdentModelApi",views.StudentModelViewSet,basename="studentModel")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path("getToken/",obtain_auth_token),
    path("getToken/",views.CustomAuthTokenView.as_view()),
    path('auth/',include("rest_framework.urls",namespace="rest_framework"),)
]
