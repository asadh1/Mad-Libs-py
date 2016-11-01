# -*- coding: utf-8 -*-

import pwd

# Functions
def getTxt(file_path):
  # Read from file:
  file = open(file_path)
  data = file.readlines()
  file.close()

  # Replace '\xe2\x80\x94' with '-'
  if "\xe2\x80\x94" in data[0]:
    data[0] = data[0].replace("\xe2\x80\x94", "-")
  
  return data[0]

# Word types and word type Dict
wordTypes = ["{ADJECTIVE}", "{NOUN}", "{NOUN_2}", "{VERB}", "{VERB_2}", "{PIR}", "{PLACE}", "{CEL}", "{ANI}", "{FOOD}", "{GAME}"]
word_dict = {"{ADJECTIVE}": "Adjective", "{NOUN}": "Noun", "{NOUN_2}": "Plural Noun", "{VERB}": "Verb", "{VERB_2}": "Verb Ending With -ing", "{PIR}": "Person In Room", "{PLACE}": "Place", "{CEL}": "Celebrity", "{ANI}": "Animal", "{FOOD}": "Food", "{GAME}": "Game"}

# Mad_libs class
class Mad_libs():
  title = ""
  path = ""
  def __init__(self, title, path):
    self.title = title
    self.path = path
  def start_game(self):
    print("MAD LIBS IN PYTHON: {}".format(self.title))
    data = getTxt(self.path)
    # Replace word types
    for type in wordTypes:
      # Replacing linking words
      link_num = 1
      linking_type = "{} link:".format(type[:len(type) - 1])
      while linking_type in data:
        data = data.replace("{}{}{}".format(linking_type, link_num, "}"), raw_input("{}: ".format(word_dict[type])))
        link_num += 1
        continue
      # Replacing regular words
      while type in data:
        data = data.replace(type, raw_input("{}: ".format(word_dict[type])), 1)
        continue
    print(data)

_taoe = Mad_libs("The Art Of Espionage", "/Users/{}/Downloads/Mad-Libs-py-master/madlibs_str.txt".format(pwd.getpwuid(os.getuid())[0]))

_iyga = Mad_libs("If You Give A •••", "/Users/{}/Downloads/Mad-Libs-py-master/madlibs_str2.txt".format(pwd.getpwuid(os.getuid())[0]))
_iyga.start_game()
