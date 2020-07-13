from rest_framework import serializers
from . models import PersonCaseStudyDetails,Subject
from django.core import validators

class PersonCaseStudyDetailsSerializers(serializers.HyperlinkedModelSerializer):
    '''
    [
    {
        "person_name": "Sneha Sunil Pawar",
        "contact_no": "9867660000",
        "subject_name": "http://127.0.0.1:8000/blog/api/subject/5/"
    },
    {
        "person_name": "Anand Ankush Sharma.",
        "contact_no": "7655555555",
        "subject_name": "http://127.0.0.1:8000/blog/api/subject/5/"
    }
   ]'''
    contact_no = serializers.CharField(
        required=False,
        validators=[
            validators.RegexValidator('^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$', message='Please check you contact no'),
        ]
    )
    class Meta:
        model = PersonCaseStudyDetails
        fields = ('person_name','contact_no','subject_name')


class SubjectSerializers(serializers.HyperlinkedModelSerializer):
    subject_name = serializers.CharField(
        required=True,
    )
    class Meta:
        model = Subject
        fields = ('subject_name',)


