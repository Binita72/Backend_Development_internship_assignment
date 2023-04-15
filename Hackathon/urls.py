from django.urls import path, include
from rest_framework import routers
from .views import HackathonViewSet, SubmissionViewSet, EnrollmentViewSet

router = routers.DefaultRouter()
router.register(r'hackathons', HackathonViewSet)
router.register(r'submissions', SubmissionViewSet)
router.register(r'enrollments', EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
