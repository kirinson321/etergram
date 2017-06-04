from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def logout_view(request):
    """logging the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('etergrams:index'))


def register(request):
    """registering a new user"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('etergrams:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
