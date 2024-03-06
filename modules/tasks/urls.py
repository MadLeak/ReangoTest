"""
Task URLs
"""

from rest_framework import routers
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from .views import TaskView

# Task router
router = routers.DefaultRouter()
router.register(
    r"tasks",
    TaskView,
)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="Tasks API")),
]
