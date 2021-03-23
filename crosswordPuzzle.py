import numpy as np

def checkRow(row):
    stack = {}
    length = 0
    for i in range(len(row)):
        if row[i] == "1.0":
            length +=1
        else:
            if length>0:
                stack.update({str(i):length})
                length=0                
    return stack
def checkCol(col):
    stack = {}
    length = 0
    for i in range(len(col)):
        if col[i] != "0.0":
            length +=1
        else:
            if length>0:
                stack.update({str(i):length})
                length=0                
    return stack
def findFitWord(words, l):
    index = []
    for i in range(len(words)):
        if len(words[i]) == l:
            index.append(i)
    return index
def fill(matrix, words):
    for row in range(matrix.shape[0]):
        emptyArea = [(int(end), l) for (end, l) in checkRow(matrix[row]).items()]
        for i in range(len(emptyArea)):
            end, l = emptyArea[i]
            fitWs = findFitWord(words, l)
            if len(fitWs) == 0:
                continue
            for k in range(len(fitWs)):
                wordChoose=wordChoose[k]
                for j in range(l):
                    matrix[row, end-l+j]= ' ' + wordChoose[j] + ' '
                words.pop(k)
                if not fill(matrix, words):
                    for j in range(l):
                        matrix[row, end-l+j]= "1.0"
                    words.append(wordChoose)
    for col in range(matrix.shape[1]):
        emptyArea = [(int(end), l) for (end, l) in checkCol(matrix[:,col]).items()]
        for i in range(len(emptyArea)):
            end, l = emptyArea[i]
            fitWs = findFitWord(words, l)
            if len(fitWs) == 0:
                continue
            for k in range(len(fitWs)):
                wordChoose=wordChoose[k]
                for j in range(l):
                    matrix[end-l+j, col]= ' ' + wordChoose[j] + ' '
                words.pop(k)
                if not fill(matrix, words):
                    for j in range(l):
                        matrix[row, end-l+j]= "1.0"
                    words.append(wordChoose)
                else:
                    emptyArea.pop()
    if len(words)==0 and 

            
def main():
    words = ["AGRA","NORWAY","ENGLAND","GWALIOR"]
    matrix = np.zeros((10,10))
    matrix[0:7,1]=1
    matrix[2,1:8]=1
    matrix[5,1:7]=1
    matrix[6:9,5]=1
    # print(matrix.shape[0])
    # print(checkRow(matrix[2]))
    # print(checkCol(matrix[:,5]))
    matrix=matrix.astype(str)
    fill(matrix,words)
    print(matrix)
if __name__ == "__main__":
    main()

# +-++++++++
# +-++++++++
# +-------++
# +-++++++++
# +-++++++++
# +------+++
# +-+++-++++
# +++++-++++
# +++++-++++
# ++++++++++

