# Graph-Theory-Assignment
*Database designed with neo4j for the GMIT timetabling system. Third Year, Graph Theory, Software Development.*

**First Draft:**

```
CREATE (year:Academic_Yr {name: "2017"}), (dept:Dept {name:"Galway Campus - Dept of Computer Science & Applied Physics"}), (course:Course {name:"Software Development L7 Y3"}), 
(group :Group {name:"C"}), (lect:Lecturer {name:"Ian McLoughlin"}), (mod:Module {name:"Graph Theory"}), (room:Room {name:"1000"}), (time:Time {name:"09:00"}), (day:Day {name:"Monday"}), 
(year)-[:SEM_3]->(dept), (dept)-[:HAS]->(course), (dept)-[:HAS]->(lect), (course)-[:GROUP]->(group), (group)-[:ATTENDING]->(mod), (lect)-[:LECTURING]->(mod), 
(mod)-[:IN]->(room), (room)-[:AT]->(time),(time)-[:ON]->(day);
```

![alt text](https://github.com/taraokelly/Graph-Theory-Assignment/blob/master/img/v0.PNG "v0.0.1")

*N.B. This draft's data is not accurate, just used for testing/demonstrational purposes.*

(2017)-[:SEM_3]->(Software Development L7 Y3)-[:HAS]->(Software Development L7 Y3)-[:GROUP]->(C)-[:ATTENDING]->(Graph Theory)-[:IN]->(1000)-[:AT]->(09:00)-[:ON]->(Monday)

2017, *Semester 3*, Software Development L7 Y3 *HAS* Software Development L7 Y3 *GROUP* C *ATTENDING* Graph Theory *IN* 1000 *AT* 9:00 *ON* Monday.

-----

__*Tara O'Kelly - G00322214@gmit.ie*__