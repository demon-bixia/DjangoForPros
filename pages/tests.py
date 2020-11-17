from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutView

class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    # test if home page view exits
    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    # check that view uses the correct template
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
    
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')
    
    def test_homepage_dose_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page')
    
    # check if path resolves to view function
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    # test if home page view exits
    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    # check that view uses the correct template
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
    
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')
    
    def test_homepage_dose_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page')
    
    # check if path resolves to view function
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutView.as_view().__name__
        )
