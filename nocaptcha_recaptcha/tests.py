from django.test import TestCase


class AnimalTestCase(TestCase):
    def setUp(self):
        pass

    def test_add(self):
        self.assertEqual(1 + 1, 2)

