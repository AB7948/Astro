from django.urls import path
from . import views

urlpatterns = [

    # ---------------------
    # Home
    # ---------------------
    path('', views.home, name='home'),

    # ---------------------
    # User Pages
    # ---------------------
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('user/dashboard/', views.user_dashboard, name='user_dashboard'),
    path('appointment/history/', views.appointment_history, name='appointment_history'),
    path('book/', views.book_appointment, name='book'),

    # ---------------------
    # Astrologer Pages
    # ---------------------
    path('astrologer/profile/', views.astrologer_profile, name='astrologer_profile'),
    path('astro/login/', views.astro_login, name='astro_login'),
    path('astro/dashboard/', views.astro_dashboard, name='astro_dashboard'),
    path('astro/schedule/', views.schedule_management, name='schedule_management'),

    # ---------------------
    # Admin Pages
    # ---------------------
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
]