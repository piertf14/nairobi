from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize


positives = open('discussion/constants/positive.txt', 'r')
positive_message = positives.read()
positives.close()

negatives = open('discussion/constants/negative.txt', 'r')
negative_message = negatives.read()
negatives.close()

bd_pos = positive_message.split(",")
bd_neg = negative_message.split(",")


def ngrams(_input, n):
    _input = _input.split(' ')
    output = []
    for i in range(len(_input) - n + 1):
        output.append(_input[i:i + n])
    return output


stopset = set(stopwords.words('spanish'))


def evaluate_sentence(sentence):
    data = sentence
    word_sent_tokens = word_tokenize(data)

    # removing special characters
    regExpresionToken = RegexpTokenizer(r'\w+')
    tokens = regExpresionToken.tokenize(sentence)

    # removing stopwords
    removedata = [w for w in tokens if not w in stopset]

    sentCounter = 0
    sentence = []

    for w in word_sent_tokens:
        sentence.append(w.lower())

    for eachPosWord in sentence:
        if eachPosWord in bd_pos:
            sentCounter = sentCounter + 1

    for eachNegWord in sentence:
        if eachNegWord in bd_neg:
            sentCounter = sentCounter - 1

    for g in (' '.join(x) for x in ngrams(data, 2)):
        word_tokens = word_tokenize(g)
        sent = []
        for w in word_tokens:
            sent.append(w.lower())
        if sent[0] in bd_neg and sent[1] in bd_pos:
            sentCounter = sentCounter - 1

        if sent[0] in bd_neg and sent[1] in bd_neg:
            sentCounter = sentCounter + 2

    for g in (' '.join(x) for x in ngrams(data, 3)):
        word_tokens = word_tokenize(g)
        sent = []
        for w in word_tokens:
            sent.append(w.lower())

        if sent[0] in bd_neg and sent[1] in bd_pos and sent[2] in bd_pos:
            sentCounter -= 2

    return sentCounter >= 0
