x = 0
while x < 10: 
  print("Hodnota x je:", x)
  x -= 1
print("Konec")

for kamarad in ["Adam", "Bert", "Cyril"]:
  print("Můj kamarád je:",kamarad)
  if kamarad == "Bert":
    break
print("Konec")

for kamarad in ["Adam", "Bert", "Cyril", "Dan", "Emil"]:
  if kamarad == "Bert":
    continue
  
  print("Můj kamarád je:",kamarad)
  
  if kamarad == "Dan":
    break
print("Konec")