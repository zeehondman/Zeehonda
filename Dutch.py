#███████╗███████╗███████╗██╗░░██╗░█████╗░███╗░░██╗██████╗░░█████╗░
#╚════██║██╔════╝██╔════╝██║░░██║██╔══██╗████╗░██║██╔══██╗██╔══██╗
#░░███╔═╝█████╗░░█████╗░░███████║██║░░██║██╔██╗██║██║░░██║███████║
#██╔══╝░░██╔══╝░░██╔══╝░░██╔══██║██║░░██║██║╚████║██║░░██║██╔══██║
#███████╗███████╗███████╗██║░░██║╚█████╔╝██║░╚███║██████╔╝██║░░██║
#╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝
#𝐴𝑙𝑙𝑒𝑒𝑛 𝑔𝑒𝑏𝑟𝑢𝑖𝑘 𝑑𝑖𝑡 𝑣𝑜𝑜𝑟 𝑒𝑑𝑢𝑐𝑎𝑡𝑖𝑜𝑛𝑎𝑙𝑒 𝑑𝑜𝑒𝑙𝑒𝑖𝑛𝑑𝑒𝑛.
#𝐴𝑙𝑠 𝑗𝑒 𝑠𝑡𝑎𝑟𝑡 ℎ𝑒𝑡, 𝑗𝑒 ℎ𝑒𝑏𝑡 3 𝑠𝑒𝑐𝑜𝑛𝑑𝑒𝑛 𝑜𝑚 jouw typbar te selecteren.
#𝐷𝑎𝑛 ℎ𝑒𝑡 start het automatisch 𝑠𝑝𝑎𝑚𝑚𝑖𝑛𝑔/𝑡𝑦𝑝𝑖𝑛𝑔.
#𝑆𝑜𝑚𝑚𝑖𝑔𝑒 𝑑𝑖𝑛𝑔𝑒𝑛 𝑧𝑖𝑗𝑛 𝑛𝑖𝑒𝑡 𝑐𝑜𝑟𝑟𝑒𝑐𝑡 𝑔𝑒𝑠𝑐ℎ𝑟𝑒𝑣𝑒𝑛. 𝑀𝑎𝑎𝑟 𝑑𝑎𝑡 𝑖𝑠 best grappig!!

import random
import pyautogui
import time
from tkinter import simpledialog, Tk
from tkinter import messagebox
import sys
names = ['Jan', 'Aidan', 'Gerard', 'Harry Potter', 'Hermelien Griffel', 'Ron Wemel', 'Albus Perkamentus', 'Severus Sneep', 'Een boom', 'Een zeehond', 'Een moeder', 'Lushairplane165', 'Zeehondasaurus', 'Je moeder', 'Obama', 'Trump']
verbs = ['eet', 'loopt', 'werkt', 'zwemt', 'slaapt', 'likt', 'wobbelt', 'dreigt', 'drinkt', 'leert', 'speelt', 'vliegt', 'valt', 'zit', 'rent', 'zingt', 'begrijpt', 'vergeet', 'denkt', 'schrijft']
subjects = ['hond', 'kat', 'boek', 'auto', 'computer', 'fiets', 'telefoon', 'schilderij', 'gitaar', 'vliegtuig', 'Golfcar', 'Beukwilg', 'Zwerkbalwedstrijd met Harry Potter', 'Nimbus 2000', 'zeehond', 'aap']
with_what = ['met een', 'op een', 'in een', 'bij een', 'onder een', 'over een']

root = Tk()
root.withdraw()

num_sentences = simpledialog.askinteger(title="Aantal zinnen", prompt="Hoeveel zinnen wil je genereren?")

if num_sentences > 15:
    result = messagebox.askquestion("Zeker?", f"Je hebt {num_sentences} ingevoerd. Weet je het zeker? Het is boven 15.")
    if result == 'no':
        num_sentences = 0
        sys.exit(0)
time.sleep(3)
pyautogui.typewrite("Deze user heeft de ©️Zeehonda - Vensterspammer gebruikt. Als deze user het verkeerd gebruikt. Is het zijn schuld. Niet van ©️Zeehonda")
pyautogui.press("enter")
time.sleep(0.2)
pyautogui.typewrite("----------------------------------------------------")
pyautogui.press("enter")

def generate_sentence():
    random_name = random.choice(names)
    random_verb = random.choice(verbs)
    random_subject = random.choice(subjects)
    random_with_what = random.choice(with_what)

    if random_subject in ['hond', 'kat', 'aap'] and random_with_what == 'met':
        random_with_what = 'door'

    sentence = f"{random_name} {random_verb} {random_with_what} {random_subject}."
    return sentence

for i in range(num_sentences):
    sentence = generate_sentence()
    while ' op op ' in sentence or ' in in ' in sentence or ' met met ' in sentence or ' bij bij ' in sentence or ' onder onder ' in sentence or ' over over ' in sentence:
        sentence = generate_sentence()

    time.sleep(0.5)
    pyautogui.typewrite(sentence)
    pyautogui.press("enter")