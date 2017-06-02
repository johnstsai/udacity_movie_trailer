import media
import fresh_tomatoes

'''attributes for movie get out'''
get_out = media.Movie(
    "Get Out",
    "A young African-American man visits his Caucasian"
    "girlfriend's mysterious family estate.",
    "https://images-na.ssl-images-amazon.com/images/M/M"
    "V5BNTE2Nzg1NjkzNV5BMl5BanBnXkFtZTgwOTgyODMyMTI@._V1"
    "_SY1000_CR0,0,631,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=DzfpyUB60YY")

'''attributes for movie jane doe'''
jane_doe = media.Movie(
    "The Autopsy of Jane Doe",
    "A father and son, both coroners, are pulled into "
    "a complex mystery while attempting to identify the "
    "body of a young woman, who was apparently harboring "
    "dark secrets.",
    "https://images-na.ssl-images-amazon.com/images/M/MV"
    "5BMjA2MTEzMzkzM15BMl5BanBnXkFtZTgwMjM2MTM5MDI@._V1_SY"
    "1000_CR0,0,674,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=mtTAhXuiRTc")

'''attributes for movie fantastic beast'''
fantastic_beast = media.Movie(
    "Fantastic Beasts and Where to Find Them",
    "The adventures of writer Newt Scamander in New "
    "York's secret community of witches and wizards "
    "seventy years before Harry Potter reads his "
    "book in school.",
    "https://images-na.ssl-images-amazon.com/images/"
    "M/MV5BMjMxOTM1OTI4MV5BMl5BanBnXkFtZTgwODE5OTYxM"
    "DI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=ViuDsy7yb8M")

'''attributes for movie pirate 2017'''
pirates_carib = media.Movie(
    "Pirates of the Caribbean: Dead Men Tell No Tales",
    "Captain Jack Sparrow searches for the trident of "
    "Poseidon.",
    "https://images-na.ssl-images-amazon.com/images/M/"
    "MV5BMTYyMTcxNzc5M15BMl5BanBnXkFtZTgwOTg2ODE2MTI@._"
    "V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=XibzC-e_s5M")

'''attributes for movie la la land'''
lala_land = media.Movie(
    "La La Land",
    "A jazz pianist falls for an aspiring actress in Los "
    "Angeles.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BM"
    "zUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_SY1000_S"
    "X675_AL_.jpg",
    "https://www.youtube.com/watch?v=0pdqf4P9MB8")

'''attributes for movie gifted'''
gifted = media.Movie(
    "Gifted",
    "Frank, a single man raising his child prodigy niece Mary, "
    "is drawn into a custody battle with his mother.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ2ND"
    "U3NDE0M15BMl5BanBnXkFtZTgwMjA3OTg0MDI@._V1_SY1000_CR0,0,675,"
    "1000_AL_.jpg",
    "https://www.youtube.com/watch?v=tI01wBXGHUs")

'''movie list'''
movies = [get_out, jane_doe, fantastic_beast, pirates_carib, lala_land, gifted]
'''create website through functions in fresh tomatoes.py'''
fresh_tomatoes.open_movies_page(movies)
