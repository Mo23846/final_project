
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
import nltk
nltk.download('inaugural')
nltk.download('gutenberg')
nltk.download('nps_chat')
nltk.download('webtext')
nltk.download('treebank')
from nltk.corpus import inaugural
text = inaugural.raw()
wordcloud = WordCloud(max_font_size=60).generate(text)
plt.figure(figsize=(16,12))
# plot wordcloud in matplotlib
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
from  nltk.book import text4 as inaugural_speeches
plt.figure(figsize=(16,5))
topics = ['sports',  'news', 'Government']
inaugural_speeches.dispersion_plot(topics)
from nltk.corpus import brown
stop_words = set(STOPWORDS)
topics = ['Sports - الرياضة',  'News - الاخبار', 'Government - السياسة']
for topic in topics:
    words = [word for word in brown.words(categories=topic)
            if word.lower() not in stop_words and word.isalpha() ]
    freqdist = nltk.FreqDist(words)
    print(topic,'more :', ' , '.join([ word.lower() for word, count in freqdist.most_common(5)]))
    print(topic,'less :', ' , '.join([ word.lower() for word, count in freqdist.most_common()[-5:]]))

corpus_genre = 'government'
words = [word for word in brown.words(categories=corpus_genre) if word.lower() not in stop_words and word.isalpha() ]
freqdist = nltk.FreqDist(words)
plt.figure(figsize=(16,5))
freqdist.plot(50)
def lexical_diversity(text):
    return round(len(set(text)) / len(text),2)


def get_brown_corpus_words(category, include_stop_words=False):

    if include_stop_words:
        words = [word.lower() for word in brown.words(categories=category) if word.isalpha() ]
    else:
        words = [word.lower() for word in brown.words(categories=category)
                 if word.lower() not in stop_words and word.isalpha() ]
    return words

for genre in brown.categories():
    lex_div_with_stop = lexical_diversity(get_brown_corpus_words(genre, True))
    lex_div = lexical_diversity(get_brown_corpus_words(genre, False))
    print(genre ,lex_div , lex_div_with_stop)
