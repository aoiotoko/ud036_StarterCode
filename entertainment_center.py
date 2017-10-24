import fresh_tomatoes
import media

''' This application generates a website with movie info according to the '''
''' data in each of the object instances '''

# Akira: movie title, storyline, poster image and movie trailer
akira = media.Movie(
    "Akira",
    "Akira tells the story of Shōtarō Kaneda, a leader of a local biker gang"
    " whose childhood friend, Tetsuo Shima, acquires incredible powers after
    " a motorcycle accident, eventually threatening the entire military"
    " complex amidst chaos and rebellion in the sprawling futuristic"
    " metropolis of Neo-Tokyo",
    "https://upload.wikimedia.org/wikipedia/en/5/5d/AKIRA_%281988_poster%29.jpg",  # NOQA
    "https://www.youtube.com/watch?v=FtPhrCTjMtQ"
    )

# My Neighbor Totoro: movie title, storyline, poster image and movie trailer
my_neighbor_totoro = media.Movie(
    "My Neighbor Totoro",
    "This acclaimed animated tale by director Hayao Miyazaki follows"
    " schoolgirl Satsuke (Dakota Fanning) and her younger sister, Mei (Elle"
    " Fanning), as they settle into an old country house with their father"
    " (Tim Daly) and wait for their mother (Lea Salonga) to recover from an"
    " illness in an area hospital. As the sisters explore their new home,
    " they encounter and befriend playful spirits in their house and the"
    " nearby forest, most notably the massive cuddly creature known as"
    " Totoro.",
    "https://d32qys9a6wm9no.cloudfront.net/images/movies/poster/dc/dc2208f9bbd11486d5dbbb9218e03017_500x735.jpg?t=1499831918",  # NOQA
    "https://www.youtube.com/watch?v=92a7Hj0ijLs"
    )

# The Matrix: movie title, storyline, poster image and movie trailer
the_matrix = media.Movie(
    "The Matrix",
    "Neo (Keanu Reeves) believes that Morpheus (Laurence Fishburne), an"
    " elusive figure considered to be the most dangerous man alive, can"
    " answer his question -- What is the Matrix? Neo is contacted by Trinity"
    " (Carrie-Anne Moss), a beautiful stranger who leads him into an"
    " underworld where he meets Morpheus. They fight a brutal battle for"
    " their lives against a cadre of viciously intelligent secret agents. It"
    " is a truth that could cost Neo something more precious than his life.",
    "https://i.pinimg.com/736x/a4/50/8f/a4508fea5edd41f3c311aab1e82b0ed1--top-movies-the-matrix.jpg",  # NOQA
    "https://www.youtube.com/watch?v=vKQi3bBA1y8"
    )

# Lord of the Rings: movie title, storyline, poster image and movie trailer
lord_of_the_rings = media.Movie(
    "The Lord of the Rings",
    "The future of civilization rests in the fate of the One Ring, which has"
    " been lost for centuries. Powerful forces are unrelenting in their"
    " search for it. But fate has placed it in the hands of a young Hobbit"
    " named Frodo Baggins (Elijah Wood), who inherits the Ring and steps into"
    " legend. A daunting task lies ahead for Frodo when he becomes the"
    " Ringbearer - to destroy the One Ring in the fires of Mount Doom where"
    "it was forged.",
    "https://www.movieposter.com/posters/archive/main/105/MPW-52979",
    "https://www.youtube.com/watch?v=V75dMMIW2B4"
    )

# Gantz 0: movie title, storyline, poster image and movie trailer
gantz_0 = media.Movie(
    "Gantz: 0",
    "While fighting invading monsters, Kei Kurono rescues his friend, Reika."
    " Though she protests, he attacks the monsters' leader, dying after"
    " killing it. Reika and her surviving teammates are teleported back to"
    " their base. Elsewhere, Masaru Kato dies attempting to save someone from"
    " a knife attack in a subway. He wakes up in a room with Reika and her"
    " teammates: Yoshikazu Suzuki, an old man; Joichiro Nishi, a surly"
    " teenager; and an angry, unidentified man. Suzuki explains that they"
    " have each died and woken in the room, and have been forced to fight"
    "against waves of monsters ever since. Before Suzuki can explain further,"
    " a black orb identified as 'Gantz' announces that their next mission is"
    " about to  begin. The angry man refuses to participate and is killed by"
    " Nishi, who reasons that he would have been a liability.",
    "http://pm1.narvii.com/6289/a8e840f42c5bf0e5350aafded30ce12ad1ced398_hq.jpg",  # NOQA
    "https://www.youtube.com/watch?v=r37ARGRJC-k"
    )

# Pacific Rim: movie title, storyline, poster image and movie trailer
pacific_rim = media.Movie(
    "Pacific Rim",
    "Long ago, legions of monstrous creatures called Kaiju arose from the"
    " sea, bringing with them all-consuming war. To fight the Kaiju, mankind"
    " developed giant robots called Jaegers, designed to be piloted by two"
    " humans locked together in a neural bridge. However, even the Jaegers
    " are not enough to defeat the Kaiju, and humanity is on the verge of"
    " defeat. Mankind's last hope now lies with a washed-up ex-pilot (Charlie"
    " Hunnam), an untested trainee (Rinko Kikuchi) and an old, obsolete"
    " Jaeger.",
    "https://vignette1.wikia.nocookie.net/pacificrim/images/f/f6/Pacific_rim_poster.jpeg/revision/latest?cb=20140207013732",  # NOQA
    "https://www.youtube.com/watch?v=5guMumPFBag"
    )

# Set list of movies that will be passed to the media file
movies = [
        akira,
        my_neighbor_totoro,
        the_matrix,
        lord_of_the_rings,
        gantz_0,
        pacific_rim
	]

# Open/Create the HTML file in a webbrowser through the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
