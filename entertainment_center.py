import fresh_tomatoes
import movies

# begin movie info
toy_story_3 = movies.Movie("Toy Story 3",
                        "The toys are mistakenly delivered to a day-care center"
                        " instead of the attic right before Andy leaves for"
                        " college, and it's up to Woody to convince the other"
                        " toys that they weren't abandoned and to return home.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SY1000_CR0,0,707,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4")

sandlot = movies.Movie("The Sandlot",
                       "A new kid in town is taken under the wing of a young"
                       " baseball prodigy and his team in this coming of age"
                       " movie set in the summer of 1962. Together, they get"
                       " themselves into many adventures involving rival teams,"
                       " lifeguards, and a vicious dog.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgyODA5MzQ1MF5BMl5BanBnXkFtZTgwMzYxNzYxMTE@._V1_.jpg",
                       "https://www.youtube.com/watch?v=ec9W8JbFykw")

prisoner_of_azkaban = movies.Movie("Harry Potter and the Prisoner of Azkaban",
                                   "It's Harry's third year at Hogwarts; not"
                                   " only does he have a new Defense Against the"
                                   " Dark Arts teacher, but there is also"
                                   " trouble brewing. Convicted murderer"
                                   " Sirius Black has escaped the Wizards'"
                                   " Prison and is coming after Harry.",
                                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY4NTIwODg0N15BMl5BanBnXkFtZTcwOTc0MjEzMw@@._V1_SY1000_CR0,0,676,1000_AL_.jpg",
                                   "https://www.youtube.com/watch?v=lAxgztbYDbs")


shawshank_redemption = movies.Movie("The Shawshank Redemption",
                                    "Two imprisoned men bond over a number of"
                                    " years, finding solace and eventual"
                                    " redemption through acts of common"
                                    " decency.",
                                    "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
                                    "https://www.youtube.com/watch?v=6hB3S9bIaco"
                                    )


blade_runner = movies.Movie("Blade Runner",
                            "A blade runner must pursue and try to"
                            " terminate four replicants who stole a"
                            " ship in space and have returned to Earth"
                            " to find their creator.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BZWZlYmEyYTItNGRjYy00ZmMxLWEzMWItM2Q2NjZlNTMwMjQ3XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=eogpIG53Cis")

# end movie info

# create movie list array
movie_list = [toy_story_3, sandlot, prisoner_of_azkaban, shawshank_redemption, blade_runner]

# create page using fresh_tomatoes.py using movie_list
fresh_tomatoes.open_movies_page(movie_list)
