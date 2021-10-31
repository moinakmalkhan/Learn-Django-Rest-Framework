
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("stuinfo/", views.student_list, name="oneobj"),
    path("stuinfo/<int:pk>/", views.student_detail, name="allobj"),
    path('admin/', admin.site.urls),
]
