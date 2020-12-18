from typing import List, Tuple, Callable
from utils import process_input, read_input

    
def frequencies(entry: Tuple) -> bool:
    min_freq, max_freq, letter, password = entry
    frequency_of_letter = password.count(letter)
    if frequency_of_letter >= int(min_freq) and frequency_of_letter <= int(max_freq):
        return True

def exactlyone(entry: Tuple) -> bool:
    fst_index, snd_index, letter, password = entry
    
    # we need to XOR here
    return (password[int(fst_index)-1] == letter) ^ (password[int(snd_index)-1] == letter)
    
def password_philosophy_parttone(password_entries: List, validation_method: Callable) -> int:
    
    valid_entries = 0
    for entry in password_entries:
        if validation_method(entry):
            valid_entries += 1
    return valid_entries
    
if __name__ == "__main__":
    password_entries = process_input(read_input("day2"))
    print("Answer to part 1 is: {}".format(password_philosophy_parttone(password_entries, frequencies)))
    print("Answer to part 1 is: {}".format(password_philosophy_parttone(password_entries, exactlyone)))