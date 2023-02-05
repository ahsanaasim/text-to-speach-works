from GSpeaker import GSpeaker
from MovieMaker import MovieMaker

ayah = "Who is an enemy to Allah, and His angels and His messengers, and Gabriel and Michael! Then, lo! Allah (Himself) is an enemy to the disbelievers."

speaker = GSpeaker(ayah)
speaker.speak()

movie = MovieMaker()
movie.generate(ayah)
