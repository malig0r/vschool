# from django.test import TestCase
# import pytest
# from rest_framework.test import APIClient

# client = APIClient()

# pytestmark = pytest.mark.django_db
# class LoginTestCase(TestCase):
#     response = client.post('/api/users/login/', 
#                            {"username": "igorm",
#                             "password": "123"}, 
#                            format='json')
#     assert response.status_code == 202
#     assert bool(response.COOKIES.get('csrftoken')) == True