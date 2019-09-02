from django.shortcuts import render, redirect

from .models import Instagram
from .forms import InstagramForm


def update(request, update_id):
	account_update = Instagram.objects.get(id=update_id)
	
	data = {
		'first_name' : account_update.first_name,
		'last_name' : account_update.last_name,
		'username' : account_update.username,
	}

	account_form = InstagramForm(request.POST or None, initial=data, instance=account_update)

	if request.method == 'POST':
		if account_form.is_valid():
			account_form.save()

		return redirect('sosmed:list')

	context = {
			"page_title" : "Update Account",
			"account_form" : account_form,
	}

	return render(request, 'sosmed/create.html', context)


def delete(request,delete_id):
	Instagram.objects.filter(id=delete_id).delete()

	return redirect('sosmed:list')	


def create(request):
	account_form = InstagramForm(request.POST or None)

	if request.method == 'POST':
		if account_form.is_valid():
			account_form.save()

		return redirect('sosmed:list')

	context = {
			"page_title" : "Add Account",
			"account_form" : account_form,
	}

	return render(request, 'sosmed/create.html', context)


def list(request):
	all_account = Instagram.objects.all()

	context = {
	'page_title' : 'Social Media',
	'all_account' : all_account,
	}

	return render(request, 'sosmed/list.html', context)