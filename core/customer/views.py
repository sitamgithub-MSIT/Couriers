from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
    return render(request, "core/home.html")
