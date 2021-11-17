import datetime

class Book:
	items = []

	def __init__(self, title, published, author):
		self.title = title
		self.author = author
		self.published = published
		Book.items.append(self)

	def __str__(self):
		return f'{self.author}\'s {self.title}'

	def __repr__(self):
		return f'{self.author}\'s {self.title}'
		
	def __eq__(self, other):
		return self.author == other.author and self.title == other.title
		
	def __hash__(self):
		return hash((self.title, self.author))	

	@classmethod
	def find_by_title(cls, title):
		find_books = []
		for item in cls.items:
			if title.lower() == item.title.lower():
				find_books.append(item)
		return find_books

	@classmethod
	def find_by_author(cls, author):
		find_books = []
		for item in cls.items:
			if author.lower() in item.author.lower():
				find_books.append(item)
		return find_books

	@classmethod
	def published_after(cls, year):
		find_books = []
		for item in cls.items:
			if item.published.year > year:
				find_books.append(item)
		return find_books


class Movie:
	items = []

	def __init__(self, name, release_day, directed_by, based_on):
		self.name = name
		self.release_day = release_day
		self.directed_by = directed_by
		self.based_on = based_on
		Movie.items.append(self)

	def __str__(self):
		return f'{self.directed_by}\'s {self.name}'

	def __repr__(self):
		return f'{self.directed_by}\'s {self.name} {self.release_day}'

	@classmethod
	def sort_items(cls):
		sorted_movies = cls.items
		swapped = True
		while swapped:
			swapped = False
			for i in range(len(sorted_movies)-1):
				if sorted_movies[i].release_day > sorted_movies[i+1].release_day:
					sorted_movies[i], sorted_movies[i+1] = sorted_movies[i+1], sorted_movies[i]
					swapped = True
		return sorted_movies

	@classmethod
	def for_book(cls, book_title):
		find_book = []
		for item in cls.items:
			if book_title in item.based_on.title:
				find_book.append(item.based_on)
		return find_book

	def recommendations(self):
		recommendations_movies = []
		for item in Movie.items:
			if self.name in item.name or self.directed_by in item.directed_by or self.based_on.title in item.based_on.title or self.based_on.title in item.name or self.name in item.based_on.title:
				if self.name in item.name and self.directed_by in item.directed_by and self.based_on.title and item.based_on.title:
					continue
				else: 
					recommendations_movies.append(item)
		return recommendations_movies

first_book = Book('Dune', datetime.date(1965, 8, 1), 'Frank Herbert')
first_movie = Movie('Dune', datetime.date(2021, 9, 3), 'Denis Villeneuve', first_book)
second_book = Book('The Lord of the Rings', datetime.date(1954, 7, 29), 'J. R. R. Tolkien')
second_movie = Movie('The Lord of the Rings', datetime.date(2001, 12, 10), 'Peter Jackson', second_book)
third_movie = Movie('Dune', datetime.date(1984, 12, 3), 'Raffaella De Laurentiis', first_book)
print(Movie.items)
print(third_movie.recommendations())

'''

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

'''
