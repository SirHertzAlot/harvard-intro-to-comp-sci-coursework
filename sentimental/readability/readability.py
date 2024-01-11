import math

words = 0
chars = 0
sent = 0

val = input("Text: ")

sent += val.count(".") + val.count("!") + val.count("?")
words += len(val.split())

for i in val:
  chars += len(i.split())

chars -= sent

l = float(chars) / float(words) * 100
s = float(sent) / float(words) * 100

index = math.floor(0.0588 * l - 0.296 * s - 15.8)

if(index < 1):
  print("Before Grade 1");
elif(index > 16):
  print("Grade 16+");
else:
  print("Grade " + str(int(index)))
