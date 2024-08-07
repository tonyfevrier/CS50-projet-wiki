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
    if TITLE in util.list_entries():
        content = util.get_entry(TITLE)
        return render(request, "encyclopedia/entry.html", context={'content':content})
    else:
        suggestions = util.list_entries_containing_string(TITLE)
        return render(request, "encyclopedia/error.html", context={'suggestions':suggestions})
    

def query(request):
    """
    View to take the input search and to redirect to the corresponding entry page
    """
    TITLE = request.POST["q"]
    return redirect(f"/wiki/{TITLE}")


def newpage(request):
    """
    View of the page allowing the user to create his own page
    """
    return render(request, "encyclopedia/newpage.html")


def savenewpage(request):
    """
    View getting the information the user types during a page creation
    """
    title = request.POST['title']
    content = request.POST['content']
    
    if title not in util.list_entries():
        util.save_entry(title,content)
        return redirect(f"/wiki/{title}")
    else:
        message = 'Your entry is already part of the wiki. Thus you can not create a new page but only edit it.'
        return render(request, 'encyclopedia/newpage.html', context={'message':message})