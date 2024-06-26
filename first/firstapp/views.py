from django.shortcuts import render
from django.views import View
from .cadastros import CadastroAlbums


class AlbumView(View):
    def get(self, request):
        ultimos_albuns =  CadastroAlbums.obter_ultimos_albuns(10)
        context = {'albuns': ultimos_albuns}
        return render(request, 'first/index.html', context)
    
    

