from .models import Course, Images, Videos
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

flag = {'off': True, 'on': False}
class CourseDetails(View):
	template_name = "createcourse/coursedetails.html"
	def get(self, request, course_id):
		course = Course.objects.get(id=course_id)
		images = Images.objects.filter(parent_course=course_id)
		videos = Videos.objects.filter(parent_course=course_id)
		return render(request, self.template_name, context={'course':course,'images':images, 'videos':videos} )
	def post(self, request, course_id):
		if request.FILES.get('courseimage', False):
			newimage = Images(parent_course=course_id, image=request.FILES.get('courseimage', False))
			newimage.save()
		if request.FILES.get('coursevideo', False):
			newvideo = Videos(parent_course=course_id, video=request.FILES.get('coursevideo', False))
			newvideo.save()
		course = Course.objects.get(id=course_id)
		course.course_expect_desc = request.POST.get('cname','')
		course.course_expect_desc = request.POST.get('cexpectdesc','')
		course.course_req_desc = request.POST.get('creqdesc','')
		course.course_result_desc = request.POST.get('cresultdesc','')
		course.avability_start_date = request.POST.get('avabilitysd','')
		course.avability_end_date = request.POST.get('avabilityed','')
		course.avability_start_time = request.POST.get('ast','')
		course.avability_start_time_period = request.POST.get('astp','')
		course.avability_end_time = request.POST.get('aet','')
		course.avability_end_time_period = request.POST.get('aetp','')
		# webinar mode details
		course.webinar_price = request.POST.get('wprice','')
		course.webinar_duration = request.POST.get('wduration','')
		course.webinar_is_free = request.POST.get('wisfree','off')
		course.webinar_price_per_access = request.POST.get('wppa','')
		course.webinar_max_num = request.POST.get('wmaxnum','')
		course.webinar_subsequent_ed = request.POST.get('subsquent','')
		course.webinar_category = request.POST.get('wcategory','')

		# video mode details
		course.video_price = request.POST.get('vprice','')
		course.video_duration = request.POST.get('vduration','')
		course.video_is_free = request.POST.get('visfree','off')
		course.video_subsequent_ed = request.POST.get('vsubsquent','')
		course.video_category = request.POST.get('vcategory','')


		course.course_draft = flag[request.POST.get('isdraft', 'off')]
		course.save()
		images = Images.objects.filter(parent_course=course_id)
		videos = Videos.objects.filter(parent_course=course_id)
		return render(request, self.template_name, context={'course':course,'images':images, 'videos':videos} )

def deletCourse(request, course_id):
	try: 
		course = Course.objects.get(id=course_id)
	except ObjectDoesNotExist:
		return redirect('createcourse:index')

	relatedimgs = Images.objects.filter(parent_course=course_id)
	relatedvids = Videos.objects.filter(parent_course=course_id)
	relatedimgs.delete()
	relatedvids.delete()
	course.delete()
	return redirect('createcourse:index')
