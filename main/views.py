from django.shortcuts import render, redirect

# ---------------------------------------
# Home Page
# ---------------------------------------
def home(request):
    return render(request, 'main/home.html')


# ---------------------------------------
# User Pages
# ---------------------------------------
def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Accept ANY dummy values for now (no DB yet)
        if email and password:
            request.session["logged_in"] = True  # store simple session login flag
            return redirect("book")  # redirect to Book Appointment

    return render(request, "main/login.html")


def signup_page(request):
    return render(request, 'main/signup.html')


def user_dashboard(request):
    return render(request, 'main/user_dashboard.html')


def appointment_history(request):
    return render(request, 'main/appointment_history.html')


def book_appointment(request):
    # Later we can add: if not logged in -> redirect to login
    return render(request, 'main/book_appointment.html')


# ---------------------------------------
# Astrologer Pages
# ---------------------------------------
def astrologer_profile(request):
    return render(request, 'main/astrologer_profile.html')


def astro_login(request):
    return render(request, 'main/astro_login.html')


def astro_dashboard(request):
    return render(request, 'main/astro_dashboard.html')


def schedule_management(request):
    return render(request, 'main/schedule_management.html')


# ---------------------------------------
# Admin Pages
# ---------------------------------------
def admin_login(request):
    return render(request, 'main/admin_login.html')


def admin_dashboard(request):
    return render(request, 'main/admin_dashboard.html')