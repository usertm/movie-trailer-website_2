import media  # Stores Movie class
import fresh_tomatoes  # Contains web-page generator

# A list of favorite movies is below.
# Each movie has Title, Storyline, url of poster image, url of the trailer.
toy_story = media.Movie(
	"Toy Story", 
	"1995", 
	"A story of a boy and his toys that come to live",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
	"Avatar", 
	"2009",  
	"A marine on alien planet", 
	"http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
	"https://www.youtube.com/watch?v=cRdxXPV9GNQ")

secretary = media.Movie(
	"Secretary",
	"2002", 
	"A romantic story of a dominant boss and his secretary", 
	"http://upload.wikimedia.org/wikipedia/en/b/b9/Secretarymovpost.jpg", 
	"https://www.youtube.com/watch?v=YmSO07r_zTc")

artist = media.Movie(
	"The Artist", 
	"2011", 
	"A story of an artist", 
	"http://upload.wikimedia.org/wikipedia/en/f/f3/The-Artist-poster.png", 
	"http://www.youtube.com/watch?v=O8K9AZcSQJE")

life_of_brian=media.Movie(
	"Life of Brian",
	"1979", 
	"A story of young jewish boy", 
	"http://upload.wikimedia.org/wikipedia/en/1/18/Lifeofbrianfilmposter.jpg", 
	"https://www.youtube.com/watch?v=u5MVPM7dZlI")

annie_hall= media.Movie(
	"Annie Hall", 
	"1977", 
	"A love story in NY", 
	"http://upload.wikimedia.org/wikipedia/en/e/e6/Anniehallposter.jpg", 
	"http://upload.wikimedia.org/wikipedia/en/e/e6/Anniehallposter.jpg" )


# A list of movies for web-page generator
movies = [toy_story, avatar, secretary, artist, life_of_brian, annie_hall]

# Creates fresh_tomatoes.html web-page and tries to open it in default webbrowser
fresh_tomatoes.open_movies_page(movies)


