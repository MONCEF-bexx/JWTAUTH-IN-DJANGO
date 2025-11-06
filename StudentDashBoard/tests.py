from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class StudentDashboardAuthTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='amine', password='khouyalkbir')

    def test_login_with_correct_credentials(self):
        logged_in = self.client.login(username='amine', password='khouyalkbir')
        self.assertTrue(logged_in)