from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, external_posts, status_counts

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('external_posts/', external_posts, name='external-posts'),
    path('status_counts/', status_counts, name='status-counts'),
]
