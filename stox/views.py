from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Min, Max

from .forms import PriceCheckForm, LoginForm
from .models import StockXPrice
from .Playwright_file import get_stockx_price
from accounts.models import Profile

@login_required
def tracking_price(request):
    form = PriceCheckForm()
    print("METHOD:", request.method)
    print("POST DATA:", request.POST)
    if request.method == "POST":
        form = PriceCheckForm(request.POST)

        if form.is_valid():
            url = request.POST.get("url")
            size = request.POST.get("size")
            profile = Profile.objects.get(user=request.user)
            region = profile.region
            price = get_stockx_price(url,size,region)
            StockXPrice.objects.create(
                url=url,
                size=size,
                price=price,
                user_id=request.user.id
            )
        return redirect("history")
    
    else:
        form = PriceCheckForm()
    return render(request, "stox/tracking_price.html", {"form": form})

@login_required
def history(request):
    prices = StockXPrice.objects.filter(user=request.user).order_by("-created_at")

    size = request.GET.get("size")
    if size:
        prices = prices.filter(size=size)

    sort = request.GET.get("sort", "asc")

    if sort == "desc":
        prices = prices.order_by("-price")
    else:
        prices = prices.order_by("price")
    
    min_price = prices.aggregate(Min("price"))["price__min"]
    max_price = prices.aggregate(Max("price"))["price__max"]

    sizes = (
        StockXPrice.objects
        .filter(user=request.user)
        .values_list("size", flat=True)
        .distinct()
    )

    context = {
        "prices": prices,
        "min_price": min_price,
        "max_price": max_price,
        "sort": sort,
        "sizes": sizes,
        "selected_size": size,
    }

    return render(request, "stox/history.html", context)


def register(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password") 

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists")
            return redirect("register")
        
        user = User.objects.create_user(username=username, password=password) 

        login(request, user) 
        
        return redirect("history")

    return render(request, "stox/register.html")


def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
           
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("history")

            form.add_error(None, "Invalid credentials")

    return render(request, "stox/login.html", {"form": form,})

@login_required
def logout_view(request):
    logout(request)

    return redirect("home")

def home(request):
    return render(request, "stox/home.html")

    
class StockXPriceDeleteView(LoginRequiredMixin,DeleteView):
    model = StockXPrice
    success_url = reverse_lazy("history")

    def get_queryset(self):
        return StockXPrice.objects.filter(user=self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.delete(request,*args, **kwargs)