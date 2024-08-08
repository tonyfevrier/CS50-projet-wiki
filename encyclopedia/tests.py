from django.test import TestCase
from django.core.files.storage import default_storage

class TestEntriesUpdating(TestCase):

    def test_newpage_creation(self):
        """
        Test that the page is registered after its creation with the correct content.
        """
        #we create a new page
        title = 'testing'
        content = "Ceci est le contenu de test."
        self.client.post("/savenewpage/",data={'title':title, 'content':content})

        #we verify the creation of the file and the associated content 
        _,filenames = default_storage.listdir('entries') 
        self.assertIn("testing.md",filenames)
        file = default_storage.open("entries/testing.md")
        self.assertEqual(file.read().decode("utf-8"), content)

        #we close and clean the data
        file.close()
        default_storage.delete("entries/testing.md")
        

    def test_editpage(self):
        """
        Test if the page content has been correctly updated after the edition of the page
        """
        #we create a new page
        title = 'test'
        content = "Ceci est le contenu de test."
        self.client.post("/savenewpage/", data={'title':title, 'content':content})

        #we then modify the content
        modified_content = "#Modification. Ceci est le contenu de test."
        self.client.post(f"/wiki/{title}/saveedition", data={'content':modified_content})

        #we verify that the content has been correctly updated and close the file
        file = default_storage.open("entries/test.md")
        self.assertEqual(file.read().decode("utf-8"), modified_content)
        file.close()
        default_storage.delete("entries/test.md")
 


        
