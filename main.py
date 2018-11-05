
import re


def remove_special_characters(question):
    question = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", question)
    question = re.sub("[\(\[].*?[\)\]]", "", question)
    question = re.sub(r"n\'t", " not", question)
    question = re.sub(r"\'re", " are", question)
    question = re.sub(r"\'s", " is", question)
    question = re.sub(r"\'d", " would", question)
    question = re.sub(r"\'ll", " will", question)
    question = re.sub(r"\'t", " not", question)
    
    return question



def preprocess_sentences(sentence):
    sentence = sentence.lower()
    sentence = sentence.strip()
    sentence = remove_special_characters(sentence)
    
    return sentence
    


article = input("Enter the text you want to summarize\n")


sentences = article.split('.')
sentences_weight={}

for i in sentences:
    i = preprocess_sentences(i)
    #print(i)
    sentences_weight[i] = 0
    
word_count={}

for i in sentences:
    i = preprocess_sentences(i)
    sentence = i.split(' ')
    for j in sentence:
        if j not in word_count:
            word_count[j] = 1
        else:
            word_count[j] = word_count[j]+1
            

maximum_count=-1

for i in word_count:
    if word_count[i] > maximum_count:
        maximum_count = word_count[i]
        
        
for i in word_count:
    word_count[i] = word_count[i]/maximum_count
    
for i,j in sentences_weight.items():
    
    sentence = i.split(' ')
    sum = 0
    
    for k in sentence:
        sum = sum + word_count[k]
    sentences_weight[i] = sum
    
count = 0 

sentences_weight = sorted(sentences_weight.items(), key=lambda x: x[1], reverse = True)

for i in sentences_weight:
    print (i[0], end='')
    print(".")
    count = count +1 
    if count >=3:
        break
    