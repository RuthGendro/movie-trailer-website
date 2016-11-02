import fresh_tomatoes
import media

harry_potter = media.Movie("Harry Potter",
                          "The story of a young wizard",
                           "https://c1.staticflickr.com/5/4106/4845076281_6cf62e31b4_z.jpg",
                          "https://www.youtube.com/watch?v=PbdM1db3JbY")


lord_of_the_rings = media.Movie("Lord of the Rings",
                          "A hobbit journeys to destroy the one ring",
                           "https://s-media-cache-ak0.pinimg.com/originals/da/62/15/da6215975e9cf756e5e2e0235b237264.jpg",
                          "https://www.youtube.com/watch?v=cnf4h5HT4dc")

the_hunger_games = media.Movie("The Hunger Games",
                          "A hobbit journeys to destroy the one ring",
                         "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                          "https://www.youtube.com/watch?v=mfmrPu43DF8")

deadpool = media.Movie("Deadpool",
                          "A hobbit journeys to destroy the one ring",
                           "https://c2.staticflickr.com/2/1713/25001141921_5826f003c9_b.jpg",
                          "https://www.youtube.com/watch?v=9vN6DHB6bJc")

movies = [harry_potter, lord_of_the_rings, the_hunger_games, deadpool]

fresh_tomatoes.open_movies_page(movies)
