from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tasks.views import TaskViewSet, external_posts, status_counts
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Frontend
    path('', TemplateView.as_view(template_name='index.html'), name='home'),

    # API
    path('api/', include(router.urls)),
    path('api/external/posts/', external_posts, name='external-posts'),
    path('api/reports/status-counts/', status_counts, name='status-counts'),
]
