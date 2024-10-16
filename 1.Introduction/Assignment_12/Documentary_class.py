
from Media_class import Media

class Documentary(Media):
     def __init__(self,type,name,director,imdb_score,url,duration,part,actor ,season):
        Media.__init__(self,type,name,director,imdb_score,url,duration,actor)
        self.part = part
        self.season = season
        