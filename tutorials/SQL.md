# articles
https://www.swequiz.com/learn/database-types-explained 

# load a CSV file and create a table using the Datasette tool. 
1- in the Datasette tool, click on the right-top three lines icon and select "add dataset"
2- add the url address in the url field
3- run the query: SELECT COUNT(*) FROM exercise03_car_sales_data; 

# using aggregating functions in sql
SELECT max(price) as max_price, 
               min(price) as min_price,
               avg(price) as avg_price
FROM exercise03_car_sales_data;

# using distinct 
SELECT distinct(model) as max_price
FROM exercise03_car_sales_data;