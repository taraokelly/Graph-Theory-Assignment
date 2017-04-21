# Graph-Theory-Assignment
*Database designed with neo4j for the GMIT timetabling system. Third Year, Graph Theory, Software Development.*

**First Draft:**

```
CREATE (year:Academic_Yr {name: "2017"}), (dept:Dept {name:"Galway Campus - Dept of Computer Science & Applied Physics"}), (course:Course {name:"Software Development L7 Y3"}), 
(group :Group {name:"C"}), (lect:Lecturer {name:"Ian McLoughlin"}), (mod:Module {name:"Graph Theory"}), (room:Room {name:"1000"}), (time:Time {name:"09:00"}), (day:Day {name:"Monday"}), 
(year)-[:SEM_2]->(dept), (dept)-[:HAS]->(course), (dept)-[:HAS]->(lect), (course)-[:GROUP]->(group), (group)-[:ATTENDING]->(mod), (lect)-[:LECTURING]->(mod), 
(mod)-[:IN]->(room), (room)-[:AT]->(time),(time)-[:ON]->(day);
```

![alt text](https://github.com/taraokelly/Graph-Theory-Assignment/blob/master/img/v0.PNG "v0.0.1")

__*N.B. This draft's data is not accurate, just used for testing/demonstrational purposes.*__

(2017)-[:SEM_3]->(Software Development L7 Y3)-[:HAS]->(Software Development L7 Y3)-[:GROUP]->(C)-[:ATTENDING]->(Graph Theory)-[:IN]->(1000)-[:AT]->(09:00)-[:ON]->(Monday)

2017, SEMESTER 3, Software Development L7 Y3 HAS Software Development L7 Y3 GROUP C ATTENDING Graph Theory IN 1000 AT 9:00 ON Monday.

**To Query Database:**

As a for a student, they need know the academic year, semester, course.

```
MATCH (year:Academic_Yr {name: "2017"})-[r:SEM_2]-> (dept:Dept {name:"Galway Campus - Dept of Computer Science & Applied Physics"})
-[r1:HAS]->(course:Course {name:"Software Development L7 Y3"})-[:GROUP]->(g:Group)-[:ATTENDING]->(mod:Module)-[:IN]->(room:Room)
-[:AT]->(time:Time)-[:ON]->(day:Day), (mod)<-[:LECTURING]-(lect:Lecturer) RETURN year, dept, course, g, mod, room, time, day, lect;
```

This will return the student's entire time table, the groups, the modul, the corresponding lecturer, the room and the time. The following is the same query, only it doesn't display the academic year or department that the user has specified - for a cleaner viewing experience. 

```
MATCH (year:Academic_Yr {name: "2017"})-[r:SEM_2]-> (dept:Dept {name:"Galway Campus - Dept of Computer Science & Applied Physics"})
-[r1:HAS]->(course:Course {name:"Software Development L7 Y3"})-[:GROUP]->(g:Group)-[:ATTENDING]->(mod:Module)-[:IN]->(room:Room)
-[:AT]->(time:Time)-[:ON]->(day:Day), (mod)<-[:LECTURING]-(lect:Lecturer) RETURN course, g, mod, room, time, day, lect;
```

-----

__*Tara O'Kelly - G00322214@gmit.ie*__