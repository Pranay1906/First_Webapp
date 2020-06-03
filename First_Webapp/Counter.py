import operator


def count(article):
    words = article.split()
    count_word = len(words)
    dict_word = {}
    for word in words:
        if word in dict_word:
            dict_word[word] += 1
        else:
            dict_word[word] = 1
    var_dict = sorted(dict_word.items(), key=operator.itemgetter(1), reverse=True)
    return var_dict, count_word
