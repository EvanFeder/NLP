## NLP
General collection of code as I explore into the field of Natural Language Processing

# Perplexity Calculator

Perplexity is a measure of how well a language model predicts a sample of text. This program weights four different language models to create an interpolated language model, trains them on a training corpus, and then calculates the perplexity of a test text sample. The perplexity will be outputted to both the console and a file named result.txt.

Terminal: python PerplexityCalculator.py lamba0 lambda1 lambda2 lambda3 test_file_path training_file_path

The lambdas are the respective weightings of the uniform, unigram, bigram, and trigram language models. The test file path should be the path of the file you wish to calcualte the perplexity value of, and the training file path should be the path of the corpus on which you wish to train the interpolated language model.


# Dictionary Match

Given a list of potentially misspelled words, this program will use an edit distance calculator to find the closest dictionary match, and return a list of all the dictionary matches and the edit distance.

Terminal: python DictionaryMatch.py mode words_path dictionary_path output_path

The mode is the type of distance algorithm you wish to be used (1 for Levenshtein distance, 2 for Optimal String Alignment distance). The words path should be the path of the misspelled words, the dictionary path be the path of the dictionary, and the output path be the path of where the final output will be stored.
