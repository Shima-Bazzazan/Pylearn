
from Media_class import Media

class Film(Media):
    def __init__(self,type,name,director,Imdb_score,url,duration,actor):
        Media.__init__(self,type,name,director,Imdb_score,url,duration,actor)