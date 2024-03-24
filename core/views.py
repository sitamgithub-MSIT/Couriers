from django.shortcuts import render

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
