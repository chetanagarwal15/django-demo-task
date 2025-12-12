from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.db.models import Count
import requests

# CRUD API for Task Model
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

# External API Example
@api_view(['GET'])
def external_posts(request):
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    return Response(r.json()[:10])   # return top 10 posts

# Report API: Count tasks by status
@api_view(['GET'])
def status_counts(request):
    try:
        data = Task.objects.values("status").annotate(count=Count("id"))
        result = {x["status"]: x["count"] for x in data}

        # Ensure all keys exist
        for k in ["todo", "in-progress", "done"]:
            result.setdefault(k, 0)

        return Response(result)
    except Exception as e:
        print("Error in status_counts:", e)
        return Response({
            "todo": 0,
            "in-progress": 0,
            "done": 0,
            "error": str(e)
        })
