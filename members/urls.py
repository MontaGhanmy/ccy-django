from django.conf.urls import url
from .views import UserForm

app_name = 'members'

urlpatterns = [
    url(r'^$', UserForm.as_view() , name='index'),
]
