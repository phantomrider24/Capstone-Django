from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include("django.contrib.auth.urls")),
    path('', include("user_auth.urls")),

]
