#import math

#print(dir(math)) imprime en una lista de nombres o métodos del módulo math

#print("pi to 4 significant digits={:.4}".format(math.pi))

# import * hace que las variables del modulo sean accesibles directamente sin necesidad del prefijo con punto. 
#El problema es que si se importan varias librerias y tienen la misma función, se genera conflicto con esta notación.
#Para usar submodulos de modulos, se usa dos puntos, del modulo más grande al más especifico

#rolls = numpy.random.randint(low=1, high=6, size=10)

#______________________________________________________________________________________________
# Import luigi's full dataset of race data
from learntools.python.luigi_analysis import full_dataset

# Fix me!
def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for item in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name']
                 )
    return winner_item_counts

# Try analyzing the imported full dataset
#print(full_dataset)
best_items(full_dataset)
