from django.conf.urls import url
from . import views
from .views import Index, CourseDetails

app_name = "createcourse"


urlpatterns = [
    url(r'^$', Index.as_view() , name='index'),
    url(r'^(?P<course_id>[0-9]+)/$', CourseDetails.as_view() , name='addoursedetails'),
    url(r'^delete/(?P<course_id>[0-9]+)/$', views.deletCourse , name='deletcourse'),
]