
from Media_class import Media

class Clip(Media):
   def __init__(self, type, name, director, imdb_score, url, duration,actor):
       Media.__init__(self,type, name, director, imdb_score, url, duration,actor)