class Musica:
    def __init__(self, titulo, artista, album):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album


    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def artista(self):
        return self.__artista
    
    @property
    def album(self):
        return self.__album
    
class CtrlMusica():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaMusicas = []
        
    def getListaMusicas(self):
        return self.listaMusicas
    
    def getMusica(self, musicaBuscada):
        musicaRet = None
        for musica in self.listaMusicas:
            if musica.titulo == musicaBuscada:
                musicaRet = musica
        return musicaRet
    
    def addMusica(self, titulo, artista, album):
        musica = Musica(titulo,artista,album)
        self.listaMusicas.append(musica)