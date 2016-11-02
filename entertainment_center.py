import media

harry_potter = media.Movie("Harry Potter",
                          "The story of a young wizard",
                           "https://en.wikipedia.org/wiki/Harry_Potter#/media/File:Harry_Potter_wordmark.svg",
                          "https://www.youtube.com/watch?v=PbdM1db3JbY")
print(harry_potter.storyline)
harry_potter.show_trailer()