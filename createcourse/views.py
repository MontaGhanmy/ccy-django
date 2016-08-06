from .models import Course, Images
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
			if request.POST['coursename'] and not request.POST['coursename'].isspace():
				newcourse = Course(course_author=request.user.username, course_name=request.POST['coursename'])
				newcourse.save()
				courses = Course.objects.filter(course_author=request.user.username)
				return render(request, self.template_name, context={'message':'Course Created! Please add description for the audience.','courses':courses})
			else:
				courses = Course.objects.filter(course_author=request.user.username)
				return render(request, self.template_name, context={'message':'Error ! Please enter a valid course name.','courses':courses})			
		courses = Course.objects.filter(course_author=request.user.username)
		return render(request, self.template_name, context={'message':'Course exists ! Please pick another name.','courses':courses})


class CourseDetails(View):
	template_name = "createcourse/coursedetails.html"
	def get(self, request, course_id):
		course = Course.objects.get(id=course_id)
		images = Images.objects.filter(parent_course=course_id)
		return render(request, self.template_name, context={'message':course,'images':images} )
	def post(self, request, course_id):
		if request.FILES.get('courseimage', False):
			newimage = Images(parent_course=course_id, image=request.FILES.get('courseimage', False))
			newimage.save()
		course = Course.objects.get(id=course_id)
		course.course_expect_desc = request.POST.get('cexpectdesc','')
		course.course_req_desc = request.POST.get('creqdesc','')
		course.course_result_desc = request.POST.get('cresultdesc','')
		course.save()
		images = Images.objects.filter(parent_course=course_id)
		return render(request, self.template_name, context={'message':course,'images':images} )

def deletCourse(request, course_id):
	try: 
		course = Course.objects.get(id=course_id)
	except ObjectDoesNotExist:
		return redirect('createcourse:index')
	course.delete()
	return redirect('createcourse:index')
