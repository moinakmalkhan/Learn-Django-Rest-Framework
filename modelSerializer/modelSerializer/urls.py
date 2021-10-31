from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("studentapiclassbased/", views.StudentApiClassBased.as_view()),
    path("studentapifunctionbased/", views.StudentApiFunctionBased),
]
