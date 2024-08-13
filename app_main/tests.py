from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Test class for CustomLoginView
class CustomLoginViewTests(TestCase):
    def setUp(self):
        """
        Set up a test environment before each test runs.
        - Create a user for authentication testing.
        - Define the URL for the login view.
        """
        self.user = get_user_model().objects.create_user(username='testuser', password='password123')
        self.login_url = reverse('login')

    def test_login_redirects_authenticated_user(self):
        """
        Test that an authenticated user is redirected from the login page to the 'tasks' page.
        """
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.login_url)
        self.assertRedirects(response, reverse('tasks'))
        
        """
        Test that the login view renders the correct template for anonymous users.
        """
    def test_login_view_renders_for_anonymous_user(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_main/login.html')

        """
        Test that a user can log in successfully and is redirected to the 'tasks' page.
        """
    def test_user_login_success(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'password123'})
        self.assertRedirects(response, reverse('tasks'))