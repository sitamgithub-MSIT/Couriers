from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


def homepageview(request):
    """
    Renders the homepage view.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response for the homepage.
    """
    return render(request, "core/home.html")


@login_required()
def customerpageview(request):
    """
    Renders the customer page view.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response for the customer page.
    """
    return render(request, "core/home.html")


@login_required()
def courierpageview(request):
    """
    Renders the courier page view.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response for the courier page.
    """
    return render(request, "core/home.html")


def registerpageview(request):
    """
    View function for the registration page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """

    # Create a new instance of the UserRegisterForm
    form = forms.UserRegisterForm()

    # If the form is submitted
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)

        # If the form is valid
        if form.is_valid():

            # Save the form
            user = form.save(commit=False)
            user.username = user.email
            user.save()

            # Log the user in and redirect to the home page
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("/")

    # Render the registration page with the form
    return render(request, "core/register.html", {"form": form})
