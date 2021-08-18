# Now the researcher wants to supply multiple keywords to search for. Complete the function below to help her.

# (You're encouraged to use the word_search function you just wrote when implementing this function. Reusing code in this way makes your programs more robust and readable - and it saves typing!)

def word_search(doc_list, keyword):
    # """
    # Takes a list of documents (each document is a string) and a keyword. 
    # Returns list of the index values into the original list for all documents 
    # containing the keyword.

    # Example:
    # doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    # >>> word_search(doc_list, 'casino')
    # >>> [0]
    # """
    indice=[]
    keyword=keyword.lower()
    
    
    for doc in doc_list:
        words=[]
        x=doc_list.index(doc)
        doc=doc.split()
        
        for word in doc:
            word=word.rstrip('.,').lower()
            words.append(word)
        if keyword in words:
            indice.append(x)
      
    
    return indice


def multi_word_search(doc_list, keywords):
    """
    # Takes list of documents (each document is a string) and a list of keywords.  
    # Returns a dictionary where each key is a keyword, and the value is a list of indices
    # (from doc_list) of the documents containing that keyword

    # >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    # >>> keywords = ['casino', 'they']
    # >>> multi_word_search(doc_list, keywords)
    # {'casino': [0, 1], 'they': [1]}
    """
    keyword_to_indices={}
    for keyword in keywords:
        #print(keyword)
        keyword_to_indices[keyword]=word_search(doc_list,keyword)
    return keyword_to_indices
    
doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['casino', 'they']

print(multi_word_search(doc_list,keywords))