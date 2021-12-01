from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from API.models import Todo

USER = get_user_model()



class AccountTests(APITestCase):

    def setUp(self) -> None:
        self.url = reverse('todo-list')
        self.data = {'description': 'NEW TODO', 'completed': 'NOTDONE'}
        self.user_data = {'username': 'admin', 'password': 'adminadmin'}
        self.user = USER.objects.create_user(**self.user_data)
        self.client = APIClient()
        return super().setUp()

    def test_create_todo(self):
        self.client.login(**self.user_data)
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.get().completed, 'NOTDONE')

    
    def test_get_todo(self):
        self.client.login(**self.user_data)
        self.create_todo()
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_delete_todo(self):
        self.client.login(**self.user_data)
        todo = self.create_todo()
        id = todo.data['id']
        url = reverse('todo-detail', kwargs={'pk': id}) 
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    
    def create_todo(self):
        response = self.client.post(self.url, self.data, format='json')
        return response

