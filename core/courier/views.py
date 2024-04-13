from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def courierhomeview(request):
    """
    Renders the courier home page view.
    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response for the courier page.
    """
    return render(request, "core/home.html")
