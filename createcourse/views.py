from .models import Course
from django.views.generic import TemplateView
from django.views.generic import  View
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

class Index(View):
	template_name = "createcourse/index.html"
	def get(self, request):
		courses = Course.objects.filter(course_author=request.user.username)
		return render(request, self.template_name, context={'courses': courses})
	def post(self, request):
		try:
			Course.objects.get(course_author=request.user.username, course_name=request.POST['coursename'])
		except ObjectDoesNotExist:
			newcourse = Course(course_author=request.user.username, course_name=request.POST['coursename'])
			newcourse.save()
			courses = Course.objects.filter(course_author=request.user.username)
			return render(request, self.template_name, context={'message':'Course Created! Please add description for the audience.','courses':courses})
		courses = Course.objects.filter(course_author=request.user.username)
		return render(request, self.template_name, context={'message':'Course exists ! Please pick another name.','courses':courses})
