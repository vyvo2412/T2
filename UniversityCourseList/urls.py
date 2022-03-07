from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^CourseList/', include('CourseList.urls')),
    path('', include('CourseList.urls'))
]
