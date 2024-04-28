# Django imports
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.conf import settings

# Firebase imports
import firebase_admin
from firebase_admin import credentials, auth

# Import the forms module
from . import forms

# Create your views here.

cred = credentials.Certificate(settings.FIREBASE_ADMIN_SDK_CONFIG)
firebase_admin.initialize_app(cred)

@login_required()
def customerhomeview(request):
    """
    Renders the customer home page view.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response for the customer page.
    """
    return redirect(reverse("customer:customerprofileview"))


@login_required(login_url="/sign-in/?next=/customer/")
def customerprofileview(request):
    """
    Renders the customer profile page view.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response for the customer profile page.
    """

    user_form = forms.UserProfileForm(instance=request.user)
    customer_form = forms.CustomerProfileForm(instance=request.user.customer)
    password_form = PasswordChangeForm(request.user)

    if request.method == "POST":

        if request.POST.get("action") == "update_profile":
            user_form = forms.UserProfileForm(request.POST, instance=request.user)
            customer_form = forms.CustomerProfileForm(
                request.POST, request.FILES, instance=request.user.customer
            )

            if user_form.is_valid() and customer_form.is_valid():
                user_form.save()
                customer_form.save()

                messages.success(request, "Profile updated successfully! ")
                return redirect(reverse("customer:customerprofileview"))

        elif request.POST.get("action") == "update_password":
            password_form = PasswordChangeForm(request.user, request.POST)

            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Password updated successfully! ")
                return redirect(reverse("customer:customerprofileview"))
            
        elif request.POST.get("action") == "update_phone_number":
            firebase_user = auth.verify_id_token(request.POST.get("id_token"))

            request.user.customer.phone_number = firebase_user['phone_number']
            request.user.customer.save()
            return redirect(reverse("customer:customerprofileview"))

    return render(
        request,
        "core/customer/profile.html",
        {
            "user_form": user_form,
            "customer_form": customer_form,
            "password_form": password_form,
        },
    )
