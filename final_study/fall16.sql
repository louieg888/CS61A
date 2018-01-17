create table ns as
with t ( n ) as ( select 0 union select n +1 from t where n < 99 )
select * from t ;
create table ps as select n from ns where n > 0;

CREATE TABLE hailstoned2 AS 
    SELECT a.n as x, b.n as y, c.n as gcd
    FROM ps as a, ps as b, ps as c
    WHERE x <> y AND x % gcd = 0 AND y % gcd = 0
    GROUP BY x, y HAVING MAX(GCD);

CREATE TABLE hailstoned3 AS 
    WITH hailstone(m, length) as (
        SELECT 1, 1 UNION
        SELECT n,length+1 FROM hailstone, ps 
            WHERE (n % 2 == 0 and m == n / 2) OR 
            (n > 1 and n % 2 == 1 and m = 3 * n + 1)
    ) SELECT * FROM hailstone;

select * from hailstoned3;
