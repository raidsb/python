# articles
https://www.swequiz.com/learn/database-types-explained 

# load a CSV file and create a table using the Datasette tool. 
1- in the Datasette tool, click on the right-top three lines icon and select "add dataset"
2- add the url address in the url field
3- run the query: SELECT COUNT(*) FROM exercise03_car_sales_data; 

# using aggregating functions in sql
```
SELECT max(price) as max_price, 
               min(price) as min_price,
               avg(price) as avg_price
FROM exercise03_car_sales_data;
```

# using distinct 
SELECT distinct(model) as max_price
FROM exercise03_car_sales_data;

# using distinct with aggregate function
```
select count(city) - count(distinct city)
from station
```

# Length or len of a field 
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

```
select city, length(city)
from station
order by length(city), city asc
 limit 1; 
 
 select city, length(city)
  from station
  order by length(city) desc
  limit 1
```

# query for names starting with chars 
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
```
select distinct city 
from station 
where left(city, 1) in ('a', 'e', 'i', 'o', 'u');
```

ending 
```
select distinct city
from station 
where right(city, 1) in ('a', 'e', 'i', 'o', 'u')
```

not ending
```
select distinct city
from station 
where right(city, 1) not in ('a', 'e', 'i', 'o', 'u')

/*or*/
select distinct city
from station 
where right(city, 1) not in ('a', 'e', 'i', 'o', 'u') or left(city, 1) not in ('a', 'e', 'i', 'o', 'u')

/*and*/
select distinct city
from station 
where right(city, 1) not in ('a', 'e', 'i', 'o', 'u') and  left(city, 1) not in ('a', 'e', 'i', 'o', 'u')
```

# nested order by
Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

# round and truncate 
```
select round(max(lat_n), 4) from station where lat_n < 137.2345
select truncate(max(lat_n), 4) from station where lat_n < 137.2345
```

# using order by with great value
Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than . Round your answer to  decimal places.

```
select round(long_w, 4) 
from station 
where lat_n < 137.2345
  order by lat_n desc 
  limit 1
```

# manhattan distance
```
/* manhattan distance: |x1 - x2| + |y1 - y2|*/
select round(abs(min(lat_n) - max(lat_n)) + abs(min(long_w) - max(long_w)), 4) as manhattan_distance
from station
```

# using power
```
select round(power(power(min(lat_n) - max(lat_n), 2) + power(min(long_w) - max(long_w), 2), 0.5), 4)
from station
```

# with syntax 
The WITH Clause in SQL
WITH clause, also known as a ** Common Table Expression (CTE)**, is a powerful tool in SQL for creating temporary named result sets that can be referenced within a single SELECT, INSERT, UPDATE, or DELETE statement. It enhances query readability, maintainability, and performance by breaking down complex queries into smaller, reusable subqueries.

```
SELECT ROUND(AVG(LAT_N), 4) AS median_latitude
FROM (
  SELECT LAT_N,
         @row_number := @row_number + 1 AS row_num,
         @total_rows := @total_rows
  FROM STATION, (SELECT @row_number := 0, @total_rows := COUNT(*) FROM STATION) AS init
  ORDER BY LAT_N
) AS derived_table
WHERE row_num IN ((@total_rows + 1) / 2, (@total_rows + 2) / 2);
```
