from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    game = Games.objects.all()
    context = {'game':game}
    return render(request,'base/main.html',context)
def gaming_profile(request,pk):
    game_pf = BattleRoyale.objects.filter(Game__name=pk)
    context = {'pf':game_pf}
    return render(request,'base/profile.html',context)