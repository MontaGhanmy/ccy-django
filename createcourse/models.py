from django.db import models

class Course(models.Model):
	course_author = models.CharField(max_length=50)
	course_name = models.CharField(max_length=80)
	course_aud_desc = models.CharField(max_length=500, null=True, blank=True)

