from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def translate(request):
    original = request.GET['originaltext'].lower()
    translation = ''
    for word in original.split():
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            #this is a vowel
            translation += word
            translation += 'yay '
        else:
            #consonant
            #translation += word
            translation += word[1:] + word[0] + 'ay '

    return render(request, 'translate.html',
    {'original': original, 'translation': translation})
