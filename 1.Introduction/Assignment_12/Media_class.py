
import pytube

class Media:
    
    def __init__(self,type,name,director,imdb_score,url,duration,actor):
        self.type = type
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.actor = actor

    def show_info(self):
        if self.type=="film":
            print("Type: ",self.type , "|\tName: " , self.name ,"|\tDirector: ",self.director,"|\tScore: ",self.imdb_score,"|\tUrl: ",self.url,"|\tDuration: ",self.duration,"|\tactors: ",self.actor,"\n")
        
        elif self.type=="serial":
            print("Type: ",self.type , "|\tName: " , self.name ,"|\tDirector: ",self.director,"|\tScore: ",self.imdb_score,"|\tUrl: ",self.url,"|\tDuration: ",self.duration,"|\tPart: ",self.part,"|\tactors: ",self.actor,"|\tSeason: ",self.season,"\n")

        elif self.type=="clip":
            print("Type: ",self.type , "|\tName: " , self.name ,"|\tDirector: ",self.director,"|\tScore: ",self.imdb_score,"|\tUrl: ",self.url,"|\tDuration: ",self.duration,"|\tactors: ",self.actor,"\n")

        elif self.type=="documentary":
            print("Type: ",self.type , "|\tName: " , self.name ,"|\tDirector: ",self.director,"|\tScore: ",self.imdb_score,"|\tUrl: ",self.url,"|\tDuration: ",self.duration,"|\tPart: ",self.part,"|\tactors: ",self.actor,"|\tSeason: ",self.season,"\n")

        


    def download(self):
        link = self.url
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename='test.mp4')


            