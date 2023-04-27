from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render


def index(request):
    djtext = print(request.POST.get('text', 'default'))
    print(djtext)
    return render(request, 'index.html')
    # return HttpResponse('''<h1>"hello"</h1> <a href= "https://rjtsabharwal39.github.io/Resume"> Rajat's Resume </a>''')


def indee(request):
    return HttpResponse('''<a href= "https://www.google.com/" > Google </a>''')


def about(request):
    return HttpResponse("About hello")


def youtubevideo(request):
    djtext = request.POST.get('text', 'Rajat_Sabharwal')
    params = {'purpose': 'Removed Punctuations', 'analyzed_text': djtext}

    return render(request, 'index1.html', params)


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'Rajat_Sabharwal')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to upper case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (removepunc != "on" and extraspaceremover != "on" and newlineremover != "on" and fullcaps != "on"):
        return HttpResponse("<h4>Please select atleast one input</h4>")

    return render(request, 'analyze.html', params)

    print(djtext)
