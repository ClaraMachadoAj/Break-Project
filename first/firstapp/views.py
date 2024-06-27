from django.shortcuts import render
from django.views import View
from .cadastros import CadastroAlbums
from .cadastros import CadastrosMusicas
from .cadastros import CadastroArtistas


class HomeView(View):
    def get(self, request):
        ultimos_artistas =  CadastroArtistas.obter_ultimos_artistas(10)
        ultimos_albuns =  CadastroAlbums.obter_ultimos_albuns(10)
        ultimas_musicas =  CadastrosMusicas.obter_ultimas_musicas(10)
        context = {'artistas': ultimos_artistas, 'albuns': ultimos_albuns, 'musicas': ultimas_musicas}
        return render(request, 'index.html', context)    


class AlbumView(View):
    def get(self, request):
        ultimos_albuns =  CadastroAlbums.obter_ultimos_albuns(10)
        context = {'albuns': ultimos_albuns}
        return render(request, 'index.html', context)

class AlbumViewOne(View):
    def get(self, request, id):
        album = CadastroAlbums.obter(id)
        context = {'album': album}
        return render(request, 'album_detail.html', context)