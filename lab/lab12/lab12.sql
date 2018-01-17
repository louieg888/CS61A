.read sp17data.sql
.read fa17data.sql

CREATE TABLE obedience AS
  SELECT seven, denero, hilfinger FROM students;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 18 ORDER BY smallest LIMIT 20;

CREATE TABLE greatstudents AS
  SELECT a.date, a.color, a.pet, a.number, b.number
  FROM students AS a, sp17students AS b
  WHERE a.color = b.color AND a.pet = b.pet AND a.date = b.date;

CREATE TABLE sevens AS
  SELECT students.seven FROM students, checkboxes
  WHERE students.number = 7 AND checkboxes.'7' = 'True' AND checkboxes.time = students.time;

CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b
  WHERE a.pet = b.pet AND a.song = b.song AND a.time != b.time;
