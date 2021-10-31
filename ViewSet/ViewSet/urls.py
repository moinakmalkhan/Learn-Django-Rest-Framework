from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("sutdentApi",views.StudentViewSet,basename="student")
router.register("sutdentModelApi",views.StudentModelViewSet,basename="studentModel")
router.register("sutdentReadOnlyModelApi",views.StudentReadOnlyModelViewSet,basename="studentReadOnlyModel")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
