from django.shortcuts import render
from . import forms
from . import models
# Create your views here.

def new_view(request):
    return render(request, 'carpark/new.html')

def new_game(request):
    if request.method == "POST":
        form = forms.CreatePerson(request.POST)
        game = models.Game.create("123")
        if form.is_valid():
            player_name = form.cleaned_data['name']

            return render(request, 'carpark/wait_page.html', {'game_id': game.game_id})
    else:
        form = forms.CreatePerson()
    return render(request, 'carpark/new_game.html', {'form': form})

def join_game(request):
    return render(request, 'carpark/join_game.html')

def quiz(request):
    output = []
    if request.method == "POST":
        form = forms.AnswerForm(False, request.POST)
        words = form.words
        answer = form.answer
        if form.is_valid():
            source = form.cleaned_data['answer']
            if source == answer:
                form = forms.AnswerForm(True)
                words = form.words
                output = []
            else:
                form = forms.AnswerForm(False)
                words = form.words
                output = ["Wrong answer"]
    else:
        form = forms.AnswerForm(False)
        words = form.words
    return render(request, 'carpark/quiz.html', {'form': form, 'words': words, 'output': output})
