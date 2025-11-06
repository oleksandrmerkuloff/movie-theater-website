from django.contrib.auth import logout, authenticate, login
from django.shortcuts import get_object_or_404, render, redirect

from orders.models import Order
from accounts.models import User


def profile_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    orders = Order.objects.filter(user=user)
    return render(request, 'accounts/profile.html', {
        'user': user,
        'orders': orders
        })


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    if request.method == "POST":
        phone = request.POST["phone"]
        password = request.POST["password"]
        remember = request.POST.get("remember")

        user = authenticate(request, phone=phone, password=password)
        if user:
            login(request, user)

            if not remember:
                request.session.set_expiry(0)

            return redirect("home")

        return render(request, "accounts/login.html", {"form": {"errors": True}})

    return render(request, "accounts/login.html", {"form": {}})


def register_view(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        p1 = request.POST.get("password1")
        p2 = request.POST.get("password2")

        # Password check
        if p1 != p2:
            return render(request, "account/register.html", {
                "errors": "Passwords do not match."
            })

        # Username exists
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

    return render(request, "accounts/register.html")
