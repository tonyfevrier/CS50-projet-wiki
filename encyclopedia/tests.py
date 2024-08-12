from django.test import TestCase
from django.core.files.storage import default_storage

from encyclopedia.util import clean_title
import encyclopedia.markdownify as md 
from . import util

class TestEntriesUpdating(TestCase):

    def test_newpage_creation(self):
        """
        Test that the page is registered after its creation with the correct content.
        """
        #we create a new page
        title = 'testing'
        content = "#test\n\nCeci est le contenu de test."
        self.client.post("/savenewpage/",data={'title':title, 'content':content})

        #we verify the creation of the file and the associated content 
        _,filenames = default_storage.listdir('entries') 
        self.assertIn("testing.md",filenames) 
        self.assertEqual(util.get_entry("testing"),content)

        #we clean the data 
        default_storage.delete("entries/testing.md")
        
    def test_editpage(self):
        """
        Test if the page content has been correctly updated after the edition of the page
        """
        #we create a new page
        title = 'test'
        content = "# Test\n\nCeci est le contenu de test."
        self.client.post("/savenewpage/", data={'title':title, 'content':content})

        #we then modify the content
        modified_content = "# Test\n\nModification. Ceci est le contenu de test." 
        self.client.post(f"/wiki/{title}/saveedition", data={'content':modified_content})

        #we verify that the content has been correctly updated and close the file 
        self.assertEqual(util.get_entry("test"),modified_content)
        default_storage.delete("entries/test.md")


class TestSring(TestCase):
    """
    class of test functions testing if each of the functions of markdownify correctly transform
    the markdown string in the corresponding html
    """
    def test_clean_string(self): 
        """
        test if clean_string correctly delete spaces around strings
        """
        self.assertEqual(clean_title("test"),"test")
        self.assertEqual(clean_title("test "),"test")
        self.assertEqual(clean_title(" test"),"test")
        self.assertEqual(clean_title(""),"")
        self.assertEqual(clean_title("t "),"t")
        self.assertEqual(clean_title(" t"),"t")

    def test_replace_by_h1(self):
        self.assertEqual(md.replace_by_h1('# jqhdckhcdk \n dhjhdjhjdhd'),
                                     '<h1>jqhdckhcdk </h1>\n dhjhdjhjdhd')
        self.assertEqual(md.replace_by_h1('# jqhdckhcdk \n\n# dhjhdjhjdhd\n'),
                                     '<h1>jqhdckhcdk </h1>\n\n<h1>dhjhdjhjdhd</h1>\n')


    def test_replace_by_h1h2(self):
        content = md.replace_by_h2('# jqhdckhcdk \n ## dhjhdjhjdhd\n\n')
        self.assertEqual(content, '# jqhdckhcdk \n <h2>dhjhdjhjdhd</h2>\n\n')
        self.assertEqual(md.replace_by_h1(content), '<h1>jqhdckhcdk </h1>\n <h2>dhjhdjhjdhd</h2>\n\n')

    def test_replace_by_strong_a(self):
        content = md.replace_by_a('Django is a **web framework** written using [Python](/wiki/Python) that allows ** for the design ** of web applications that generate [HTML](/wiki/HTML) dynamically.')
        content = md.replace_by_strong(content)
        self.assertEqual(content, 'Django is a <strong>web framework</strong> written using <a href="/wiki/Python">Python</a> that allows <strong> for the design </strong> of web applications that generate <a href="/wiki/HTML">HTML</a> dynamically.')
        
    def test_replace_by_ul(self): 
        content = md.replace_by_ul('HTML is a markup language that can be used to define the structure of a web page. HTML elements include\n\n* headings\n* paragraphs \n* lists\n* links\n* and more!\n\nThe most recent major version of HTML is HTML5.')
        self.assertEqual(content, 'HTML is a markup language that can be used to define the structure of a web page. HTML elements include\n\n<ul><li>headings</li>\n<li>paragraphs </li>\n<li>lists</li>\n<li>links</li>\n<li>and more!</li></ul>\n\nThe most recent major version of HTML is HTML5.')
        
    def test_replace_by_p(self):
        content = md.replace_by_p('HTML\nHTML is a markup language that can be **used** to define the structure of a web page.\n\n HTML elements include headings')
        self.assertEqual(content,'<p>HTML</p>\n<p>HTML is a markup language that can be **used** to define the structure of a web page.</p>\n\n<p> HTML elements include headings</p>')

    def test_convert(self):
        self.maxDiff = None
        content = md.convert('# Django\n\n## First part\n\nDjango is a **web framework** written using [Python](/wiki/Python).\nThat allows\n\n* for the design\n* of web applications.')
        self.assertEqual(content,'<h1>Django</h1><h2>First part</h2><p>Django is a <strong>web framework</strong> written using <a href="/wiki/Python">Python</a>.</p><p>That allows</p><ul><li>for the design</li><li>of web applications.</li></ul>')




        
