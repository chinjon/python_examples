import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
  "class %%%{%%%}:
    "Make a class named %%% that is -a %%%."
  "class %%%{object}:\n\tdef __init__{self, ***}:
    "class %%% has-a __init__ that takes self and *** params.",
  "class %%%{object}:\m\tdef ***{self, @@@}":
    "class %%% has-a function *** that takes self and @@@ params.",
  "*** = %%%{}":
    "Set *** to an instance of class %%%",
  "***.*** (@@@)":
    "From *** get the *** function, call it with params self, @@@.",
  "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
}

if len(sys.argv) == 2 and sys.argv[1] == "english"
