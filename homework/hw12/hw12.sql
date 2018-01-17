CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name AS name, size AS size FROM dogs, sizes WHERE height > min AND height <= max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_height AS
  SELECT child FROM dogs as a, parents as b WHERE a.name = b.parent
  ORDER BY a.height DESC;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  WITH siblings(sib1, sib2) AS (
    SELECT a.child, b.child FROM parents as a, parents as b WHERE a.parent = b.parent AND a.child < b.child
  )
  SELECT sib1 || " and " || sib2 || " are " || b.size || " siblings" FROM siblings as a, size_of_dogs as b, size_of_dogs as c WHERE sib1 = b.name AND sib2 = c.name AND b.size = c.size AND sib1 < sib2;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks AS
  WITH helper(numDogs, list, total, lastHeight) AS (
    SELECT 3, name, height, height FROM dogs UNION
    SELECT numDogs-1, name || ", " || list, total + height, height FROM dogs, helper WHERE numdogs > 0 AND height < lastHeight
  )
  SELECT list, total FROM helper WHERE numDogs = 0 AND total > 170 ORDER BY total ASC;





