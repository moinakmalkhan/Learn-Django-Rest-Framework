from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("sutdentModelApi",views.StudentModelViewSet,basename="studentModel")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path("getToken/",obtain_auth_token),
    path('auth/',include("rest_framework.urls",namespace="rest_framework"),)
]
