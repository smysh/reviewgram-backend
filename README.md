# ReviewGram - backend
Repo for backend of reviewgram - a full stack webAPI for finding reviews and ratings of TV shows and movies, and keep your own watchlists

 
## Feature Set

We connected our back-end to TMDB API which gave us all the tvshows and movie information. For the front-end to work we created the following endpoints:

 - User Routes
	 - CRUD routes for user
	 - Get reviews from user
	 - Add review to Media
	 - Add to user watchlist
	 - Add to user watched list
	 - Get user watchlist
	 - Get user watched list
	 
 - Media Routes
	 - Get Img url (TMDB api requires to look up for the images in different serves regularly)
	 - Search media
	 - Get trending tv shows
	 - Get trending movies
	 - Get movie details
	 - Get show details
	 - Get reviews for tv show
	 - Get reviews for movie
	 - 
 - Authorization Routes
	 - Get authorization Token

## Technology used
This back-end has been entirely programmed in ***Python***, using ***flask*** and ***SQLAlchemy***. The database used is ***Postgres***.
