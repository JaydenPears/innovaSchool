class Film:
    def __init__(self, name: str, genre: str, duration: int, rating: int, age_rating: int):
        self.name = name
        self.genre = genre
        self.duration = duration
        self.rating = rating
        self.age_rating = age_rating

    def get_info(self) -> tuple:
        return self.name, self.genre, self.duration, self.rating, self.age_rating


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def movie_info(film: Film) -> str:
        name, genre, duration, rating, age_rating = film.get_info()
        return f"Name: {name} | Genre: {genre} | Duration: {duration} minutes | Rating: {rating}/10 | Age rating: {age_rating} y. o."

    def buy_film(self, films: list) -> Film | None:
        pass