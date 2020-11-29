'''
    # this is my firat home page with django
'''
from django.http import HttpResponse
from django.shortcuts import render

def index(request): #params = {'Name':'XYZ','Email':'xyz@gmail.com','Contact':'8888880006'}
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('txtstory', 'default')
    
    removePunc = request.POST.get('removePunc', 'off') # variable used for remove symbols
    allCaps = request.POST.get('allCaps', 'off') # variable used for convert data into uppercase
    removeNewLines = request.POST.get('removeNewLines', 'off') # variable used for remove new lines
    removeExtraSpaces = request.POST.get('removeExtraSpaces', 'off') # variable used for remove extra spaces
    allLowerCase = request.POST.get('allLowerCase', 'off') # variable used to convert all in lower case
    cntLower = request.POST.get('cntLower', 'off') # variable used to count lower case
    cntUppers = request.POST.get('cntUppers', 'off') # variable used for capital letter counting
    cntLetters = request.POST.get('cntLetters', 'off') # count all leters
    cntNumbers = request.POST.get('cntNumbers', 'off')# variable used to count numbers
    cntSymbols = request.POST.get('cntNumbers', 'off') # variable used to count symbols

    if removePunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(allCaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # if you dont want to apply all at time return render(request, 'analyze.html', params)

    if(removeExtraSpaces=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (removeNewLines == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (allLowerCase == "on"):
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.lower()
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed #return render(request, 'analyze.html', params)

    if (cntLower == "on"):
        analyzed = ""
        cnt = 0
        for char in djtext:
            if(char.islower()):
                analyzed = analyzed + char
                cnt+=1
        params = {'purpose': 'Count lower', 'analyzed_text': analyzed, 'Counter':cnt}
        djtext = analyzed

    if (cntUppers == "on"):
        analyzed = ""
        cnt=0
        for char in djtext:
            if(char.isupper()):
                cnt += 1
                analyzed = analyzed + char
        params = {'purpose': 'Count Upper', 'analyzed_text': analyzed, 'Counter': cnt}
        djtext = analyzed
    
    if (cntLetters == "on"):
        analyzed = ""
        cnt=0
        for char in djtext:
            if(char.isalpha()):
                cnt += 1
                analyzed = analyzed + char
        params = {'purpose': 'Count aphabaste', 'analyzed_text': analyzed, 'Counter': cnt}
        djtext = analyzed
    
    if (cntNumbers == "on"):
        analyzed = ""
        cnt=0
        for char in djtext:
            if(char.isalnum()):
                analyzed = analyzed + char
                cnt += 1
        params = {'purpose': 'Count digit', 'analyzed_text': analyzed, 'Counter': cnt}
        djtext = analyzed
    
    if (cntSymbols == "on"):
        punctuations = '''!()-[]'"{'};:'"\,<>./?@#$%^&*_~'''
        cnt = 0
        for char in djtext:
            if(char in punctuations):
                cnt+=1
        params = {'purpose': 'Count digit', 'analyzed_text': analyzed, 'Counter':cnt}
        djtext = analyzed
    
    if(removePunc != "on" and allCaps != "on" and removeExtraSpaces != "on " and removeNewLines != "on" and allLowerCase != "on" and cntLower != "on" and cntUppers!="on" and cntLetters!="on" and cntNumbers!="on" and cntSymbols!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
