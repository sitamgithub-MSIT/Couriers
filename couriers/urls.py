"""
URL configuration for couriers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views

from core.customer import views as customer_views
from core.courier import views as courier_views

customer_urls = [
    path("", customer_views.customerhomeview, name="customerhomeview"),
]

courier_urls = [
    path("", courier_views.courierhomeview, name="courierhomeview"),
]

# URL patterns for the couriers project.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("social_django.urls", namespace="social")),
    path("", views.homepageview, name="homepageview"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html")),
    path("logout/", auth_views.LogoutView.as_view(next_page="/")),
    path("sign-up/", views.registerpageview, name="registerpageview"),
    path("customer/", include((customer_urls, "customer"))),
    path("courier/", include((courier_urls, "courier"))),
]
