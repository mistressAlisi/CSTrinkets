from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json,time,urllib.request,re,string,copy,itertools
import numpy as np
from CSTrinkets import knightsTour
# Create your views here.


# Reverse Row at specified index in the matrix
def reverseRow(data, index):
    cols = len(data[index])
    for i in range(cols // 2):
        temp = data[index][i]
        data[index][i] = data[index][cols - i - 1]
        data[index][cols - i - 1] = temp
    return data
# Rotate Matrix by 180 degrees
def rotateMatrix180c(data):

    rows = len(data)
    cols = len(data[0])
    if (rows % 2):
        data = reverseRow(data, len(data) // 2)
        for i in range(rows // 2):
            for j in range(cols):
                temp = data[i][j]
                data[i][j] = data[rows - i - 1][cols - j - 1]
                data[rows - i - 1][cols - j - 1] = temp
        return data

matrixY = ['A','B','C','D','E','F','G','H',"J","I","K","L"]
@csrf_exempt
def run_matrixMadness(request):
    #print(request.POST)
    # Step one: Fetch and build the matrix:
    if ('dim' not in request.POST) or ('oper' not in request.POST):
        return JsonResponse({'res':"err","payload":{"string":'Error!!',"matrix":'Err.','runtime':'Error.'}},safe=False)
    dim = int(request.POST['dim'])
    matrix = []
    for mY in range(0,dim):

        level = []
        for mX in range(0,dim):
            level.append(request.POST[f"m_{mY}.{mX}"])
        matrix.append(level)
    # Step 2: Now lets perform the operation requested:
    oper = request.POST['oper']
    tic = time.perf_counter()
    # Do the operations here:
    # 90 degree rotation with zip right:
    if (oper == 'r90l'):
        matrix = list(zip(*reversed(matrix)))
    # 90 degree rotation with zip left:
    if (oper == 'l90l'):
        matrix = list(reversed(list(zip(*matrix))))
    # vertical sort with Zip:
    elif (oper == 'zvo'):
        matrix = list(zip(*(matrix)))
    # Numpy 90deg Right Rotate:
    elif (oper == 'n90r'):
        matrix = np.rot90(matrix,k=1,axes=(1,0)).tolist()
    # Numpy 90deg Left Rotate:
    elif (oper == 'n90l'):
        matrix = np.rot90(matrix,k=1,axes=(0,1)).tolist()
    # Numpy Roll Array by N places left:
    elif (oper == 'nrnl'):
        matrix = np.roll(matrix,dim*-1).tolist()
    # Numpy Roll Array by N places right:
    elif (oper == 'nrrl'):
        matrix = np.roll(matrix,dim).tolist()
    # Numpy Roll Array by 2N places left:
    elif (oper == 'nr2l'):
        matrix = np.roll(matrix,dim*-2).tolist()
    # Numpy Roll Array by 2N places right:
    elif (oper == 'nr2r'):
        matrix = np.roll(matrix,dim*2).tolist()
    # Custom 180 degree rotate:
    elif (oper == "n180"):
        matrix = np.rot90(np.rot90(matrix,k=1,axes=(1,0)),k=1,axes=(1,0)).tolist()
    outstr =  ','.join(list(itertools.chain.from_iterable(matrix)))
    toc = time.perf_counter()
    #print(tour_data)
    #print(matrix)
    return JsonResponse({'res':"ok","payload":{"string":outstr,"matrix":matrix,'runtime':toc-tic,'dim':dim}},safe=False)
