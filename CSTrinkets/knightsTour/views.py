from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json,time,urllib.request,re,string
from bs4 import BeautifulSoup

from CSTrinkets import knightsTour
# Create your views here.

@csrf_exempt
def run_knightsTour(request):
    #print(request.POST)
    # Step one: Fetch and build the matrix:
    matrix = []
    for mY in (['A','B','C','D','E','F','G','H']):
        level = []
        for mX in range(1,9):
            level.append(request.POST[f"m_{mY}.{mX}"])
        matrix.append(level)
    #print(matrix)
    # Step 2: Now lets figure out if we need the URL or the Text string provided:
    # Text string is provided?:
    if ('inputtext' in request.POST):
        itext = request.POST['inputtext']

    # Step 2a. URL:
    if ('url' in request.POST):
        source = "INPUT TEXT"
        text_data = ""
        sourceURL = request.POST['url']
        if (sourceURL != ""):
            #print("Trying URL")
            try:
                html_data = urllib.request.urlopen(sourceURL).read().decode("utf-8")
                soup = BeautifulSoup(html_data,'lxml')
                text_data = soup.get_text()
            except Exception as e:
                print(e)
                matrixData = "URL Error."
                debug = str(e)
                out = f"URL fetch error for: {sourceURL}"
                return JsonResponse({'res':"ok","payload":{"string":out,"matrix":matrixData,'debug':debug}},safe=False)
            finally:
                # use the URL data:
                if (text_data != ""):
                    itext = text_data
                    source = sourceURL
    # Build the dictionary:
    dictionary = itext.upper().split(" ")[:-1]
    # Initialise the Trie:
    WordsTrie = knightsTour.Trie()
    for word in dictionary:
        WordsTrie.insert(word)
    # run the tour!
    tic = time.perf_counter()
    tour_data =  knightsTour.the_grand_tour(WordsTrie,matrix)
    toc = time.perf_counter()
    #print(tour_data)
    try:
        matrixData = f"Lenght: {tour_data[1]} @ pos: X {tour_data[2].x}, Y: {tour_data[2].y} -> Letter: {tour_data[2].char()}"
        debug = f"For Source from '{source}':\n<-**Completed in: {toc - tic:0.4f} seconds**->\n<-**Debug Output**->:\n{tour_data[3]}"
        out = tour_data[0]
    except AttributeError:
        matrixData = "NO SOLUTIONS!!!"
        debug = "NO SOLUTIONS!!!"
        out = "No strings possible."
    return JsonResponse({'res':"ok","payload":{"string":out,"matrix":matrixData,'debug':debug}},safe=False)
