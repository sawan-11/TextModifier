# creating files
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text from the user
    User_text = request.POST.get('text', 'default')

    # check box values
    remove_punc = request.POST.get('remove_punc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newLineRemover = request.POST.get('newLineRemover', 'off')
    spaceRemover = request.POST.get('spaceRemover', 'off')
    charCount = request.POST.get('charCount', 'off')

    # checking which box is checked
    if remove_punc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in User_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        # Analyze the text
        User_text = analyzed

    # checking which box is checked
    if fullcaps == 'on':
        analyzed = ""
        for char in User_text:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'capitalized text', 'analyzed_text': analyzed}
        User_text = analyzed

    if(newLineRemover == 'on'):
        analyzed = ""
        for char in User_text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'capitalized text', 'analyzed_text': analyzed}
        User_text = analyzed

    if(spaceRemover == 'on'):
        analyzed = ""
        for index, char in enumerate(User_text):
            if not (User_text[index] == " " and User_text[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose': 'capitalized text', 'analyzed_text': analyzed}
        User_text = analyzed

    if(charCount == 'on'):
        analyzed = ""
        analyzed = f"your text length is {len(User_text)}"

        params = {'purpose': 'capitalized text', 'analyzed_text': analyzed}

    if (remove_punc != 'on' and fullcaps != "on" and newLineRemover != 'on' and spaceRemover != 'on'):
        return HttpResponse("error! please select any opreations")

    return render(request, 'analyze.html', params)


def About(request):
    return HttpResponse("about page here")


def contact(request):
    return HttpResponse("contact here")
