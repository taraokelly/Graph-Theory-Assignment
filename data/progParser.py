import xml.etree.ElementTree as ET
import csv

'''
Tara O'Kelly - G00322214,
Graph Theory Assignment,
Third Year, Graph Theory, Software Development.

A program to parse the xml file with data taken from http://timetable.gmit.ie/.

File name: 
    progCCAM.xml - progCCAM.csv
    progCE.xml - progCE.csv
    progCS.xml - progCS.csv
    progCA.xml -  progCA.csv
    progEE.xml - progEE.csv
    progHT.xml - progHT.csv
    progLPS.xml - progLPS.csv
    progMIE.xml - progMIE.csv
    progSI.xml - progSI.csv
    progSOB_AIS.xml - progSOB_AIS.csv
    progSOB_M.xml - progSOB_M.csv
    progEFDT.xml - progEFDT.csv
    progMayo.xml - progMayo.scv

'''

# adapted from https://docs.python.org/3/library/xml.etree.elementtree.html


out = csv.writer(open("programmes.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
dept = ["CCAM","CE","CS","CA","EE","HT","LPS","MIE","SI","SOB_AIS","SOB_M","EFDT", "Mayo"]
#dept = ["Centre for the Creative Arts and Media","Dept of Building and Civil Engineering","Dept of Computer Science & Applied Physics","Dept of Culinary Arts","Dept of Electronic and Electrical Engineering","Dept of Heritage and Tourism", "Dept of Life and Physical Sciences", "Dept of Mechanical and Industrial Engineering","Dept of Service Industries","Department of Accounting & Information Systems","Department of Management", "Letterfrack","Mayo"]
c = 0


for d in dept:
    print(d)
    tree = ET.parse("prog"+d+".xml")
    root = tree.getroot()

    headerRow = ["course", "code", "degree", "dept"]
    out.writerow(headerRow)

    for child in root:
        count = 0
        ss = ""
        row = []
        s = child.text.split(" ", 3)

        # course names that adhered to the common naming convention  
        if "BA" == s[1] or "BSc" == s[1] or s[1] == "BB" or s[1] == "BBs" or s[1] == "HDip" or s[1] == "HC" or s[1] == "BEng" or s[1] == "NCC" or s[1] == "MSc" or s[1] == "Certificate" or s[1] == "Assc" or s[1] == "BICT62":
            if s[2] == "in" or s[2] == "of":
                row = [s[3], s[0], s[1], d]
            else:
                row = [s[2] + " " + s[3], s[0], s[1], d]
        elif s[1] == "Bachelor": 
            s = child.text.split(" ", 5)
            if s[4] == "in":
                row = [s[5], s[0], s[1] + " " + s[2] +  " " + s[3],d]
            else:
                if s[4] == "L8":
                    row = [s[0] + " " + s[4] + " " + s[5], s[0], s[1] + " " + s[2] +  " " + s[3], d]
                else:
                    row = [s[4] + " " + s[5], s[0], s[1] + " " + s[2] +  " " + s[3], d]
        elif s[1] == "SPA" or s[1] == "Higher" or s[1] == "Advanced" or s[1] == "Prof" or s[1] == "Post":
            s = child.text.split(" ", 4)
            if s[3] == "in":
                row = [s[4], s[0], s[1] + " " + s[2],d]
            else:
                row = [s[3] + " " + s[4], s[0], s[1] + " " + s[2],d]   
        elif s[1] == "National":
            s = child.text.split(" ", 6)
            if s[5] == "in":
                row = [s[6], s[0], s[1] + " " + s[2] + " " + s[3]  + " " + s[4], d]
            else:
                row = [s[5] + " " + s[6], s[0], s[1] + " " + s[2] + " " + s[3]  + " " + s[4], d]
        # courses distinguished by groups (art students)
        elif s[1] == "Gr":
            s = child.text.split(" ", 5)
            if s[4] == "in":
                row = [s[5] + " " + s[1] + " " + s[2], s[0], s[3], d]
            else:
                row = [s[4] + " " + s[5] + " " + s[1] + " " + s[2], s[0], s[3], d]
        elif s[1] == "L8" or s[1] == "L7":
            row = [s[0], s[0], s[1] + " " + s[2] + " " + s[3], d]
        elif s[1] == "" :
            s = child.text.split(" ", 4)
            row = [s[4], s[0], s[2], d]
        elif s[1] == "Cons" :
            row = [s[3], s[0] + s[1], "SPA", d]
        # courses with no specified name
        else:
            for subs in s:
                if count == 1:
                    ss += subs
                if count > 1:
                    ss += " " + subs
                count += 1
            row = [ss, s[0], "Unknown", d]
        out.writerow(row) 
        c += 1   

'''
getInput = 0
filename = ""
dept = ""

while(getInput == 0):
    # Now ask for input
    user_input = input("Enter\n1- CCAM\n2- Building & Civil Engineering\n3- Computer Science & Applied Physics\n4- Culinary Arts\n5- Electronic & Electrical Engineering\n6- Heritage & Tourism\n7- Life & Physical Sciences\n8- Mechanical & Industrial Engineering\n9- Service Industries\n10- Accounting & Information Systems\n11- Management\n12- Letterfrack\n13- Mayo\n")

    # Now do something with the above
    if user_input == "1":
        print(user_input)
        filename = "progCCAM"
        dept = "Centre for the Creative Arts and Media"
        getInput = 1
    elif user_input == "2":
        print(user_input)
        filename = "progEE"
        dept = "Dept of Building and Civil Engineering"
        getInput = 1
    elif user_input == "3":
        print(user_input)
        filename = "progCS"
        dept = "Dept of Computer Science & Applied Physics"
        getInput = 1
    elif user_input == "4":
        print(user_input)
        filename = "progCA"
        dept = "Dept of Culinary Arts"
        getInput = 1
    elif user_input == "5":
        print(user_input)
        filename = "progEE"
        dept = "Dept of Electronic and Electrical Engineering"
        getInput = 1
    elif user_input == "6":
        print(user_input)
        filename = "progEE"
        dept = "Dept of Electronic and Electrical Engineering"
        getInput = 1 '''

'''tree = ET.parse('prog.xml')
root = tree.getroot()
out = csv.writer(open("programmes.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)

headerRow = ["course", "code", "degree", "dept"]
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
    out.writerow(row)    '''