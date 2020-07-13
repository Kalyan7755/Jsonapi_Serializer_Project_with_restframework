from django.db import models
# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=20)
    def __str__(self):
        return "{}".format(self.subject_name)

class PersonCaseStudyDetails(models.Model):
    person_name = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=13,null=True)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='case_study_subject')
    def __str__(self):
        return "{}".format(self.person_name)