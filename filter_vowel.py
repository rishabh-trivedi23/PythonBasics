s = "onomatopoeia"
a = ['a','e', 'i','o','u']

def filter_vowel(s):
  new_str = s
  for i in s.lower():
    if i in a:
      new_str = new_str.replace(i,"")
  return new_str 

def filter_consonent(s):
  new_str = ""
  for i in s.lower():
    if i in a:
      new_str = new_str+i
  return new_str

vowel = filter_consonent(s)
consonent = filter_vowel(s)
print(vowel, consonent)