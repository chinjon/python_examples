import ex40_my_stuff

class Song(object):
  
  def _init_(self, lyrics):
    self.lyrics = lyrics
    
  def sing_me_a_song(self):
    for line in self.lyrics:
      print(line)

thing = ex40_my_stuff.MyStuff()

ex40_my_stuff.apple()
print(ex40_my_stuff.tangerine)

thing.apple()

happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])

happy_bday.sing_me_a_song()
