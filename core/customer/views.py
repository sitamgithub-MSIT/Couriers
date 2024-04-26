from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


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

    if request.method == "POST":
        user_form = forms.UserProfileForm(request.POST, instance=request.user)
        customer_form = forms.CustomerProfileForm(
            request.POST, request.FILES, instance=request.user.customer
        )

        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            return redirect(reverse("customer:customerprofileview"))

            
    return render(request, "core/customer/profile.html", {"user_form": user_form, "customer_form": customer_form})
