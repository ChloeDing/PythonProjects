import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://www.google.ca/search?q=toy+story&newwindow=1&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjE873n9ZXdAhWRoFsKHcBCAh4Q_AUICigB&biw=1581&bih=790#imgrc=P-Dlqkg6wu5RnM:",
                        "https://www.youtube.com/watch?v=tN1A2mVnrOM")


#print(toy_story.storyline)

#toy_story.show_trailer()

island = media.Movie("Island",
                     "A cataclysmic event causes a man, who dreams of winning the lottery, to become stranded on an island with his co-workers.",
                     "http://www.goldposter.com/zh/273490/",
                     "https://www.youtube.com/watch?v=0xSl0Dsmw_0")

#island.show_trailer()

movies = [toy_story, island]

#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)

print(media.Movie.__name__)

print(media.Movie.__module__)
