from django.test import TestCase
from django.contrib.auth import get_user_model


class UserAccountTests(TestCase):
    test_email = 'test@email.com'
    test_first_name = 'Lungu'
    test_last_name = 'Caria'
    test_cnp = '2487056981178'
    test_password = 'p@ssw0rd'

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            self.test_email, self.test_first_name, self.test_last_name, self.test_cnp, self.test_password
        )

        self.assertEqual(super_user.email, self.test_email)
        self.assertEqual(super_user.first_name, self.test_first_name)
        self.assertEqual(super_user.last_name, self.test_last_name)
        self.assertEqual(super_user.cnp, self.test_cnp)
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), self.test_first_name +
                         " " + self.test_last_name)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email=self.test_email,
                first_name=self.test_first_name,
                last_name=self.test_last_name,
                cnp='',
                password=self.test_password,
                is_superuser=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email=self.test_email,
                first_name=self.test_first_name,
                last_name=self.test_last_name,
                cnp=self.test_cnp,
                password=self.test_password,
                is_staff=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='',
                first_name=self.test_first_name,
                last_name=self.test_last_name,
                cnp=self.test_cnp,
                password=self.test_password,
                is_superuser=True
            )

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            self.test_email, self.test_first_name, self.test_last_name, self.test_cnp, self.test_password
        )
        self.assertEqual(user.email, self.test_email)
        self.assertEqual(user.first_name, self.test_first_name)
        self.assertEqual(user.last_name, self.test_last_name)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='',
                first_name=self.test_first_name,
                last_name=self.test_last_name,
                cnp=self.test_cnp,
                password=self.test_password
            )
