from itertools import chain

fileName = input("Please type the file name.\n")

words = []
ngram = []
counts = []
prob = []
length = 0
temp = 0


def unigramValues():
    global length
    for i in words:
        if i not in ngram: 
            ngram.append(i)
            counts.append(1)
        else:
            index = ngram.index(i)
            counts[index] += 1
    length = len(ngram)
    
    
def unigramProbabilities():
    sum = 0
    for i in counts:
        sum += i
    print("\nUnigram Probabilities:")
    for i in range(len(ngram)):
        prob.append([ngram[i],counts[i] / sum])
    print(prob)
    prob.clear()
        
    
def bigramValues():
    global temp
    count = 0
    for i in words:
        for j in words:
            for x in range(len(words)-1):
                if(words[x] == i and words[x+1] == j):
                    count += 1
            if [i,j] not in ngram:
                ngram.append([i,j])
                counts.append(count)
            count = 0
    temp = len(ngram)       
     
                   
def bigramProbabilities():
    print("\nBigram Probabilities:")
    for i in range(length,len(ngram)):
        index = ngram.index(ngram[i][0])
        if(counts[index] != 0):
            prob.append([ngram[i],counts[i] / counts[index]])
    print(prob)
    prob.clear()      
        

def trigramValues():
    count = 0
    for i in range(length):
        for j in range(length,len(ngram)):
            for x in range(len(words) - 2):
                if(words[x] == ngram[i] and words[x+1] == ngram[j][0] and words[x+2] == ngram[j][1]):
                    count += 1
            if [ngram[i],ngram[j][0],ngram[j][1]] not in ngram:
                ngram.append([ngram[i],ngram[j][0],ngram[j][1]])
                counts.append(count)
            count = 0
            

def trigramProbabilities():
     print("\nTrigram Probabilities:")
     for i in range(temp,len(ngram)):
        list1 = [ngram[i][0], ngram[i][1]]
        index = ngram.index(list1)
        if(counts[index] != 0):
            prob.append([ngram[i],counts[i] / counts[index]])
     print(prob)
     prob.clear()   
     
     
def calculate():
    unigramValues()
    unigramProbabilities()
    bigramValues()
    bigramProbabilities()
    trigramValues()
    trigramProbabilities()    
       
     
def main():
    global n
    global words
    with open(fileName) as file:
        for line in file:
            words.append(line.rstrip().lower().split(" "))     #Read file line by line and append it into a list.

    words = list(chain.from_iterable(words))    #Convert to 1D list.
    
    calculate()


main()
