import csv
from nltk.tokenize import word_tokenize, sent_tokenize
from unidecode import unidecode
import string

f =open("data.csv", "rb")
csv_d= csv.reader(f, delimter="\t")



#Function to tokenize a document into words and to remove punctuations:

exclude = string.punctuation
def get_words(sent):
    sent=sent.lower()
    sent=unidecode(sent.decode('utf-8'))
    temp=""
    for ch in sent:
        if(ch not in exclude):
            temp+=ch
        else:
            temp+=" "
    arr = word_tokenize(temp)
    sent=[]
    for i in arr:
        if i!="" and i!=" ":
            sent.append(i)
    return sent


#Creating inverted index as a dictionary:


for doc , row in enumerate(csv_d):
    f=open(file_name,"r")
    text=f.read()
    arr=get_words(text)
    print doc,file_name
    for i, term in enumerate(arr):
        if term not in index.keys():
            index[term]={}
            index[term][doc]=[]

        else:
            if doc not in index[term].keys():
                index[term][doc]=[]

        index[term][doc].append(i)


while True:
	q = str( raw_input("Enter your query"))
	print q
