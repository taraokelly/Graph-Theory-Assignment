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

Start with creating the academic year, adding the days and creating the relationship between them for each semester.
 
```
CREATE (year:Academic_Yr {name: "2017"}), (mon1:Day {name:"Monday"}), (tue1:Day {name:"Tuesday"}), (wed1:Day {name:"Wednesday"}), (thu1:Day {name:"Thursday"}), (fri1:Day {name:"Friday"}), (mon2:Day {name:"Monday"}), (tue2:Day {name:"Tuesday"}), (wed2:Day {name:"Wednesday"}), (thu2:Day {name:"Thursday"}), (fri2:Day {name:"Friday"}), (year)-[:SEM_1]->(tue1), (year)-[:SEM_1]->(wed1), (year)-[:SEM_1]->(thu1), (year)-[:SEM_1]->(fri1), (year)-[:SEM_2]->(mon2), (year)-[:SEM_2]->(tue2), (year)-[:SEM_2]->(wed2), (year)-[:SEM_2]->(thu2), (year)-[:SEM_2]->(fri2);
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