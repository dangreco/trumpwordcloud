i = [
  'rt:',
  'https',
  '@',
  'trump',
  'president',
  'amp'
]

d = [
  'trump',
  "say",
  "new",
  "want",
  "trump's",
  'donald',
  'why',
  'i',
  'a',
  'the',
  'how',
  'when',
  'where',
  'what',
  'who',
  'to',
  'of',
  'so',
  'them',
  'you',
  'him',
  'but',
  'his',
  'will',
  'now',
  'via',
  'amp'
]

def excludeWord(s):
  if isinstance(s, unicode):
    return True
  if len(s) <= 2:
    return True
  for word in i:
    if word in s:
      return True
  for word in d:
    if word == s:
      return True
  return False
