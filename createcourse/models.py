from django.db import models

class Course(models.Model):
	course_author = models.CharField(max_length=50)
	course_name = models.CharField(max_length=80)
	course_draft = models.BooleanField(default=True)
	course_expect_desc = models.CharField(max_length=500, null=True, blank=True)
	course_req_desc = models.CharField(max_length=500, null=True, blank=True)
	course_result_desc = models.CharField(max_length=500, null=True, blank=True)
	# Avability in next 2 months
	avability_start_date = models.CharField(max_length=500, null=True, blank=True)
	avability_end_date = models.CharField(max_length=500, null=True, blank=True)
	avability_start_time = models.CharField(max_length=50, null=True, blank=True)
	avability_start_time_period = models.CharField(max_length=5, null=True, blank=True)
	avability_end_time = models.CharField(max_length=50, null=True, blank=True)
	avability_end_time_period = models.CharField(max_length=5, null=True, blank=True)

	#Webinar mode details
	webinar_price = models.CharField(max_length=5, null=True, blank=True)
	webinar_duration = models.CharField(max_length=5, null=True, blank=True)
	webinar_is_free = models.CharField(max_length=5, null=True, blank=True)
	webinar_price_per_access = models.CharField(max_length=5, null=True, blank=True)
	webinar_max_num = models.CharField(max_length=5, null=True, blank=True)
	webinar_subsequent_ed = models.CharField(max_length=5, null=True, blank=True)
	webinar_category = models.CharField(max_length=50, null=True, blank=True)

	#video mode details
	video_price = models.CharField(max_length=5, null=True, blank=True)
	video_duration = models.CharField(max_length=5, null=True, blank=True)
	video_is_free = models.CharField(max_length=5, null=True, blank=True)
	video_subsequent_ed = models.CharField(max_length=5, null=True, blank=True)
	video_category = models.CharField(max_length=50, null=True, blank=True)

class Images(models.Model):
	parent_course  = models.CharField(max_length=50)
	image = models.FileField()

class Videos(models.Model):
	parent_course  = models.CharField(max_length=50)
	video = models.FileField()

