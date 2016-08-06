from django.db import models

class Course(models.Model):
	course_author = models.CharField(max_length=50)
	course_name = models.CharField(max_length=80)
	course_draft = models.BooleanField(default=True)
	course_expect_desc = models.CharField(max_length=500, null=True, blank=True)
	course_req_desc = models.CharField(max_length=500, null=True, blank=True)
	course_result_desc = models.CharField(max_length=500, null=True, blank=True)

class Images(models.Model):
	parent_course  = models.CharField(max_length=50)
	image = models.FileField()
	

