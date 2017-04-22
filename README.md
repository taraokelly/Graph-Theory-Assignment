# Graph-Theory-Assignment
*Database designed with neo4j for the GMIT timetabling system. Third Year, Graph Theory, Software Development.*

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

__*N.B. This draft's data is not accurate, just used for testing/demonstrational purposes. Real data will be entered for the finished assignment.*__


## Setting Up Database

### Creating Constraints and Indexes:

Create constraint for the Academic_Yr node (this also creates an index).
 
```
CREATE CONSTRAINT ON (a:Academic_Yr) ASSERT a.name IS UNIQUE;
```

Create indexes.

```
CREATE INDEX ON :Dept(name);
CREATE INDEX ON :Course(name);
CREATE INDEX ON :Group(name);
CREATE INDEX ON :Lecture(name);
CREATE INDEX ON :Module(name);
CREATE INDEX ON :Room(name);
CREATE INDEX ON :Time(name);
CREATE INDEX ON :Day(name);
```

### Creating Year Template:

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
(year)-[:SEM_1]->(d1s2), (year)-[:SEM_1]->(d2s2), 
(year)-[:SEM_1]->(d3s2), (year)-[:SEM_1]->(d4s2), 
(year)-[:SEM_1]->(d5s2), (year)-[:SEM_1]->(d6s2),
(year)-[:SEM_1]->(d7s2), (year)-[:SEM_1]->(d8s2), 
(year)-[:SEM_1]->(d9s2), (year)-[:SEM_1]->(d10s2), 
(year)-[:SEM_1]->(d11s2), (year)-[:SEM_1]->(d12s2),
(year)-[:SEM_1]->(d13s2),
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

Load in courses from csv file.

```
USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM "file:///programmes.csv" as row create (:Course {name: row.course, code: row.code, campus: row.degree, year: "2017", sem:"2"});
```

## To Query Database

### Student Timetable:

For a student, they need know the **academic year**, **semester**, and **course**:

```
MATCH (year:Academic_Yr {name: "2017"})-[:SEM_2]-> 
(dept:Dept {name:"Galway Campus - Dept of Computer Science & Applied Physics"})-[:HAS]->
(course:Course {name:"Software Development L7 Y3"})-[:GROUP]->(g:Group)-[:ATTENDING]->
(mod:Module)-[:ON]->(day:Day)-[:AT]->(time:Time)-[:IN]->(room:Room), 
(mod)<-[:LECTURING]-(lect:Lecturer) RETURN year, dept, course, g, mod, room, time, day, lect;
```

This will return the student's entire time table, the groups, the modules, the corresponding lecturers, the rooms and the times. The following is the same query, only it doesn't display the academic year or department that the user has specified - for a cleaner viewing experience. 

```
MATCH (:Academic_Yr {name: "2017"})-[:SEM_2]-> 
(:Dept {name:"Galway Campus - Dept of Computer Science & Applied Physics"})-[:HAS]->
(course:Course {name:"Software Development L7 Y3"})-[:GROUP]->(g:Group)-[:ATTENDING]->
(mod:Module)-[:ON]->(day:Day)-[:AT]->(time:Time)-[:IN]->(room:Room), 
(mod)<-[:LECTURING]-(lect:Lecturer) RETURN course, g, mod, room, time, day, lect;
```

To search a student timetable with a specific course **group**:

```
MATCH (:Academic_Yr {name: "2017"})-[:SEM_2]-> 
(:Dept {name:"Galway Campus - Dept of Computer Science & Applied Physics"})-[:HAS]->
(course:Course {name:"Software Development L7 Y3"})-[:GROUP]->(g:Group{name: "C"})-[:ATTENDING]->
(mod:Module)-[:ON]->(day:Day)-[:AT]->(time:Time)-[:IN]->(room:Room), 
(mod)<-[:LECTURING]-(lect:Lecturer) RETURN course, g, mod, room, time, day, lect;
```

-----

__*Tara O'Kelly - G00322214@gmit.ie*__