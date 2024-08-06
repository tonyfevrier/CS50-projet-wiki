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
    """
    si le titre correspond à une page alors on transmet son content sinon on génère une page d'erreur
    """
    if TITLE in util.list_entries():
        content = util.get_entry(TITLE)
        return render(request, "encyclopedia/entry.html", context={'content':content})
    else:
        return render(request, "encyclopedia/error.html")
