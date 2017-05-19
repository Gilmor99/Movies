import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Toys Come to Life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print toy_story.storyline

avatar = media.Movie("Avatar",
                    "A marine on alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=a0CDJZu4M5I")

#print avatar.storyline
#avatar.show_trailer()
school_of_rock = media.Movie("School Of Rock",
                            "storyline",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                            "https://youtu.be/3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille", "Storyline",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg",
                            "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris", "Storyline",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/220px-Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=-NoGpkSTK8k")
hunger_games = media.Movie("Hunger Games", "Storyline",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg",
                            "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
#fresh_tomatoes.open_movies_page(movies)

print media.Movie.__name__
print media.Movie.__module__
