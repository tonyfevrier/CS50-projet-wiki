#creation of a module to transform markdown in html

import re

def replace_by_h1(content):
    """
    Converts # in <h1> in a string content
    """
    return re.sub(r'^# (.*)(\n{1,})',r'<h1>\1</h1>\2',content, flags=re.MULTILINE)


def replace_by_h2(content):
    """
    Converts ## in <h2> in a string content
    """
    return re.sub(r'## (.*)(\n{1,})',r'<h2>\1</h2>\2',content,flags=re.MULTILINE)


def replace_by_strong(content):
    """
    Converts ** in <strong> in a string content
    """
    return re.sub(r'\*\*([^\*]+)\*\*',r'<strong>\1</strong>',content)


def replace_by_ul(content):
    """
    Converts * by <ul>,<li> tags
    """ 
    content = re.sub(r'^\* (.+)$',r'<li>\1</li>',content,flags=re.MULTILINE)  
    content = re.sub(r'<li>((?:[^<>]+</li>\n<li>){1,}[^<>]+)</li>',r'<ul><li>\1</li></ul>',content) 
    return content


def replace_by_p(content):
    """
    Converts contents without symbols at the beginning of a line by the tag <p>
    """ 
    return re.sub(r'^([^#*\n][^#\n]+)(\n{1,2}|$)',r'<p>\1</p>\2',content,flags=re.MULTILINE)
    

def replace_by_a(content):
    """
    Converts links in <a>
    """
    return re.sub(r'\[([a-zA-Z0-9 ]+)\]\(([a-zA-Z0-9/]+)\)',r'<a href="\2">\1</a>',content)


def convert(content):
    """
    Converts markdown to html using above functions
    """
    content = replace_by_p(content)
    content = replace_by_strong(content)
    content = replace_by_h2(content)
    content = replace_by_h1(content)
    content = replace_by_a(content)
    content = replace_by_ul(content)
    return re.sub("\n","",content)




