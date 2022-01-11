class artist():
    def __init__(self, artist, title, album, year):
        self.artist=artist
        self.title=title
        self.album=album
        self.year=year
        
    def __str__ (self):
        return('Performer: ' + self.artist + '\n' + 'Song: ' + self.title + '\n' + 'Album: ' + self.album + '\n' + 'Year: ' + self.year)
    
FrankOcean=artist('Frank Ocean', 'Futura Free', 'Blonde', '2016')
print(FrankOcean)
print()
JanGlin=artist('Jan Glin', 'Agony', 'Stranger', '2017')
print(JanGlin)