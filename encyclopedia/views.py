from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,TITLE):
    """
    View rendering the content of the theme given by TITLE
    """
    return render(request, "encyclopedia/entry.html")
