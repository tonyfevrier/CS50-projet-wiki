from django.shortcuts import render,redirect

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
    

def query(request):
    """
    View to take the input search and to redirect to the corresponding entry page
    """
    TITLE = request.POST["q"]
    return redirect(f"/wiki/{TITLE}")


def error(request):
    """
    View rendering an error page when the list of entries does not contain the query
    """
    return render(request, "error.html")