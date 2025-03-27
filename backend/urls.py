from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("tasks.urls")),
    path('api/', include('users.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
