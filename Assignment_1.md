PART A:

```sql
SELECT product_name FROM Product WHERE product_id = "PR4087";
SELECT product_name, price FROM Product WHERE manufacturer = "LEGO" ORDER BY price LIMIT 20;
SELECT product_name, (price-cost) AS "margin" FROM Product WHERE manufacturer = "LEGO" ORDER BY (price-cost) LIMIT 3;
SELECT DISTINCT manufacturer FROM Product WHERE price > 200;
SELECT * FROM Customer WHERE country IN ("Sweden", "Denmark", "Norway") ORDER BY RAND() LIMIT 10;
```

PART B:

```sql
SELECT AVG(price) FROM Product WHERE manufacturer = "LEGO";
SELECT COUNT(*) FROM Product WHERE Product_name LIKE '%lego%' AND Product_name LIKE '%star wars%';
SELECT COUNT(*) FROM Receipt WHERE date > '2021-04-01';
SELECT country, COUNT(*) FROM Customer GROUP BY country;
SELECT WEEKDAY(date), COUNT(*) FROM Receipt GROUP BY WEEKDAY(date);
```

C1:

```sql
SELECT WEEKDAY(date)
FROM ReceiptProduct RP
LEFT JOIN Product P
ON RP.product_id = P.product_id
LEFT JOIN Receipt R
ON RP.receipt_id = R.receipt_id
WHERE P.product_name LIKE '%Voldemort%'
ORDER BY date ASC
LIMIT 1;
```

C2:

```sql
SELECT COUNT(*)
FROM ReceiptProduct RP
LEFT JOIN Product P
ON RP.product_id = P.product_id
LEFT JOIN Receipt R
ON RP.receipt_id = R.receipt_id
LEFT JOIN Customer C
ON R.customer_id = C.customer_id
WHERE P.product_name LIKE '%Voldemort%' AND date >= '2021-01-01' AND country IN ("Canada", "Great Britain");
```

C3:

```sql
SELECT product_name, (price-cost) AS "margin"
FROM  Product P
LEFT JOIN ReceiptProduct RP
ON P.product_id = RP.product_id
WHERE RP.product_id IS NULL AND P.price IS NOT NULL
ORDER BY (price-cost)
LIMIT 3;
```

C4:

```sql
SELECT C.customer_id, name, sum(price*quantity) AS "total money spent"
FROM Customer C
LEFT JOIN Receipt R
ON C.customer_id = R.customer_id
LEFT JOIN ReceiptProduct RP
ON R.receipt_id = RP.receipt_id
LEFT JOIN Product P
ON RP.product_id= P.product_id
WHERE P.manufacturer  = "LEGO"
group by C.customer_id
HAVING sum(price*quantity) > 500;
```

PART D:

```sql
SELECT *
FROM Customer C1, Customer C2
WHERE C1.phone = C2.phone
AND C1.customer_id != C2.customer_id
LIMIT 1;
```
