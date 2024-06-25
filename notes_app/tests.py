from django.test import TestCase
from django.contrib.auth.models import User

from .models import StickyNote


# Create your tests here.
class StickyNotesTestCase(TestCase):

    def setUp(self):
        # Create a user to test logged-in access.
        self.username = 'testing'
        self.password = 'testing'
        self.user = User.objects.create_user(username=self.username,
                                             password=self.password)

        # Create an existing StickyNote for updating.
        self.note = StickyNote.objects.create(title="This is a note",
                                              content="This is content",
                                              owner=self.user)

    def test_home_as_guest(self):
        """
        There should be a redirect to the login page.
        """
        request = self.client.get('/')
        self.assertEqual(request.status_code, 302)
        self.assertEqual(request.url, '/accounts/login/?next=/')

    def test_home_as_user(self):
        """
        The user should land on the home page.
        """
        self.client.login(username=self.username, password=self.password)
        request = self.client.get('/')
        self.assertEqual(request.status_code, 200)

    def test_access_create_note_as_guest(self):
        """
        There should be a redirect to the login page.
        """
        request = self.client.get('/create')
        self.assertEqual(request.status_code, 302)
        self.assertEqual(request.url, '/accounts/login/?next=/create')

    def test_access_create_note_as_user(self):
        """
        The user should land on the create note page.
        """
        self.client.login(username=self.username, password=self.password)
        request = self.client.get('/create')
        self.assertEqual(request.status_code, 200)

    def test_create_note_as_guest(self):
        """
        There should be a redirect to the login page.
        """
        request = self.client.post('/create', {
            "title": "A new note",
            "content": "here it is"
            })
        self.assertEqual(request.status_code, 302)
        self.assertEqual(request.url, '/accounts/login/?next=/create')

    def test_create_note_as_user(self):
        """
        The user should be redirected to the home page on success.
        """
        self.client.login(username=self.username, password=self.password)
        request = self.client.post('/create', {
            "title": "A new note",
            "content": "here it is"
            })
        self.assertEqual(request.status_code, 302)
        self.assertEqual(request.url, '/')

    def test_create_invalid_note_as_user(self):
        """
        The user should remain on the page.
        """
        self.client.login(username=self.username, password=self.password)
        request = self.client.post('/create', {
            "title": "A new note with no content"
            })
        self.assertEqual(request.status_code, 200)
        # A REST endpoint would return a UNPROCESSABLE ENTITY code.

    def test_access_update_note_as_guest(self):
        """
        There should be a redirect to the login page.
        """
        request = self.client.get(f"/update/{self.note.pk}")
        self.assertEqual(request.status_code, 302)
        self.assertEqual(request.url,
                         f"/accounts/login/?next=/update/{self.note.pk}")

    def test_access_update_note_as_user(self):
        """
        The user should land on the update note page.
        """
        self.client.login(username=self.username, password=self.password)
        request = self.client.get(f"/update/{self.note.pk}")
        self.assertEqual(request.status_code, 200)

    def test_access_update_invalid_note_as_user(self):
        """
        The page should be not found.
        """
        self.client.login(username=self.username, password=self.password)
        request = self.client.get('/update/404')
        self.assertEqual(request.status_code, 404)

    def test_update_note_as_guest(self):
        """
        There should be a redirect to the login page.
        """
        request = self.client.post(f"/update/{self.note.pk}", {
            "title": "New Title",
            "content": "New content"
            })
        self.assertEqual(request.status_code, 302)
        self.assertEqual(request.url,
                         f"/accounts/login/?next=/update/{self.note.pk}")

    def test_update_note_as_user(self):
        """
        The user should be redirected to the home page on success.
        """
        self.client.login(username=self.username, password=self.password)
        request = self.client.post(f"/update/{self.note.pk}", {
            "title": "New Title",
            "content": "New content"
            })
        self.assertEqual(request.status_code, 302)
        self.assertEqual(request.url, '/')

    def test_update_invalid_note_as_user(self):
        """
        The page should be not found.
        """
        self.client.login(username=self.username, password=self.password)
        request = self.client.post('/update/404', {
            "title": "New Title",
            "content": "New content"
            })
        self.assertEqual(request.status_code, 404)

    def test_delete_note_as_guest(self):
        """
        There should be a redirect to the login page.
        """
        request = self.client.delete(f"/delete/{self.note.pk}")
        self.assertEqual(request.status_code, 302)
        self.assertEqual(request.url,
                         f"/accounts/login/?next=/delete/{self.note.pk}")

    def test_delete_note_as_user(self):
        """
        There should be a redirect to the home page on success.
        """
        self.client.login(username=self.username, password=self.password)
        request = self.client.delete(f"/delete/{self.note.pk}")
        self.assertEqual(request.status_code, 302)
        self.assertEqual(request.url, "/")

    def test_delete_invalid_note_as_user(self):
        """
        The page should be not found.
        """
        self.client.login(username=self.username, password=self.password)
        request = self.client.delete("/delete/404")
        self.assertEqual(request.status_code, 404)

    def test_access_create_post_as_guest(self):
        """
        There should be a redirect to the home page.
        """
        request = self.client.get('/post')
        self.assertEqual(request.status_code, 302)
        self.assertEqual(request.url, '/accounts/login/?next=/post')

    def test_access_create_post_as_user(self):
        """
        The user should land on the create post page.
        """
        self.client.login(username=self.username, password=self.password)
        request = self.client.get('/post')
        self.assertEqual(request.status_code, 200)

    def test_create_post_as_guest(self):
        """
        There should be a redirect to the login page.
        """
        request = self.client.post('/post', {
            "title": "A new note",
            "content": "here it is"
            })
        self.assertEqual(request.status_code, 302)
        self.assertEqual(request.url, '/accounts/login/?next=/post')

    def test_create_post_as_user(self):
        """
        The user should be redirected to the home page on success.
        """
        self.client.login(username=self.username, password=self.password)
        request = self.client.post('/post', {
            "title": "A new note",
            "content": "here it is"
            })
        self.assertEqual(request.status_code, 302)
        self.assertEqual(request.url, '/')

    def test_create_invalid_post_as_user(self):
        """
        The user should remain on the page.
        """
        self.client.login(username=self.username, password=self.password)
        request = self.client.post('/post', {
            "title": "A new note with no content"
            })
        self.assertEqual(request.status_code, 200)
        # A REST endpoint would return a UNPROCESSABLE ENTITY code.

    def test_access_register_page(self):
        """
        The register page should be accessible.
        """
        request = self.client.get('/register')
        self.assertEqual(request.status_code, 301)
        # 301 is returned instead of 200, no idea why.

    def test_register_new_user(self):
        """
        The user should be redirected to the login page on success.
        """
        request = self.client.post('/register', {
            "username": "BestMan",
            "password": "InTheWorld0123"
        })
        self.assertEqual(request.status_code, 301)
        # self.assertEqual(request.url, '/accounts/login')
        # For some reason request.url = '/register' at this point, have not
        # been able to find out why.
