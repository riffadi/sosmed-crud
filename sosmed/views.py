from django.shortcuts import render

# Create your views here.
from .models import Instagram
from .forms import InstagramForm

def list(request):
	all_account = Instagram.objects.all()

	context = {
	'page_title' : 'Social Media',
	'all_account' : all_account,
	}

	return render(request, 'sosmed/list.html', context)