formatter="%s %s %s %s"

print(formatter % (1,2,3,4))
print(formatter % ("one","two","three","four"))
print(formatter % ("true","false","false","true"))
print(formatter % (formatter,formatter,formatter,formatter))
print(formatter % 
   ( " i had this thing.",
     " that you could type up right.",
     " but it didnt sing.",
     " so i said goodnight."))  