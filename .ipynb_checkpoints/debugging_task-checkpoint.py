# Function to print dictionary values given the keys
# change 'k' (not defined) to key
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!",                # change from ' to "
                         "maggie": "(Pacifier Suck)"}

# enter the correct number of inputs
print_values_of(simpson_catch_phrases, ["lisa", "bart", "homer"])

