from django.test import TestCase
from example.models import Movie, Genre
from example.forms import MovieForm, GenreForm


class SimpleTestCase(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name='Horror')
        self.movie = Movie.objects.create(
            name='Dracula',
            year='1987',
            released='02-11-1987',
            genre=self.genre,
        )


    def tearDown(self):
        self.movie.delete()
        self.genre.delete()


    def test_max_length(self):
        form = MovieForm(data={'name': 'X' * 200})
        self.assertFalse(form.is_valid())


    def test_initial(self):
        form = MovieForm(instance=self.movie)
        self.assertEqual(form.initial['name'], self.movie.name)
        self.assertEqual(form.initial['year'], self.movie.year)
        self.assertEqual(form.initial['released'], self.movie.released)
        self.assertEqual(form.initial['genre'], self.movie.genre.id)


    def test_year(self):
        form = MovieForm(data={'year': 'X' * 200})
        self.assertFalse(form.is_valid())

    def test_max_length_genre(self):
        form = GenreForm(data={'name': 'X' * 200})
        self.assertFalse(form.is_valid())


class SimpleTestCase2(TestCase):
    hello_world_url = reverse('hello_world')

    def test_display_view(self):
        response = self.client.get(self.hello_world_url)
        content = str(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.view_name, 'hello')
