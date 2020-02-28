LE = int ( input ("What's your LE grade? "))
PE = int ( input ("What's your PE grade? "))
RE = int ( input ("What's your RE grade? "))
TE = int ( input ("What's your TE grade? "))
grade = (LE + RE + 4*PE + 4*TE)/50
output = int(grade)
for x in [LE,PE,TE,RE]:
    if x<0 or x>100:
        output = "Input error"
if RE<40 or PE<40:
    output = "RFC"
print(output)