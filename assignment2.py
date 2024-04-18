import pandas as pd
import nltk
from nltk.corpus import stopwords
if(nltk.data.find('corpora/stopwords') == -1):
    nltk.download('stopwords')


#step 1 :read paragraphs from text file

file_path = "random_paragraphs.txt"

with open(file_path, 'r',encoding='utf-8') as file:
    text = file.read()
paragraphs = text.splitlines()
len(paragraphs)

#step 2 : put data in dataframe

df = pd.DataFrame(paragraphs,columns=['Paragraph'])

# step 3 : removing stopwords

def removeStopwords(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)


df["Paragraph"]  = df.apply(lambda x: removeStopwords(x['Paragraph']), axis=1)


#step 4 : counting word frequency
word_freq : dict = {}
def countWordFrequency(text):
    words = text.split()
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq


df.apply(lambda x: countWordFrequency(x['Paragraph']), axis=1)
word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
word_freq_list = list(word_freq)
first_10_elements = word_freq_list[:10]
print(f'The 10 most common words are {first_10_elements}')
print(f'The total number of words is {len(word_freq)}')