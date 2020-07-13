from . serializers import SubjectSerializers,PersonCaseStudyDetailsSerializers
from . models import Subject,PersonCaseStudyDetails
from rest_framework import viewsets

class Subjectview(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers

class PersonCaseStudyDetailsView(viewsets.ModelViewSet):
    queryset = PersonCaseStudyDetails.objects.all()
    serializer_class = PersonCaseStudyDetailsSerializers