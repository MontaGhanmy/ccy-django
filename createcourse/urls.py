from django.conf.urls import url
from . import views
from .views import Index

app_name = "createcourse"


urlpatterns = [
    url(r'^$', Index.as_view() , name='index'),
]