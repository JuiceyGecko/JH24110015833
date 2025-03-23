# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])  # Changed 'k' to 'key' to access the dictionary values.

# Print dictionary values from simpson_catch_phrases


simpson_catch_phrases = {"lisa": "BAAAAAART!",
                         "bart": "Eat My Shorts!",
                         "marge": "Mmm~mmmmm",
                         "homer": "d'oh!",  # Added quotes (") to properly format the string.
                         "maggie": "(Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])  # Added "[ ]" to pass the keys as a list.

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''
