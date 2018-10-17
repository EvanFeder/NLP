import sys



def osa_distance(word1, word2, mem):
    '''  Returns OSA distance using insert, delete, substitute, and transpose '''
    
    matrix = [[0 for i in range(0, len(word2) + 1)] for j in range(0, len(word1) + 1)]
    
    for i in range(0, len(word1) + 1):
        matrix[i][0] = i
    for j in range(0, len(word2) + 1):
        matrix[0][j] = j

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            cost = 0
            if word1[i-1] != word2[j-1]:
                cost = 1
            
            matrix[i][j] = min([matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + cost])
    
            if i > 1 and j > 1 and word1[i-1] == word2[j-2] and word1[i-2] == word2[j-1]:
                matrix[i][j] = min(matrix[i][j], matrix[i-2][j-2] + cost)

    return matrix[-1][-1]

def lev_distance(word1, word2, mem):
    '''  Returns Levenshtein distance using insert, delete, and substitute '''
    
    matrix = [[0 for i in range(0, len(word2) + 1)] for j in range(0, len(word1) + 1)]

    for i in range(0, len(word1) + 1):
        matrix[i][0] = i
    for j in range(0, len(word2) + 1):
        matrix[0][j] = j

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            cost = 0
            if word1[i-1] != word2[j-1]:
                cost = 1
            
            matrix[i][j] = min([matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + cost])
    
    return matrix[-1][-1]

def get_dictionary_match(word, dictionary, mem, mode):
    ''' Returns matched word and distance, with method dependent on mode '''
    
    best_match = ""
    best_dist = -1
    for term in dictionary:
        if mode == 1:
            new_dist = lev_distance(word, term, mem)
        elif mode == 2:
            new_dist = osa_distance(word, term, mem)
        
        if best_dist == -1 or new_dist < best_dist:
            best_dist = new_dist
            best_match = term

    return best_match, best_dist
    


def clean_file(file):
    ''' Takes a file path and returns a list, one line per member '''
    with open (file) as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        return lines


if __name__ == '__main__':
    
    # Take in arguments
    mode = int(sys.argv[1])
    raw_path = sys.argv[2]
    dictionary_path = sys.argv[3]
    output_path = sys.argv[4]

    raw_words = clean_file(raw_path)
    dictionary = clean_file(dictionary_path)

    mem = {}
    output_tuples = []
    outputs = []

    for word in raw_words:
        output_tuples.append(get_dictionary_match(word, dictionary, mem, mode))

    # Format for output
    for output in output_tuples:
        outputs.append(output[0] + " " + str(output[1]) + "\n")

    with open (output_path, "w") as f:
        f.writelines(outputs)
