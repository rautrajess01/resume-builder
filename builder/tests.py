from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Resume

# Create your tests here.

class ResumeViewCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_resume_list_requires_login(self):
        response = self.client.get(reverse('resume_list'))
        self.assertEqual(response.status_code, 302)

    def test_create_resume(self):
        self.client.login(username='testuser', password='12345')
        data = {
            'full_name': 'Rajesh Raut',
            'email': 'test@gmail.com',
            'phone': '98623638888',
            'skills': 'Python',
            'education': 'Bachelor',
            'projects': 'Resume Builder'

        }
        response = self.client.post(reverse('create_resume'), data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Resume.objects.count(), 1)

        resume = Resume.objects.first()
        self.assertEqual(resume.user, self.user)

    def test_preview_resume(self):
        self.client.login(username='testuser', password='12345')
        resume = Resume.objects.create(user=self.user, email='test@gmail.com', phone='981382374827', skills='python', education='bachelor', projects='Resumue builder')
        response = self.client.get(reverse('preview_resume', args=[resume.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'builder/preview.html')




