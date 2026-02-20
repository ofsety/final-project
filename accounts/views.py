from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

from .models import Profile
from stox.models import StockXPrice

    
def profile(request):
    user=request.user
    profile=user.profile
    total_requests = StockXPrice.objects.filter(user=user).count()

    context = {
        "profile": profile,
        "total_requests": total_requests,
    }


    return render(request,"accounts/profile.html",context)  
    
@login_required
def profile_edit(request):
    profile = request.user.profile

    if request.method == "POST":
        profile.region = request.POST.get("region")
        new_username = request.POST.get("username")

        User.objects.filter(username=request.user.username).update(username=new_username)

        profile.save()

        return redirect("profile")

    return render(request, "accounts/profile_edit.html", {
        "profile": profile
    })

@login_required
def profile_delete(request):

    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        return redirect("home")

    return render(request, "accounts/profile_delete.html")