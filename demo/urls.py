from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tasks.views import TaskViewSet, external_posts, status_counts
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register('api/tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('', include(router.urls)),
    path('api/external/posts/', external_posts),
    path('api/reports/status-counts/', status_counts),
]
