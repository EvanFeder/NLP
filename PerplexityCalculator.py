from collections import Counter
import math
import sys



def clean(file):
    ''' Takes a file path and returns the whole text as one string '''
    text = ""
    with open (file) as f:
        lines = f.readlines()
        for line in lines:
            text += line
    return text


def rel_frequency(tokens, tokensize):
    ''' Returns a dict of relative frequency on tokens with tokensize # of terms per token '''
    result = {}
    new_tokens = []
    size = tokensize - 1
    for i in range(0, len(tokens) - size):
        new_token = ""
        for j in range(i, i + size + 1):
            if new_token != "":
                new_token += " "
            new_token += tokens[j]
        if new_token in result:
            result[new_token] += 1
        else:
            result[new_token] = 1
            new_tokens.append(new_token)
    return {x: i / len(result) for (x,i) in result.items()}
    

if __name__ == '__main__':

    # Take in arguments
    lamda0 = float(sys.argv[1])
    lamda1 = float(sys.argv[2])
    lamda2 = float(sys.argv[3])
    lamda3 = float(sys.argv[4])
    testfile_path = sys.argv[5]
    trainfile_path = sys.argv[6]

    # Grab text files
    testfile = clean(testfile_path)
    trainfile = clean(trainfile_path)

    # Replace uncommon words
    traintokens = [s for s in trainfile.split()]
    train_counts = Counter(traintokens)
    traintokens = [x if train_counts[x] > 5 else "UNKNOWNWORD" for x in traintokens]
    unique_traintokens = set(traintokens)

    # Replace unknown words
    testtokens = [s for s in testfile.split()]
    testtokens = [x if (x in unique_traintokens) else "UNKNOWNWORD" for x in testtokens]
    
    # Create model dictionaries
    uniform_prob = 1.0 / len(unique_traintokens)
    unigram_set = rel_frequency(traintokens, 1)
    bigram_set = rel_frequency(traintokens, 2)
    trigram_set = rel_frequency(traintokens, 3)

    # Calculate probabilities
    probs = [0]*len(testtokens)
    for i, token in enumerate(testtokens):
        prob1 = lamda0 * uniform_prob
        prob2 = lamda1 * unigram_set[token]
        if i > 0 and (testtokens[i-1] + " " + token) in bigram_set:
            prob3 = lamda2 * bigram_set[testtokens[i-1] + " " + token]
        else:
            prob3 = 0
        if i > 1 and (testtokens[i-2] + " " + testtokens[i-1] + " " + token) in trigram_set:
            prob4 = lamda3 * trigram_set[testtokens[i-2] + " " + testtokens[i-1] + " " + token]
        else:
            prob4 = 0
        probs[i] = prob1 + prob2 + prob3 + prob4

    # Using presicion formula, calculate text perplexity
    temp_math = 0
    for prob in probs:
        temp_math += math.log(1 / prob)
    perplexity = math.e ** (temp_math / len(testtokens))

    with open ("result.txt", "w") as f:
        f.write(str(perplexity))

    print(perplexity)
