from django.contrib.auth import get_user_model
from django.test import TestCase


class AccountsManagersTests(TestCase):
    def test_create_account(self):
        account_model = get_user_model()
        account = account_model.objects.create_user(
            email="user@user.com", password="password"
        )
        self.assertEqual(account.email, "user@user.com")
        self.assertTrue(account.is_active)
        self.assertFalse(account.is_superuser)
        self.assertFalse(account.is_staff)
        with self.assertRaises(TypeError):
            account_model.objects.create_user()
        with self.assertRaises(ValueError):
            account_model.objects.create_user(email="")
        with self.assertRaises(ValueError):
            account_model.objects.create_user(email="", password="password")

    def test_create_superuser_account(self):
        account_model = get_user_model()
        superuser_account = account_model.objects.create_superuser(
            email="superuser@user.com", password="password"
        )
        self.assertEqual(superuser_account.email, "superuser@user.com")
        self.assertTrue(superuser_account.is_active)
        self.assertTrue(superuser_account.is_superuser)
        self.assertTrue(superuser_account.is_staff)
        with self.assertRaises(ValueError):
            account_model.objects.create_superuser(
                email="superuser1@user.com", password="password", is_superuser=False
            )
        with self.assertRaises(ValueError):
            account_model.objects.create_superuser(
                email="superuser2@user.com", password="password", is_staff=False
            )
