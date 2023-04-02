#███████╗███████╗███████╗██╗░░██╗░█████╗░███╗░░██╗██████╗░░█████╗░
#╚════██║██╔════╝██╔════╝██║░░██║██╔══██╗████╗░██║██╔══██╗██╔══██╗
#░░███╔═╝█████╗░░█████╗░░███████║██║░░██║██╔██╗██║██║░░██║███████║
#██╔══╝░░██╔══╝░░██╔══╝░░██╔══██║██║░░██║██║╚████║██║░░██║██╔══██║
#███████╗███████╗███████╗██║░░██║╚█████╔╝██║░╚███║██████╔╝██║░░██║
#╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝
#𝑂𝑛𝑙𝑦 𝑢𝑠𝑒 𝑡ℎ𝑖𝑠 𝑓𝑜𝑟 𝑒𝑑𝑢𝑐𝑎𝑡𝑖𝑜𝑛𝑎𝑙 𝑝𝑢𝑟𝑝𝑜𝑠𝑒𝑠. 
#𝐼𝑓 𝑦𝑜𝑢 𝑠𝑡𝑎𝑟𝑡 𝑖𝑡. 𝑌𝑜𝑢 ℎ𝑎𝑣𝑒 3 𝑠𝑒𝑐𝑜𝑛𝑑𝑠 𝑡𝑜 𝑠𝑒𝑙𝑒𝑐𝑡 𝑦𝑜𝑢𝑟 𝑡𝑦𝑝𝑒𝑏𝑎𝑟. 
#𝑇ℎ𝑒𝑛 𝑖𝑡 𝑎𝑢𝑡𝑜𝑚𝑎𝑡𝑖𝑐𝑙𝑦 𝑠𝑡𝑎𝑟𝑡 𝑠𝑝𝑎𝑚𝑚𝑖𝑛𝑔 / 𝑡𝑦𝑝𝑖𝑛𝑔. 
#𝑆𝑜𝑚𝑒 𝑡ℎ𝑖𝑛𝑔𝑠 𝑎𝑟𝑒𝑛' 𝑡 𝑐𝑜𝑟𝑟𝑒𝑐𝑡 𝑒𝑛𝑔𝑙𝑖𝑠ℎ. 𝐵𝑢𝑡 𝑡ℎ𝑎𝑡𝑠 𝑘𝑖𝑛𝑑𝑎 𝑓𝑢𝑛𝑛𝑦!

import random
import pyautogui
import time
from tkinter import simpledialog, Tk
from tkinter import messagebox
import sys

names = ['Jan', 'Aidan', 'Gerard', 'Harry Potter', 'Hermione Granger', 'Ron Weasley', 'Albus Dumbledore', 'Severus Snape', 'A tree', 'A seal', 'A mother', 'Lushairplane165', 'Sealosaurus', 'Your mom', 'Obama', 'Trump']
verbs = ['eats', 'walks', 'works', 'swims', 'sleeps', 'licks', 'wobbles', 'threatens', 'drinks', 'learns', 'plays', 'flies', 'falls', 'sits', 'runs', 'sings', 'understands', 'forgets', 'thinks', 'writes']
subjects = ['dog', 'cat', 'book', 'car', 'computer', 'bike', 'phone', 'painting', 'guitar', 'airplane', 'Golf cart', 'Whomping Willow', 'Quidditch match with Harry Potter', 'Nimbus 2000', 'seal', 'monkey']
with_what = ['with a', 'on a', 'in a', 'by a', 'under a', 'over a']

root = Tk()
root.withdraw()

num_sentences = simpledialog.askinteger(title="Number of Sentences", prompt="How many sentences would you like to generate?")

if num_sentences > 15:
    result = messagebox.askquestion("Are you sure?", f"You have entered {num_sentences}. Are you sure? It's more than 15.")
    if result == 'no':
        num_sentences = 0
        sys.exit(0)

time.sleep(3)
pyautogui.typewrite("This user has used the ©️Sealosaurus - Window spammer. If this user uses it wrong, it is their fault, not ©️Sealosaurus's.")
pyautogui.press("enter")
time.sleep(0.2)
pyautogui.typewrite("----------------------------------------------------")
pyautogui.press("enter")

# Define a function to generate a sentence
def generate_sentence():
    random_name = random.choice(names)
    random_verb = random.choice(verbs)
    random_subject = random.choice(subjects)
    random_with_what = random.choice(with_what)

    # Change 'with' to 'by' if the subject is a dog, cat or monkey
    if random_subject in ['dog', 'cat', 'monkey'] and random_with_what == 'with a':
        random_with_what = 'by a'

    # Construct the sentence using the randomly chosen components
    sentence = f"{random_name} {random_verb} {random_with_what} {random_subject}."
    return sentence

# Generate the specified number of sentences and display them using pyautogui
for i in range(num_sentences):
    sentence = generate_sentence()

    # Check if the sentence contains repeated prepositions and generate a new sentence if so
    while ' on on ' in sentence or ' in in ' in sentence or ' with with ' in sentence or ' near near ' in sentence or ' under under ' in sentence or ' over over ' in sentence:
        sentence = generate_sentence()

    time.sleep(0.5)
    pyautogui.typewrite(sentence)
    pyautogui.press("enter")
