from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIClient

from users.tests.factories import AdminUserFactory, UserFactory

from ..serializers import GenreSerializer, MovieSerializer
from .factories import GenreFactory, MovieFactory


class TestGenre(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = GenreFactory()

    def test_list(self):
        """Test that Genre collection can be listed"""

        resp = self.client.get("/api/v1/core/genre/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_get(self):
        """Test that an instance of Genre can be retrieved"""

        resp = self.client.get(f"/api/v1/core/genre/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Genre"""

        resp = self.client.post("/api/v1/core/genre/")
        self.assertEqual(resp.status_code, 403)

    @patch("core.views.GenreViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Genre"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = GenreSerializer(self.instance).data

        resp = self.client.post("/api/v1/core/genre/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Genre"""

        resp = self.client.patch(f"/api/v1/core/genre/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Genre update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/core/genre/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Genre"""

        resp = self.client.delete(f"/api/v1/core/genre/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Genre deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/core/genre/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)


class TestMovie(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.admin = AdminUserFactory()
        self.instance = MovieFactory()

    def test_list(self):
        """Test that Movie collection can be listed"""

        resp = self.client.get("/api/v1/core/movie/")
        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["id"], self.instance.id)

    def test_get(self):
        """Test that an instance of Movie can be retrieved"""

        resp = self.client.get(f"/api/v1/core/movie/{self.instance.id}/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], self.instance.id)

    def test_anonymous_create_fails(self):
        """Test that anonymous users can't create a new Movie"""

        resp = self.client.post("/api/v1/core/movie/")
        self.assertEqual(resp.status_code, 403)

    @patch("core.views.MovieViewSet.get_serializer")
    def test_create(self, mock_get_serializer):
        """Test create view for Movie"""

        self.client.force_authenticate(user=self.user)
        serializer = mock_get_serializer.return_value
        serializer.is_valid.return_value = True
        serializer.data = MovieSerializer(self.instance).data

        resp = self.client.post("/api/v1/core/movie/", {})
        self.assertEqual(resp.status_code, 201)

        mock_get_serializer.assert_called_once_with(data={})
        serializer.save.assert_called_once_with()

    def test_anonymous_update_fails(self):
        """Test that anonymous users can't update an existing Movie"""

        resp = self.client.patch(f"/api/v1/core/movie/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 403)

    def test_update(self):
        """Test Movie update"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.patch(f"/api/v1/core/movie/{self.instance.id}/", {})
        self.assertEqual(resp.status_code, 200)

    def test_anonymous_delete_fails(self):
        """Test that anonymous users can't delete Movie"""

        resp = self.client.delete(f"/api/v1/core/movie/{self.instance.id}/")
        self.assertEqual(resp.status_code, 403)

    def test_delete(self):
        """Test Movie deletion"""

        self.client.force_authenticate(user=self.admin)
        resp = self.client.delete(f"/api/v1/core/movie/{self.instance.id}/")

        self.assertEqual(resp.status_code, 204)
