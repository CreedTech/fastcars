from multiprocessing import context
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from account.forms import ProfileForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from account.models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Login successful')
            return redirect('login')
    else:
        form = ProfileForm()
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)

    # ===========================LOGIN=======================


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # admin
        if user:
            if user.is_active:
                login(request, user)
                if user.is_staff:
                    messages.success(request, 'Logged in Successfully')
                    return redirect('core:home')
                else:
                    messages.success(request, 'Logged in Successfully')
                    return redirect('core:home')
            else:
                messages.warning(request, 'Account is not active')
                return render(request, 'account/login.html')

        # The normal user
        elif user is not None and not user.is_staff:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'Account is not active')
                return render(request, 'account/login.html')
        else:
            messages.warning(request, 'please enter valid details')
            return render(request, 'account/login.html')
    else:
        return render(request, 'account/login.html')

# logout


def logout(request):
    auth.logout(request)
    return redirect('core:home')

# ==========================edit profile==================
@login_required
def edit_profile(request):
    if request.method == "POST":
        profile_form = EditProfileForm(
            request.POST or None, request.FILES, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            profile_form.save()
            if request.user.is_authenticated and request.user.is_staff:
                messages.success(request, 'Edited successfully')
                return redirect('core:home')
            elif request.user.is_authenticated and not request.user.is_staff:
                messages.success(request, 'Edited successfully')
                return redirect('core:home')

    else:
        profile_form = EditProfileForm(instance=request.user)

    context = {
        'profile_form': profile_form
    }

    return render(request, 'account/edit_profile.html', context)
