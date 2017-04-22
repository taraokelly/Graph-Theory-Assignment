import xml.etree.ElementTree as ET
import csv

'''
Tara O'Kelly - G00322214,
Graph Theory Assignment,
Third Year, Graph Theory, Software Development.

A program to parse the xml file with data taken from http://timetable.gmit.ie/.

'''

# adapted from https://docs.python.org/3/library/xml.etree.elementtree.html

tree = ET.parse('prog.xml')
root = tree.getroot()
out = csv.writer(open("programmes.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)

headerRow = ["course", "code", "degree"]
out.writerow(headerRow)

for child in root:
    count = 0
    ss = ""
    row = []
    s = child.text.split(" ", 3)

    # course names that adhered to the common naming convention  
    if "BA" == s[1] or "BSc" == s[1] or s[1] == "BB" or s[1] == "BBs" or s[1] == "HDip" or s[1] == "HC" or s[1] == "BEng" or s[1] == "NCC" or s[1] == "MSc" or s[1] == "Certificate" or s[1] == "Assc" or s[1] == "BICT62":
        if s[2] == "in" or s[2] == "of":
            row = [s[3], s[0], s[1]]
        else:
            row = [s[2] + " " + s[3], s[0], s[1]]
    elif s[1] == "Bachelor": 
        s = child.text.split(" ", 5)
        if s[4] == "in":
            row = [s[5], s[0], s[1] + " " + s[2] +  " " + s[3]]
        else:
            if s[4] == "L8":
                row = [s[0] + " " + s[4] + " " + s[5], s[0], s[1] + " " + s[2] +  " " + s[3]]
            else:
                row = [s[4] + " " + s[5], s[0], s[1] + " " + s[2] +  " " + s[3]]
    elif s[1] == "SPA" or s[1] == "Higher" or s[1] == "Advanced" or s[1] == "Prof" or s[1] == "Post":
        s = child.text.split(" ", 4)
        if s[3] == "in":
            row = [s[4], s[0], s[1] + " " + s[2]]
        else:
            row = [s[3] + " " + s[4], s[0], s[1] + " " + s[2]]   
    elif s[1] == "National":
        s = child.text.split(" ", 6)
        if s[5] == "in":
            row = [s[6], s[0], s[1] + " " + s[2] + " " + s[3]  + " " + s[4]]
        else:
           row = [s[5] + " " + s[6], s[0], s[1] + " " + s[2] + " " + s[3]  + " " + s[4]]
    # courses distinguished by groups (art students)
    elif s[1] == "Gr":
        s = child.text.split(" ", 5)
        if s[4] == "in":
            row = [s[5] + " " + s[1] + " " + s[2], s[0], s[3]]
        else:
            row = [s[4] + " " + s[5] + " " + s[1] + " " + s[2], s[0], s[3]]
    elif s[1] == "L8" or s[1] == "L7":
        row = [s[0], s[0], s[1] + " " + s[2] + " " + s[3]]
    elif s[1] == "" :
        s = child.text.split(" ", 4)
        row = [s[4], s[0], s[2]]
    elif s[1] == "Cons" :
        row = [s[3], s[0] + s[1], "SPA"]
    # courses with no specified name
    else:
        for subs in s:
            if count == 1:
                ss += subs
            if count > 1:
                ss += " " + subs
            count += 1
        row = [ss, s[0], "Unknown"]
    out.writerow(row)    