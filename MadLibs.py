import time
company_name = input("whats your companys name: ")
adj1 = input("choose an adjective ")
adj2 = input("choose another ")
adj3 = input("and another ")
clothing = input("choose a type of clothing ")
adj4 = input("hey look another adjective ")
adj5 = input("and another one ")
bodypart = input("now choose a body part ")
Verb1 = input("choose a verb ")
verb2 = input("another verb ")
noun = input("choose a noun ")
adj6 = input("choose an adjective ")
adj7 = input("and another ")
bodypart2 = input("choose a body part ")
noun2 = input("choose another noun ")
noun3 = input("another noun ")
plrn = input("mixing it up a bit with a plural noun ")
plrn2 = input("hey another plural noun ")
adj8 = input("yet another adjective ")
noun4 = input("another noun ")
verbing = input("now a verb ending in 'ing' ")
plrn3 = input("another plural noun ")
verb4 = input("and finally the last one, a verb ")
a = input("jk heres another noun ")
print("adding your words...")
print()
print()
word = ['a', 'an']
wordlist = []
wordlist.append(a)
print(wordlist[0][0])
vowel1 = "a"
vowel2 = "e"
vowel3 = "i"
vowel4 = "o"
vowel5 = "u"
print()
def lookatvowels(x):
    if a[0][0] == str(vowel1) or str(vowel2) or str(vowel3) or str(vowel4) or str(vowel5):
        print(word[1])
    else:
        print(word[0])
print(lookatvowels(word))
time.sleep(5)
print("Congratulations! You finally managed to get a job interview at %s. Follow these a steps and you'll be %s for sure!" % (company_name.title(), adj1))
print("1  Make sure you dress appropriately. You should probably wear something like a %s" % (clothing))
print("Make sure its not too %s or %s. Prospective employers do not like to see too much %s." % (adj2, adj3, adj4))
print("2  Be sure to %s and %s your %s before the interview. Make sure your breath is %s" % (Verb1, noun, adj5, adj8))
print("3  Smile, be %s and remember a firm hand shake is always %s %s" % (adj6, lookatvowels(word), a))
print("4  Make sure to mention such topics as %s, %s and %s." % (noun2, noun3, plrn))
print("Be sure to avoid talking about %s They might get the wrong impression and think you are too %s." % (plrn2, adj7))
print("5  You may want to compliment your potential boss on his her %s and mention how much you enjoyed %s with them." % (noun4, verbing))
print("6  Get plenty of %s the night before the interview and don't %s too much and you will do fine!" % (plrn3, verb4))
