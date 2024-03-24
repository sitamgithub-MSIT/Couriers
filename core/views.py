from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
