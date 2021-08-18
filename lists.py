# from random import randint, uniform,random


# play_slot_machine=randint(0,10)

# def estimate_average_slot_payout(n_runs):
#     """Run the slot machine n_runs times and return the average net profit per run.
#     Example calls (note that return value is nondeterministic!):
#     >>> estimate_average_slot_payout(1)
#     -1
#     >>> estimate_average_slot_payout(1)
#     0.5
#     """
#     i=0
#     gain=[]
#     while i<n_runs:
#         print(play_slot_machine)
#         gain.append(play_slot_machine-1)
#         i+=1

#help(str.isdigit)

#     return (sum(gain)/n_runs)


# print(estimate_average_slot_payout(10))
# '_______________________________________'

zip_code="12346"

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    if len(zip_code)==5 and zip_code.isdigit():
        return True
    return False 

print((is_valid_zip(zip_code)))

# '____________________________________'

# A researcher has gathered thousands of news articles. But she wants to focus her attention on articles including a specific word. Complete the function below to help her filter her list of articles.

# Your function should meet the following criteria:

# Do not include documents where the keyword string shows up only as a part of a larger word. For example, if she were looking for the keyword “closed”, you would not include the string “enclosed.”
# She does not want you to distinguish upper case from lower case letters. So the phrase “Closed the case.” would be included when the keyword is “closed”
# Do not let periods or commas affect what is matched. “It is closed.” would be included when the keyword is “closed”. But you can assume there are no other types of punctuation.
doc_list = ['The Learn Python Challenge Casino has a big casino full of casino games', 'They bought a car', 'Casinoville']
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
        
                
               

print(word_search(doc_list, 'car'))

#_________________________________________________________________________________________________________


