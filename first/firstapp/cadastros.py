from firstapp.models import Musica
from firstapp.models import Album
from firstapp.models import Artista
from firstapp.models import AvaliacaoMusica

class CadastroArtistas:
    def criar(nome):
        art = Artista()
        art.nome = nome
        art.save()

    def obter(id):
        return Artista.objects.filter(id = id).first()
    
    def excluir(id):
        art = CadastroAlbums.obter(id)
        art.delete()

    def atualizar(nome, artista_id):
        art = CadastroArtistas.obter(artista_id)
        if art is None:
            raise ValueError('Artista não existe.')
        art.nome = nome
        art.save()
    
    def obter_ultimos_artistas(quantidade):
        return Artista.objects.order_by("-id")[:quantidade]

class CadastroAlbums: 
    
    def criar(titulo, artista_id, genero, ano_lancamento):
        a = Album()
        a.titulo = titulo
        a.genero = genero
        a.artista = CadastroArtistas.obter(artista_id)
        a.ano_lancamento = ano_lancamento
        a.save()
        return a 
    
    def obter(id):
        return Album.objects.filter(id = id).first()
    
    def excluir(id):
        a = CadastroAlbums.obter(id)
        a.delete()
    
    def atualizar(id, titulo, artista, genero, artista_id):
        a = CadastroAlbums.obter(id)
        if a is None:
            raise ValueError('Album não existe.')
        a.artista = CadastroArtistas.obter(artista_id)
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


    def obter_ultimas_musicas(quantidade):
        return Musica.objects.order_by("-id")[:quantidade]
    
class CadastroAvaliacaoMusica:
    
    def criar(username, musica_id, nota):
        ava = AvaliacaoMusica()
        ava.username = username
        ava.musica = CadastrosMusicas.obter(musica_id)
        ava.nota = nota
        ava.save()
        return ava

    def obter(id):
        return AvaliacaoMusica.objects.filter(id=id).first()
    
    def obter_avaliacoes_usuario(username):
        return AvaliacaoMusica.objects.filter(username=username).all()
    

