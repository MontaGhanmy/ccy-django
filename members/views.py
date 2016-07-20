from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

def index(request):
	return render(request, 'members/index.html')

class UserForm(TemplateView):
    template_name = "members/index.html"
    def get(self, request):
    	return render(request, 'members/index.html', context = {'action_type': request.GET['action_type'],})
    def post(self, request):
    	user = User.objects.create_user(request.POST['full-name'], request.POST['e-mail'], request.POST['password'])

    	return render(request, 'members/index.html', context = {'user_message': 'You just signed up to the website. Welcome !',})
