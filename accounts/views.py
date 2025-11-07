from django.contrib.auth import logout, authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from orders.models import Order
from accounts.models import User
from accounts.forms import (
    UserProfileForm,
    LoginForm,
    RegisterForm,
    NewPasswordForm
    )


def profile_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid() and form.has_changed():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('test-profile', pk=user.id)
    else:
        form = UserProfileForm(instance=user)
    orders = Order.objects.filter(user=user)
    return render(request, 'accounts/profile.html', {
        'form': form,
        'orders': orders
        })


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            remember = form.cleaned_data['remember']

            user = authenticate(request, phone=phone, password=password)
            if user:
                login(request, user)

                if not remember:
                    request.session.set_expiry(0)

                return redirect("home")

        return render(request, "accounts/login.html", {
            "form": {"errors": True}
            })
    form = LoginForm()
    return render(request, "accounts/login.html", {'form': form})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data["phone"]
            fname = form.cleaned_data["fname"]
            lname = form.cleaned_data["lname"]
            p1 = form.cleaned_data["password1"]
            p2 = form.cleaned_data["password2"]

            if p1 != p2:
                return render(request, "account/register.html", {
                    "errors": "Passwords do not match."
                })

            if User.objects.filter(phone=phone).exists():
                return render(request, "account/register.html", {
                    "errors": "User already exists."
                })

            user = User.objects.create_user(
                phone=phone,
                fname=fname,
                lname=lname,
                password=p1
                )
            login(request, user)
            return redirect("home")
    form = RegisterForm()
    return render(request, "accounts/register.html", {'form': form})


def reset_password_view(request):
    if request.method == 'POST':
        form = NewPasswordForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password1']
            user = get_object_or_404(User, phone=phone)
            user.set_password(password)
            user.save()
            return redirect('home')
    form = NewPasswordForm()
    return render(request, 'accounts/password_reset.html', {'form': form})
