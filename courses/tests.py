from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Course

User = get_user_model()

class CourseModelTest(TestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(
            username='teacher1',
            password='testpass123',
            role='teacher'
        )

    def test_create_course(self):
        course = Course.objects.create(
            title='Математика',
            description='Уроки по математике.',
            teacher=self.teacher
        )
        self.assertEqual(course.title, 'Математика')
        self.assertEqual(course.teacher.username, 'teacher1')
