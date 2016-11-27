import media
import fresh_tomatoes

toystory = media.Movie("Toy Story","Story of a toy that is alive", "http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toystory.storyline)

avatar = media.Movie("Avatar","Marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#avatar.show_trailer()

themartian = media.Movie("The Martian","Sci fi movie", "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg", "https://www.youtube.com/watch?v=Ue4PCI0NamI")
#themartian.show_trailer()

movies = [toystory, avatar, themartian]
#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
