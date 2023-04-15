#from django.shortcuts import render

from rest_framework import viewsets
from .models import Hackathonm, Submission, Enrollment
from .serializers import HackathonSerializer, SubmissionSerializer, EnrollmentSerializer

class HackathonViewSet(viewsets.ModelViewSet):
    queryset = Hackathonm.objects.all()
    serializer_class = HackathonSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer