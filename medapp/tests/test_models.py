from django.test import TestCase

from users.models import User


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='Bob_Michaels',
                            email='bobmichaels@gmail.com', password='testing321')

    def test_real_name_label(self):
        user = User.objects.get(id=1)
        self.assertEquals(user.password, 'testing321')
