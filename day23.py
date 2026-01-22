#else statement

light = "yellow"

if(light == "red"):
    print("STOP")

elif(light == "green"):
    print("GO")

elif(light == "yellow"):
    print("SLOW DOWN")

else:
    print("LIGHT IS BROKEN") # it only works when both the statements(if & elif) are false.