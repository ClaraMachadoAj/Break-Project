from firstapp.models import Musica
from firstapp.models import Album

class CadastroAlbums: 
    
    def criar(titulo, artista, genero):
        a = Album()
        a.artista = artista
        a.titulo = titulo
        a.genero = genero
        a.save()
        return a 
    def obter(id):
        return Album.objects.filter(id = id).first()
    
    def excluir(id):
        a = CadastroAlbums.obter(id)
        a.delete()
    
    def atualizar(id, titulo, artista, genero):
        a = CadastroAlbums.obter(id)
        if a is None:
            raise ValueError('Album não existe.')
        a.artista = artista
        a.titulo = titulo
        a.genero = genero
        a.save()

    def obter_ultimos_albuns(quantidade):
        return Album.objects.order_by("-id")[:quantidade]


class CadastrosMusicas:
    #titulo = models.CharField(max_length = 200, null = None)
    #compositor = models.TextField(null = None)
    #duracao = models.SmallIntegerField()
    #album = models.ForeignKey(Album, on_delete = models.CASCADE) 
   
    def criar(titulo, compositor, duracao, album_id):
        m = Musica()
        m.compositor = compositor
        m.titulo = titulo
        m.duracao = duracao
        m.album = CadastroAlbums.obter(album_id)
        m.save()
        return m 
    
    def obter(id):
        return Musica.objects.filter(id = id).first()
    
    def excluir(id):
        m = CadastrosMusicas.obter(id)
        m.delete()
    
    def atualizar(id, titulo, compositor, duracao, album_id):
        m = CadastrosMusicas.obter(id)
        if m is None:
            raise ValueError('Album não existe.')
        m.compositor = compositor
        m.titulo = titulo
        m.duracao = duracao
        m.album = CadastroAlbums.obter(album_id)
        m.save()


    def obter_ultimas_msuicas(quantidade):
        return Musica.objects.order_by("-id")[:quantidade]