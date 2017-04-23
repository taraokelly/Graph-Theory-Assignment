# Graph-Theory-Assignment
*Database designed with neo4j for the GMIT timetabling system. Third Year, Graph Theory, Software Development.*

## Introduction

Project spec: 

> "The following document contains the instructions for Project 2017 for Graph
> Theory. You are required to design and prototype a Neo4j [2] database for use
> in a timetabling system for a third level institute like GMIT. The database
> should store information about student groups, classrooms, lecturers, and
> work hours – just like the currently used timetabling system at GMIT [1].

I focused mainly on implementing a scalable DB. I designed it to accommodate the academic year; each year has to be unique and is the root node of each year. I designed a template to build the bones of the year; two semesters, with days, timeslots, rooms, courses in each. 

## Technolgies

- Neo4j: The World’s Leading Graph Database. Version - 3.1.

- Python3: Utilized etree library to parse element data.

## Database Design

### First Draft:

```
CREATE (year:Academic_Yr {name: "2017"}), 
(dept:Dept {name:"Galway Campus - Dept of Computer Science & Applied Physics"}), 
(course:Course {name:"Software Development L7 Y3"}), (group :Group {name:"C"}), 
(lect:Lecturer {name:"Ian McLoughlin"}), (mod:Module {name:"Graph Theory"}), 
(room:Room {name:"1000"}), (time:Time {name:"09:00"}), (day:Day {name:"Monday"}), 
(year)-[:SEM_2]->(dept), (dept)-[:HAS]->(course), (dept)-[:HAS]->(lect), 
(course)-[:GROUP]->(group), (group)-[:ATTENDING]->(mod), 
(lect)-[:LECTURING]->(mod), (mod)-[:IN]->(room), (room)-[:AT]->(time),
(time)-[:ON]->(day);
```

![alt text](https://github.com/taraokelly/Graph-Theory-Assignment/blob/master/img/v1.PNG "v0.0.1")

__*N.B. This draft's data is not accurate, just used for testing/demonstrational purposes. Real data will be entered for the finished assignment.*__

- (2017)-[:SEM_3]->(Software Development L7 Y3)-[:HAS]->(Software Development L7 Y3)-[:GROUP]->(C)-[:ATTENDING]->(Graph Theory)-[:IN]->(1000)-[:AT]->(09:00)-[:ON]->(Monday)

- 2017, SEMESTER 3, Software Development L7 Y3 HAS Software Development L7 Y3 GROUP C ATTENDING Graph Theory IN 1000 AT 9:00 ON Monday.

### Second Draft:

In the first draft of the DB design, the room, time, and day nodes had nothing directly assigned to them to distinguish what year and semester it was assigned to. This would have be adequate if it were not for the inability to search for a room's availabilty, the overall available rooms or what module has been assigned to a specific room and time slot.

```
CREATE (year:Academic_Yr {name: "2017"}), 
(dept:Dept {name:"Galway Campus - Dept of Computer Science & Applied Physics"}), 
(course:Course {name:"Software Development L7 Y3"}), (group :Group {name:"C"}), 
(lect:Lecturer {name:"Ian McLoughlin"}), (mod:Module {name:"Graph Theory"}), 
(room:Room {name:"1000"}), (time:Time {name:"09:00"}), (day:Day {name:"Monday"}), 
(year)-[:SEM_2]->(dept), (dept)-[:HAS]->(course), (dept)-[:HAS]->(lect), 
(course)-[:GROUP]->(group), (group)-[:ATTENDING]->(mod), 
(lect)-[:LECTURING]->(mod), (mod)-[:IN]->(room), (room)-[:AT]->(time),
(time)-[:ON]->(day), (year)-[:SEM_2]->(room);
```

![alt text](https://github.com/taraokelly/Graph-Theory-Assignment/blob/master/img/v2.PNG "v0.0.2")

__*N.B. This draft's data is not accurate, just used for testing/demonstrational purposes. Real data will be entered for the finished assignment.*__

### Third Draft:

The second draft's time and day nodes were still not distinguishable in terms of what year and semester it was related to. With the room node coming first, there would there would have to be seperate time slots for each room and seperate days for each time slot. Relative to these three node types, with the quantity of the the rooms being the largest, and the quantity of the time slots being the second largest, this design seemed inefficient.

```
CREATE (year:Academic_Yr {name: "2017"}), 
(dept:Dept {name:"Galway Campus - Dept of Computer Science & Applied Physics"}), 
(course:Course {name:"Software Development L7 Y3"}), (group :Group {name:"C"}), 
(lect:Lecturer {name:"Ian McLoughlin"}), (mod:Module {name:"Graph Theory"}), 
(room:Room {name:"1000"}), (time:Time {name:"09:00"}), (day:Day {name:"Monday"}), 
(year)-[:SEM_2]->(dept), (dept)-[:HAS]->(course), (dept)-[:HAS]->(lect), 
(course)-[:GROUP]->(group), (group)-[:ATTENDING]->(mod), (lect)-[:LECTURING]->(mod), 
(mod)-[:ON]->(day), (day)-[:AT]->(time),(time)-[:IN]->(room), (year)-[:SEM_2]->(day);
```

![alt text](https://github.com/taraokelly/Graph-Theory-Assignment/blob/master/img/v3.PNG "v0.0.3")

### Final Draft:

The room nodes were still causing difficulty being so large, I decided not to implement it the way I had desired: a room for every time slot, and those timeslots would each belong to seperate days. I felt as though it would be too bulky, with the size of the rooms being increased by the number of days(5) and of timeslots(12)(*60 altogether). I did not directly connect the room nodes to the root node, as I perhaps should have since they are now not connected to the time or day nodes, but have properties to define them to their year and semester, and a unique constaint to avaid duplicates. 

The following graph has been taken from the finished DB. 

![alt text](https://github.com/taraokelly/Graph-Theory-Assignment/blob/master/img/v4.PNG "v0.0.4")

__*N.B. This draft's data is not accurate, just used for testing/demonstrational purposes. Real data will be entered for the finished assignment.*__


## Setting Up Database

### Creating Constraints and Indexes:

Create constraint for the Academic_Yr node (this also creates an index).
 
```
CREATE CONSTRAINT ON (a:Academic_Yr) ASSERT a.name IS UNIQUE;
CREATE CONSTRAINT ON (r:Room) ASSERT a.name IS UNIQUE;
```

Create indexes.

```
CREATE INDEX ON :Dept(name);
CREATE INDEX ON :Course(name);
CREATE INDEX ON :Group(name);
CREATE INDEX ON :Lecture(name);
CREATE INDEX ON :Module(name);
CREATE INDEX ON :Time(name);
CREATE INDEX ON :Day(name);
```

### Creating Year Template:

The following can be modified to add other years in the database; simply change the first line to the desired year: "CREATE (year:Academic_Yr {name: "x"})". Please note that the same year cannot be entered twice.

Start with creating the academic year, adding the days and departments, and creating the necessary relationships between them for each semester. Then add the the times to each day.
 
```
CREATE (year:Academic_Yr {name: "2017"}), (mon1:Day {name:"Monday"}),
(tue1:Day {name:"Tuesday"}), (wed1:Day {name:"Wednesday"}),
(thu1:Day {name:"Thursday"}), (fri1:Day {name:"Friday"}),
(mon2:Day {name:"Monday"}), (tue2:Day {name:"Tuesday"}),
(wed2:Day {name:"Wednesday"}), (thu2:Day {name:"Thursday"}), 
(fri2:Day {name:"Friday"}),
(d1s1:Dept {name:"Centre for the Creative Arts and Media", campus:"Galway"}),
(d2s1:Dept {name:"Dept of Building and Civil Engineering", campus:"Galway"}), 
(d3s1:Dept {name:"Dept of Computer Science & Applied Physics", campus:"Galway"}), 
(d4s1:Dept {name:"Dept of Culinary Arts", campus:"Galway"}), 
(d5s1:Dept {name:"Dept of Electronic and Electrical Engineering", campus:"Galway"}), 
(d6s1:Dept {name:"Dept of Heritage and Tourism", campus:"Galway"}), 
(d7s1:Dept {name:"Dept of Life and Physical Sciences", campus:"Galway"}), 
(d8s1:Dept {name:"Dept of Mechanical and Industrial Engineering", campus:"Galway"}), 
(d9s1:Dept {name:"Dept of Service Industries", campus:"Galway"}), 
(d10s1:Dept {name:"School of Business - Department of Accounting & Information Systems", campus:"Galway"}), 
(d11s1:Dept {name:"School of Business - Department of Management", campus:"Galway"}),
(d12s1:Dept {name:"National Centre for Excellence in Furniture Design and Technology", campus:"Letterfrack"}), 
(d13s1:Dept {name:"Mayo Campus", campus:"Mayo"}),
(d1s2:Dept {name:"Centre for the Creative Arts and Media", campus:"Galway"}),
(d2s2:Dept {name:"Dept of Building and Civil Engineering", campus:"Galway"}), 
(d3s2:Dept {name:"Dept of Computer Science & Applied Physics", campus:"Galway"}), 
(d4s2:Dept {name:"Dept of Culinary Arts", campus:"Galway"}), 
(d5s2:Dept {name:"Dept of Electronic and Electrical Engineering", campus:"Galway"}), 
(d6s2:Dept {name:"Dept of Heritage and Tourism", campus:"Galway"}), 
(d7s2:Dept {name:"Dept of Life and Physical Sciences", campus:"Galway"}), 
(d8s2:Dept {name:"Dept of Mechanical and Industrial Engineering", campus:"Galway"}), 
(d9s2:Dept {name:"Dept of Service Industries", campus:"Galway"}), 
(d10s2:Dept {name:"School of Business - Department of Accounting & Information Systems", campus:"Galway"}), 
(d11s2:Dept {name:"School of Business - Department of Management", campus:"Galway"}),
(d12s2:Dept {name:"National Centre for Excellence in Furniture Design and Technology", campus:"Letterfrack"}), 
(d13s2:Dept {name:"Mayo Campus", campus:"Mayo"}),
(mon1t1:Time {name: "09.00"}), (mon1t2:Time {name: "10.00"}), 
(mon1t3:Time {name: "11.00"}), (mon1t4:Time {name: "12.00"}), 
(mon1t5:Time {name: "13.00"}), (mon1t6:Time {name: "14.00"}),
(mon1t7:Time {name: "15.00"}), (mon1t8:Time {name: "16.00"}),
(mon1t9:Time {name: "17.00"}), (mon1t10:Time {name: "18.00"}),
(mon1t11:Time {name: "19.00"}), (mon1t12:Time {name: "20.00"}),
(mon1t13:Time {name: "21.00"}),
(tue1t1:Time {name: "09.00"}), (tue1t2:Time {name: "10.00"}), 
(tue1t3:Time {name: "11.00"}), (tue1t4:Time {name: "12.00"}), 
(tue1t5:Time {name: "13.00"}), (tue1t6:Time {name: "14.00"}),
(tue1t7:Time {name: "15.00"}), (tue1t8:Time {name: "16.00"}),
(tue1t9:Time {name: "17.00"}), (tue1t10:Time {name: "18.00"}),
(tue1t11:Time {name: "19.00"}), (tue1t12:Time {name: "20.00"}),
(tue1t13:Time {name: "21.00"}),
(wed1t1:Time {name: "09.00"}), (wed1t2:Time {name: "10.00"}), 
(wed1t3:Time {name: "11.00"}), (wed1t4:Time {name: "12.00"}), 
(wed1t5:Time {name: "13.00"}), (wed1t6:Time {name: "14.00"}),
(wed1t7:Time {name: "15.00"}), (wed1t8:Time {name: "16.00"}),
(wed1t9:Time {name: "17.00"}), (wed1t10:Time {name: "18.00"}),
(wed1t11:Time {name: "19.00"}), (wed1t12:Time {name: "20.00"}),
(wed1t13:Time {name: "21.00"}),
(thu1t1:Time {name: "09.00"}), (thu1t2:Time {name: "10.00"}), 
(thu1t3:Time {name: "11.00"}), (thu1t4:Time {name: "12.00"}), 
(thu1t5:Time {name: "13.00"}), (thu1t6:Time {name: "14.00"}),
(thu1t7:Time {name: "15.00"}), (thu1t8:Time {name: "16.00"}),
(thu1t9:Time {name: "17.00"}), (thu1t10:Time {name: "18.00"}),
(thu1t11:Time {name: "19.00"}), (thu1t12:Time {name: "20.00"}),
(thu1t13:Time {name: "21.00"}),
(fri1t1:Time {name: "09.00"}), (fri1t2:Time {name: "10.00"}), 
(fri1t3:Time {name: "11.00"}), (fri1t4:Time {name: "12.00"}), 
(fri1t5:Time {name: "13.00"}), (fri1t6:Time {name: "14.00"}),
(fri1t7:Time {name: "15.00"}), (fri1t8:Time {name: "16.00"}),
(fri1t9:Time {name: "17.00"}), (fri1t10:Time {name: "18.00"}),
(fri1t11:Time {name: "19.00"}), (fri1t12:Time {name: "20.00"}),
(fri1t13:Time {name: "21.00"}),
(mon2t1:Time {name: "09.00"}), (mon2t2:Time {name: "10.00"}), 
(mon2t3:Time {name: "11.00"}), (mon2t4:Time {name: "12.00"}), 
(mon2t5:Time {name: "13.00"}), (mon2t6:Time {name: "14.00"}),
(mon2t7:Time {name: "15.00"}), (mon2t8:Time {name: "16.00"}),
(mon2t9:Time {name: "17.00"}), (mon2t10:Time {name: "18.00"}),
(mon2t11:Time {name: "19.00"}), (mon2t12:Time {name: "20.00"}),
(mon2t13:Time {name: "21.00"}),
(tue2t1:Time {name: "09.00"}), (tue2t2:Time {name: "10.00"}), 
(tue2t3:Time {name: "11.00"}), (tue2t4:Time {name: "12.00"}), 
(tue2t5:Time {name: "13.00"}), (tue2t6:Time {name: "14.00"}),
(tue2t7:Time {name: "15.00"}), (tue2t8:Time {name: "16.00"}),
(tue2t9:Time {name: "17.00"}), (tue2t10:Time {name: "18.00"}),
(tue2t11:Time {name: "19.00"}), (tue2t12:Time {name: "20.00"}),
(tue2t13:Time {name: "21.00"}),
(wed2t1:Time {name: "09.00"}), (wed2t2:Time {name: "10.00"}), 
(wed2t3:Time {name: "11.00"}), (wed2t4:Time {name: "12.00"}), 
(wed2t5:Time {name: "13.00"}), (wed2t6:Time {name: "14.00"}),
(wed2t7:Time {name: "15.00"}), (wed2t8:Time {name: "16.00"}),
(wed2t9:Time {name: "17.00"}), (wed2t10:Time {name: "18.00"}),
(wed2t11:Time {name: "19.00"}), (wed2t12:Time {name: "20.00"}),
(wed2t13:Time {name: "21.00"}),
(thu2t1:Time {name: "09.00"}), (thu2t2:Time {name: "10.00"}), 
(thu2t3:Time {name: "11.00"}), (thu2t4:Time {name: "12.00"}), 
(thu2t5:Time {name: "13.00"}), (thu2t6:Time {name: "14.00"}),
(thu2t7:Time {name: "15.00"}), (thu2t8:Time {name: "16.00"}),
(thu2t9:Time {name: "17.00"}), (thu2t10:Time {name: "18.00"}),
(thu2t11:Time {name: "19.00"}), (thu2t12:Time {name: "20.00"}),
(thu2t13:Time {name: "21.00"}),
(fri2t1:Time {name: "09.00"}), (fri2t2:Time {name: "10.00"}), 
(fri2t3:Time {name: "11.00"}), (fri2t4:Time {name: "12.00"}), 
(fri2t5:Time {name: "13.00"}), (fri2t6:Time {name: "14.00"}),
(fri2t7:Time {name: "15.00"}), (fri2t8:Time {name: "16.00"}),
(fri2t9:Time {name: "17.00"}), (fri2t10:Time {name: "18.00"}),
(fri2t11:Time {name: "19.00"}), (fri2t12:Time {name: "20.00"}),
(fri2t13:Time {name: "21.00"}),
(year)-[:SEM_1]->(mon1),(year)-[:SEM_1]->(tue1),  
(year)-[:SEM_1]->(wed1), (year)-[:SEM_1]->(thu1), 
(year)-[:SEM_1]->(fri1), (year)-[:SEM_2]->(mon2), 
(year)-[:SEM_2]->(tue2), (year)-[:SEM_2]->(wed2), 
(year)-[:SEM_2]->(thu2), (year)-[:SEM_2]->(fri2),
(year)-[:SEM_1]->(d1s1), (year)-[:SEM_1]->(d2s1), 
(year)-[:SEM_1]->(d3s1), (year)-[:SEM_1]->(d4s1), 
(year)-[:SEM_1]->(d5s1), (year)-[:SEM_1]->(d6s1),
(year)-[:SEM_1]->(d7s1), (year)-[:SEM_1]->(d8s1), 
(year)-[:SEM_1]->(d9s1), (year)-[:SEM_1]->(d10s1), 
(year)-[:SEM_1]->(d11s1), (year)-[:SEM_1]->(d12s1),
(year)-[:SEM_1]->(d13s1),
(year)-[:SEM_2]->(thu2), (year)-[:SEM_2]->(fri2),
(year)-[:SEM_2]->(d1s2), (year)-[:SEM_2]->(d2s2), 
(year)-[:SEM_2]->(d3s2), (year)-[:SEM_2]->(d4s2), 
(year)-[:SEM_2]->(d5s2), (year)-[:SEM_2]->(d6s2),
(year)-[:SEM_2]->(d7s2), (year)-[:SEM_2]->(d8s2), 
(year)-[:SEM_2]->(d9s2), (year)-[:SEM_2]->(d10s2), 
(year)-[:SEM_2]->(d11s2), (year)-[:SEM_2]->(d12s2),
(year)-[:SEM_2]->(d13s2),
(mon1)-[:AT]->(mon1t1), (mon1)-[:AT]->(mon1t2),
(mon1)-[:AT]->(mon1t3), (mon1)-[:AT]->(mon1t4),
(mon1)-[:AT]->(mon1t5), (mon1)-[:AT]->(mon1t6),
(mon1)-[:AT]->(mon1t7), (mon1)-[:AT]->(mon1t8),
(mon1)-[:AT]->(mon1t9), (mon1)-[:AT]->(mon1t10),
(mon1)-[:AT]->(mon1t11), (mon1)-[:AT]->(mon1t12),
(mon1)-[:AT]->(mon1t13),
(tue1)-[:AT]->(tue1t1), (tue1)-[:AT]->(tue1t2),
(tue1)-[:AT]->(tue1t3), (tue1)-[:AT]->(tue1t4),
(tue1)-[:AT]->(tue1t5), (tue1)-[:AT]->(tue1t6),
(tue1)-[:AT]->(tue1t7), (tue1)-[:AT]->(tue1t8),
(tue1)-[:AT]->(tue1t9), (tue1)-[:AT]->(tue1t10),
(tue1)-[:AT]->(tue1t11), (tue1)-[:AT]->(tue1t12),
(tue1)-[:AT]->(tue1t13),
(wed1)-[:AT]->(wed1t1), (wed1)-[:AT]->(wed1t2),
(wed1)-[:AT]->(wed1t3), (wed1)-[:AT]->(wed1t4),
(wed1)-[:AT]->(wed1t5), (wed1)-[:AT]->(wed1t6),
(wed1)-[:AT]->(wed1t7), (wed1)-[:AT]->(wed1t8),
(wed1)-[:AT]->(wed1t9), (wed1)-[:AT]->(wed1t10),
(wed1)-[:AT]->(wed1t11), (wed1)-[:AT]->(wed1t12),
(wed1)-[:AT]->(wed1t13),
(thu1)-[:AT]->(thu1t1), (thu1)-[:AT]->(thu1t2),
(thu1)-[:AT]->(thu1t3), (thu1)-[:AT]->(thu1t4),
(thu1)-[:AT]->(thu1t5), (thu1)-[:AT]->(thu1t6),
(thu1)-[:AT]->(thu1t7), (thu1)-[:AT]->(thu1t8),
(thu1)-[:AT]->(thu1t9), (thu1)-[:AT]->(thu1t10),
(thu1)-[:AT]->(thu1t11), (thu1)-[:AT]->(thu1t12),
(thu1)-[:AT]->(thu1t13),
(fri1)-[:AT]->(fri1t1), (fri1)-[:AT]->(fri1t2),
(fri1)-[:AT]->(fri1t3), (fri1)-[:AT]->(fri1t4),
(fri1)-[:AT]->(fri1t5), (fri1)-[:AT]->(fri1t6),
(fri1)-[:AT]->(fri1t7), (fri1)-[:AT]->(fri1t8),
(fri1)-[:AT]->(fri1t9), (fri1)-[:AT]->(fri1t10),
(fri1)-[:AT]->(fri1t11), (fri1)-[:AT]->(fri1t12),
(fri1)-[:AT]->(fri1t13),
(mon2)-[:AT]->(mon2t1), (mon2)-[:AT]->(mon2t2),
(mon2)-[:AT]->(mon2t3), (mon2)-[:AT]->(mon2t4),
(mon2)-[:AT]->(mon2t5), (mon2)-[:AT]->(mon2t6),
(mon2)-[:AT]->(mon2t7), (mon2)-[:AT]->(mon2t8),
(mon2)-[:AT]->(mon2t9), (mon2)-[:AT]->(mon2t10),
(mon2)-[:AT]->(mon2t11), (mon2)-[:AT]->(mon2t12),
(mon2)-[:AT]->(mon2t13),
(tue2)-[:AT]->(tue2t1), (tue2)-[:AT]->(tue2t2),
(tue2)-[:AT]->(tue2t3), (tue2)-[:AT]->(tue2t4),
(tue2)-[:AT]->(tue2t5), (tue2)-[:AT]->(tue2t6),
(tue2)-[:AT]->(tue2t7), (tue2)-[:AT]->(tue2t8),
(tue2)-[:AT]->(tue2t9), (tue2)-[:AT]->(tue2t10),
(tue2)-[:AT]->(tue2t11), (tue2)-[:AT]->(tue2t12),
(tue2)-[:AT]->(tue2t13),
(wed2)-[:AT]->(wed2t1), (wed2)-[:AT]->(wed2t2),
(wed2)-[:AT]->(wed2t3), (wed2)-[:AT]->(wed2t4),
(wed2)-[:AT]->(wed2t5), (wed2)-[:AT]->(wed2t6),
(wed2)-[:AT]->(wed2t7), (wed2)-[:AT]->(wed2t8),
(wed2)-[:AT]->(wed2t9), (wed2)-[:AT]->(wed2t10),
(wed2)-[:AT]->(wed2t11), (wed2)-[:AT]->(wed2t12),
(wed2)-[:AT]->(wed2t13),
(thu2)-[:AT]->(thu2t1), (thu2)-[:AT]->(thu2t2),
(thu2)-[:AT]->(thu2t3), (thu2)-[:AT]->(thu2t4),
(thu2)-[:AT]->(thu2t5), (thu2)-[:AT]->(thu2t6),
(thu2)-[:AT]->(thu2t7), (thu2)-[:AT]->(thu2t8),
(thu2)-[:AT]->(thu2t9), (thu2)-[:AT]->(thu2t10),
(thu2)-[:AT]->(thu2t11), (thu2)-[:AT]->(thu2t12),
(thu2)-[:AT]->(thu2t13),
(fri2)-[:AT]->(fri2t1), (fri2)-[:AT]->(fri2t2),
(fri2)-[:AT]->(fri2t3), (fri2)-[:AT]->(fri2t4),
(fri2)-[:AT]->(fri2t5), (fri2)-[:AT]->(fri2t6),
(fri2)-[:AT]->(fri2t7), (fri2)-[:AT]->(fri2t8),
(fri2)-[:AT]->(fri2t9), (fri2)-[:AT]->(fri2t10),
(fri2)-[:AT]->(fri2t11), (fri2)-[:AT]->(fri2t12),
(fri2)-[:AT]->(fri2t13);
```

### Creating Semster Template:

The following can also be modified to add semester one in the database. Also beware to change the instances of the year from "2017" to the desired year.

Load in courses from csv file.

```
USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM "file:///programmes.csv" as row create (:Course {name: row.course, code: row.code, campus: row.degree, dept:row.dept, year: "2017", sem:"2"});
```

Connect courses to the corresponding department.

```
MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"Centre for the Creative Arts and Media"}), (c:Course {dept:"CCAM", year:"2017", sem:"2" }) MERGE (d)-[:HAS]->(c);

MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"Dept of Building and Civil Engineering"}), (c:Course {dept:"CE", year:"2017", sem:"2" }) MERGE (d)-[:HAS]->(c);

MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"Dept of Computer Science & Applied Physics"}), (c:Course {dept:"CS", year:"2017", sem:"2" }) MERGE (d)-[:HAS]->(c);

MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"Dept of Culinary Arts"}), (c:Course {dept:"CA", year:"2017", sem:"2" }) MERGE (d)-[:HAS]->(c);

MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"Dept of Electronic and Electrical Engineering"}), (c:Course {dept:"EE", year:"2017", sem:"2" }) MERGE (d)-[:HAS]->(c);

MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"Dept of Electronic and Electrical Engineering"}), (c:Course {dept:"EE", year:"2017", sem:"2" }) MERGE (d)-[:HAS]->(c);

MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"Dept of Heritage and Tourism"}), (c:Course {dept:"HT", year:"2017", sem:"2" }) MERGE (d)-[:HAS]->(c);

MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"Dept of Life and Physical Sciences"}), (c:Course {dept:"LPS", year:"2017", sem:"2" }) MERGE (d)-[:HAS]->(c);

MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"Dept of Mechanical and Industrial Engineering"}), (c:Course {dept:"MIE", year:"2017", sem:"2" }) MERGE (d)-[:HAS]->(c);

MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"Dept of Service Industries"}), (c:Course {dept:"SI", year:"2017", sem:"2" }) MERGE (d)-[:HAS]->(c);

MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"School of Business - Department of Accounting & Information Systems"}), (c:Course {dept:"SOB_AIS", year:"2017", sem:"2" }) MERGE (d)-[:HAS]->(c);

MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"School of Business - Department of Management"}), (c:Course {dept:"SOB_M", year:"2017", sem:"2" }) MERGE (d)-[:HAS]->(c);

MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"National Centre for Excellence in Furniture Design and Technology"}), (c:Course {dept:"EFDT", year:"2017", sem:"2" }) MERGE (d)-[:HAS]->(c);

MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"Mayo Campus"}), (c:Course {dept:"Mayo", year:"2017", sem:"2" }) MERGE (d)-[:HAS]->(c);
```

Load in rooms from csv file.

```
USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM "file:///rooms.csv" as row create (:Room {name: row.room, capacity: row.capacity, campus: row.campus, year: "2017", sem:"2"});
```

### Adding Data

I had planned on adding the lectures in the templating, unfortunately I was unable to find a resource that supplied me with the lectures and their assigned department. I found the gmit staff directory which was inadequate as I could not tell who was a lecturer and what their department was. I add the lectures connected to the second semester sofware development year three.

```
USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM "file:///lecturers.csv" as row 
create (:Lecturer {name: row.name, title: row.title, firstname: row.firstname, 
lastname: row.lastname, location: row.location, ext: row.ext, 
number: row.number, dept:row.dept, year: "2017", sem:"2"});
```

Create the lectures relationship to the their assigned departments.

```
MATCH (:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"Dept of Computer Science & Applied Physics"}), (l:Lecturer{dept:"CS"}) CREATE (d)-[:HAS]->(l);
```

Add groups to course.

```
MATCH (:Academic_Yr {name:"2017"})-[:SEM_2]->(:Dept {name:"Dept of Computer Science & Applied Physics"})-[:HAS]->(course:Course{name:"Computing in Software Development L7 Yr 3 Sem 6"})
CREATE (a:Group{name:"A"}), (b:Group{name:"B"}), 
(c:Group{name:"C"})
MERGE (course)-[:GROUP]->(a)
MERGE (course)-[:GROUP]->(b)
MERGE (course)-[:GROUP]->(c);
```

Add modules and corresponding relationships to course.

```
MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"Dept of Computer Science & Applied Physics"})-[:HAS]->(c:Course{name:"Computing in Software Development L7 Yr 3 Sem 6"})-[:GROUP]-(g:Group{name:"C"}), 
(d)-[:HAS]->(IM:Lecturer {name:"Ian Mc Loughlin"}),
(d)-[:HAS]->(DOD:Lecturer {name:"Deirdre O'Donovan"}),
(d)-[:HAS]->(MH:Lecturer {name:"Martin Hynes"}),
(d)-[:HAS]->(DC:Lecturer {name:"Damien Costello"}),
(d)-[:HAS]->(GH:Lecturer {name:"Gerard Harrison"})
CREATE (GT:Module {name:"Graph Theory"}),
(DMS:Module {name:"Database Mgmt Sys"}),
(MA:Module {name:"Mobile Apps"}),
(SSR:Module {name:"Server Side RAD"}),
(ST:Module {name:"Software Testing"}),
(PPIT:Module {name:"Professional Practice in IT"}),
(IM)-[:LECTURING]->(GT),
(DOD)-[:LECTURING]->(DMS),
(MH)-[:LECTURING]->(ST),
(DC)-[:LECTURING]->(PPIT),
(DC)-[:LECTURING]->(MA),
(GH)-[:LECTURING]->(SSR),
(g)-[:ATTENDING]->(GT),
(g)-[:ATTENDING]->(DMS),
(g)-[:ATTENDING]->(ST),
(g)-[:ATTENDING]->(PPIT),
(g)-[:ATTENDING]->(MA),
(g)-[:ATTENDING]->(SSR);
```

Assign modules rooms.

```
MATCH
(GT:Module {name:"Graph Theory"}),
(DMS:Module {name:"Database Mgmt Sys"}),
(MA:Module {name:"Mobile Apps"}),
(SSR:Module {name:"Server Side RAD"}),
(ST:Module {name:"Software Testing"}),
(PPIT:Module {name:"Professional Practice in IT"}), 
(r1:Room {name:"G0436 CR5", year:"2017", sem:"2"}),
(r2:Room {name:"G0484 CR1", year:"2017", sem:"2"}),
(r3:Room {name:"G0481 CR4", year:"2017", sem:"2"}),
(r4:Room {name:"G0483 CR2", year:"2017", sem:"2"}),
(r5:Room {name:"G0368", year:"2017", sem:"2"}),
(r6:Room {name:"G0208", year:"2017", sem:"2"})
CREATE (GT)-[:IN]->(r1),
(DMS)-[:IN]->(r2),
(MA)-[:IN]->(r3),
(SSR)-[:IN]->(r4),
(ST)-[:IN]->(r5),
(PPIT)-[:IN]->(r6);
```

Assign time and day to modules.

```
MATCH
(:Academic_Yr {name:"2017"})-[:SEM_2]->(:Day {name:"Monday"})-[:AT]->(n:Time {name: "10.00"}), (:Academic_Yr {name:"2017"})-[:SEM_2]->(:Dept {name:"Dept of Computer Science & Applied Physics"})-[:HAS]->(:Course{name:"Computing in Software Development L7 Yr 3 Sem 6"})-[:GROUP]-(:Group{name:"C"})-[:ATTENDING]->(m:Module {name:"Graph Theory"})
CREATE
(m)-[:AT]->(n);

MATCH (year:Academic_Yr {name: "2017"})-[:SEM_2]-> 
(dept:Dept {name:"Galway Campus - Dept of Computer Science & Applied Physics"})-[:HAS]->
(course:Course {name:"Software Development L7 Y3"})-[:GROUP]->(g:Group)-[:ATTENDING]->
(mod:Module)-[:ON]->(day:Day)-[:AT]->(time:Time)-[:IN]->(room:Room), 
(mod)<-[:LECTURING]-(lect:Lecturer) RETURN year, dept, course, g, mod, room, time, day, lect;

MATCH
(:Academic_Yr {name:"2017"})-[:SEM_2]->(:Day {name:"Tuesday"})-[:AT]->(n:Time {name: "14.00"}), (:Academic_Yr {name:"2017"})-[:SEM_2]->(:Dept {name:"Dept of Computer Science & Applied Physics"})-[:HAS]->(:Course{name:"Computing in Software Development L7 Yr 3 Sem 6"})-[:GROUP]-(:Group{name:"C"})-[:ATTENDING]->(m:Module {name:"Database Mgmt Sys"})
CREATE
(m)-[:AT]->(n);

MATCH
(:Academic_Yr {name:"2017"})-[:SEM_2]->(:Day {name:"Wednesday"})-[:AT]->(n:Time {name: "9.00"}), (:Academic_Yr {name:"2017"})-[:SEM_2]->(:Dept {name:"Dept of Computer Science & Applied Physics"})-[:HAS]->(:Course{name:"Computing in Software Development L7 Yr 3 Sem 6"})-[:GROUP]-(:Group{name:"C"})-[:ATTENDING]->(m:Module {name:"Mobile Apps"})
CREATE
(m)-[:AT]->(n);

MATCH
(:Academic_Yr {name:"2017"})-[:SEM_2]->(:Day {name:"Wednesday"})-[:AT]->(n:Time {name: "11.00"}), (:Academic_Yr {name:"2017"})-[:SEM_2]->(:Dept {name:"Dept of Computer Science & Applied Physics"})-[:HAS]->(:Course{name:"Computing in Software Development L7 Yr 3 Sem 6"})-[:GROUP]-(:Group{name:"C"})-[:ATTENDING]->(m:Module {name:"Server Side RAD"})
CREATE
(m)-[:AT]->(n);

MATCH
(:Academic_Yr {name:"2017"})-[:SEM_2]->(:Day {name:"Wednesday"})-[:AT]->(n:Time {name: "12.00"}), (:Academic_Yr {name:"2017"})-[:SEM_2]->(:Dept {name:"Dept of Computer Science & Applied Physics"})-[:HAS]->(:Course{name:"Computing in Software Development L7 Yr 3 Sem 6"})-[:GROUP]-(:Group{name:"C"})-[:ATTENDING]->(m:Module {name:"Professional Practice in IT"})
CREATE
(m)-[:AT]->(n);

MATCH
(:Academic_Yr {name:"2017"})-[:SEM_2]->(:Day {name:"Thursday"})-[:AT]->(n:Time {name: "11.00"}), (:Academic_Yr {name:"2017"})-[:SEM_2]->(:Dept {name:"Dept of Computer Science & Applied Physics"})-[:HAS]->(:Course{name:"Computing in Software Development L7 Yr 3 Sem 6"})-[:GROUP]-(:Group{name:"C"})-[:ATTENDING]->(m:Module {name:"Software Testing"})
CREATE
(m)-[:AT]->(n);
```

## Collecting Data for Database

To collect the data for the rooms, I used a we crawler courtesy of [Ryan Gordon](https://github.com/FlashGordon95), who kindly shared it with the course. For the programmes I developed a python script to parse the dom and save to a csv file. I had built and used this until I realised that I would have to organise these programmes into departments, luckily the GMIT timetable page offers a filter by department feature, which was more tedious to implement than before but worthwhile none the less. I then used the LOAD CSV command to import the programmes, room, and lecturer data into the Neo4j database. The modules and lectures (although both limited - as mentioned above) , are also based on real data, however the times and rooms assigned to the modules are for demonstrational purposes. The rooms.csv, lectures.csv, programmes.csv can be located in the import directory in the database directory. The xml files and parser to creates the programmes.csv can also be found in the data folder.

## To Query Database

### Timetable:

For a student, they need know the **academic year**, **semester**, and **course**:

```
MATCH (year:Academic_Yr {name: "2017"})-[:SEM_2]-> 
(dept:Dept {name:"Dept of Computer Science & Applied Physics"})-[:HAS]->
(course:Course {name:"Computing in Software Development L7 Yr 3 Sem 6"})-[:GROUP]->(g:Group)-[:ATTENDING]->
(mod:Module)-[:AT]->(time:Time)<-[:AT]-(day:Day), 
(mod)<-[:LECTURING]-(lect:Lecturer), (mod)-[:IN]->(room:Room) RETURN year, dept, course, g, mod, room, time, day, lect;
```

This will return the student's entire time table, the groups, the modules, the corresponding lecturers, the rooms and the times. The following is the same query, only it doesn't display the academic year or department that the user has specified - for a cleaner viewing experience. 

```
MATCH (year:Academic_Yr {name: "2017"})-[:SEM_2]-> 
(dept:Dept {name:"Dept of Computer Science & Applied Physics"})-[:HAS]->
(course:Course {name:"Computing in Software Development L7 Yr 3 Sem 6"})-[:GROUP]->(g:Group)-[:ATTENDING]->
(mod:Module)-[:AT]->(time:Time)<-[:AT]-(day:Day), 
(mod)<-[:LECTURING]-(lect:Lecturer), (mod)-[:IN]->(room:Room) RETURN course, g, mod, room, time, day, lect;
```

To search a student timetable with a specific course **group**:

```
MATCH (year:Academic_Yr {name: "2017"})-[:SEM_2]-> 
(dept:Dept {name:"Dept of Computer Science & Applied Physics"})-[:HAS]->
(course:Course {name:"Computing in Software Development L7 Yr 3 Sem 6"})-[:GROUP]->(g:Group{name:"C"})-[:ATTENDING]->
(mod:Module)-[:AT]->(time:Time)<-[:AT]-(day:Day), 
(mod)<-[:LECTURING]-(lect:Lecturer), (mod)-[:IN]->(room:Room) RETURN course, g, mod, room, time, day, lect;
```

For a lecturer to search their timetable, they need enter their **name**, and **department**:

```
MATCH (year:Academic_Yr {name: "2017"})-[:SEM_2]-> 
(dept:Dept {name:"Dept of Computer Science & Applied Physics"})-[:HAS]->(lect:Lecturer{name:"Ian Mc Loughlin"})-[:LECTURING]->(mod:Module)-[:AT]->(time:Time)<-[:AT]-(day:Day), 
(mod)<-[:ATTENDING]-(g:Group)<-[:GROUP]- (course:Course), (mod)-[:IN]->(room:Room) RETURN course, g, mod, room, time, day, lect;
```
For both student timetables and lecturer timetables, they can easily filter by module, lecturer, group, course, room, day and/or time.

Check to see if a room is free, or who is occupying the room.

```
MATCH (year:Academic_Yr {name: "2017"})-[:SEM_2]-> 
(dept:Dept)-[:HAS]->(lect:Lecturer)-[:LECTURING]->(mod:Module)-[:AT]->(time:Time{name:"10.00"})<-[:AT]-(day:Day{name:"Monday"}), 
(mod)<-[:ATTENDING]-(g:Group)<-[:GROUP]- (course:Course), (mod)-[:IN]->(room:Room{name:"G0436 CR5"}) RETURN course, g, mod, room, time, day, lect;
```

To search lectures in given **department**:

```
MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"Dept of Computer Science & Applied Physics"})-[:HAS]->(l:Lecturer) return y,d,l;
```

To search for all courses connected to a **department**:

```
MATCH (y:Academic_Yr {name:"2017"})-[:SEM_2]->(d:Dept {name:"Centre for the Creative Arts and Media"})-[:HAS]->(c:Course) return y,d,c;
```

## Conclusion
This assignment has been overall, a learned experience. If I were to design another graph database in Neo4j, I would have a better idea of how to design and structure the nodes, edges and properties that compose the database. And if I were to redo this project, I would place the group node **after** the module, and manage my time more eficiently.

**References:**

https://neo4j.com/product/
http://stackoverflow.com/questions/24015854/check-whether-a-node-exists-if-not-create
http://stackoverflow.com/questions/24438083/neo4j-csv-cypher-import
http://stackoverflow.com/questions/30871599/neo4j-syntax-for-loading-csv-with-headers
https://neo4j.com/developer/guide-import-csv/
http://jexp.de/blog/2014/06/load-csv-into-neo4j-quickly-and-successfully/
https://neo4j.com/blog/importing-data-neo4j-via-csv/
http://stackoverflow.com/questions/24015854/check-whether-a-node-exists-if-not-create
http://stackoverflow.com/questions/30636248/split-a-string-only-by-first-space-in-python
https://www.tutorialspoint.com/python/python_for_loop.htm
https://docs.python.org/3/library/xml.etree.elementtree.html

-----

__*Tara O'Kelly - G00322214@gmit.ie*__