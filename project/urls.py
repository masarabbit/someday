
from django.contrib import admin
from django.urls import path, include, re_path
# from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('jwt_auth.urls')),
    path('api/todos/', include('todos.urls')),
    # re_path(r'^.*$', index)
]
