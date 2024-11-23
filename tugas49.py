print("="*30)
print("TEKA TEKI ")
print("="*30)

number = 23

gues = int(input("Enter an integer : "))
if gues == number :
     print("Congratulations,you guessed it.")
     print("But you do not win any prize!")
elif gues < number :
     print("No, it is a little higher than that. ")
else:
     print("No, it is a little lower than that")

print("Done")