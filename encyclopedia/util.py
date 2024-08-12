import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """   
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename) 
    default_storage.save(filename, ContentFile(content)) 


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8").replace("\r\n","\n")
    except FileNotFoundError:
        return None

def list_entries_containing_string(title):
    """
    Returns a list of all names of encyclopedia entries containing a given title
    """
    _, filenames = default_storage.listdir("entries")
    entries = []
    for filename in filenames:
        if title in filename:
            entries.append(re.sub(r"\.md$", "", filename))
    return sorted(entries)

def clean_title(title):
    """
    Takes a title and eliminates superfluous spaces at the beginning or the end of the string
    """  
    word_beginning, end_beginning = 0, len(title)

    #clean the beginning of the word
    for i in range(len(title)):
        if title[i] != " ":
            break
        word_beginning += 1 

    #clean the end of the word
    for i in range(len(title)):
        if title[-i-1] != " ":
            break
        end_beginning -= 1 
    
    return title[word_beginning:end_beginning]