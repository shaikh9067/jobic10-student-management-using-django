from django.test import TestCase
from django.urls import reverse

class AttendanceUpdateViewTests(TestCase):
    def test_update_attendance_without_csrf_token(self):
        response = self.client.post(reverse('attendance_update'), {})
        self.assertEqual(response.status_code, 403)

    def test_update_attendance_with_csrf_token(self):
        response = self.client.post(reverse('attendance_update'), {}, 
                                     HTTP_X_CSRFTOKEN='dummy_token')
        self.assertNotEqual(response.status_code, 403)