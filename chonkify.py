import re
import random

def chance(p):
  return True if random.random() < p else False

class Chonkify:
  def __init__(self,struggle=0.5,lisp=1,stutter=0.33,slur=0,vowels=0,eating=0,gas=False,extragas=0):
    self.struggle = struggle
    self.lisp = lisp
    self.stutter = stutter
    self.slur = slur
    self.vowels = vowels
    self.eating = eating
    self.extragas = extragas
    self.glist = ['...*bworrRPPpp*...', '...*ouurRRPp*...', '...*urrrp*...']
    self.slist = [
      '...*wheeze*...', '...*huff*...', '...*puff*...', '...*groan*...',
      '...*whimper*...', '...*gasp*...', '...*mmpphhff*...', '...*nggnhh*...',
      '...*hahhh*...', '...*aaahhh*...', '...*hrrngh*...', '...'
    ]
    self.elist = [
      '*hOMf*', '*nom*', '*munch*', '*gulp*', '*slurp*', '*chomp*',
      '*snarf*', '*crunch*', '*nomnom*', '*mnchmnch*', '*hOMnomnom*',
      '*crnchcrch*', '*omnomnom*'
    ]
    if gas: self.slist.extend(self.glist)

  def chonkify(self,input):
    words = input.split(' ')
    newstr = ''
    for index,word in enumerate(words):
      if chance(self.lisp):
        word = re.sub(r"s", "sh", word)
        word = re.sub(r"t$", "\'tsh", word)
        word = re.sub(r"the(.)", r"de\1", word)
        word = re.sub(r"The(.)", r"De\1", word)
        word = re.sub(r"s$", "sh", word)
      if len(word) > 1 and chance(self.stutter):
        word = word[0] + '-' + word[0] + word[1:]
      if chance(self.slur):
        word = re.sub(r"\b([Mm])y\b", r"\1uh", word)
        word = re.sub(r"([aeiou]+)", r"\1h", word)
      if chance(self.vowels):
        word = re.sub(r"([aeiou])", r"\1\1", word, flags=re.I)
      if len(word) > 2 and chance(self.extragas):
        sp = int(random.random() * (len(word) - 1)) + 1
        word = word[:sp-1] + self.glist[int(random.random() * len(self.glist))] + word[sp-1:]
      newstr += word + ' '
      if index < len(words)-1:
        if chance(self.eating):
          newstr += self.elist[int(random.random() * len(self.elist))] + " "
        if chance(self.struggle):
          newstr += self.slist[int(random.random() * len(self.slist))] + " "
    return newstr.strip()
