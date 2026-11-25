--Exploring a mock database running on DuckDB, using several SQL queries.

/*
Example 1: Find the Nth highest refund (3rd highest)
*/

WITH refund_ranks AS (
    SELECT
    amount,
    DENSE_RANK() OVER (ORDER BY amount DESC) as rnk
  FROM refunds
)

SELECT amount
FROM refund_ranks
WHERE rnk = 3
LIMIT 1;

/*
Example 2: Find orders with more than 1 refund
*/

SELECT COUNT(refund_id) AS tot_refunds, order_id
FROM refunds
GROUP BY order_id
HAVING tot_refunds > 1;

-- Here's a more advanced query to retrieve customer data from the customers table
SELECT
    COUNT(r.refund_id) AS tot_refunds,
    r.order_id,
    o.customer_id,
    c.email,
    c.first_name
FROM refunds AS r
LEFT JOIN orders AS o
    ON r.order_id = o.order_id
LEFT JOIN customers AS c
    ON o.customer_id = c.customer_id
GROUP BY
    r.order_id,
    o.customer_id,
    c.email,
    c.first_name
HAVING COUNT(r.refund_id) > 1;

/*
Example 3: Get the latest order per customer_id
*/

WITH ranked_orders AS (
    SELECT
        order_id,
        customer_id,
        order_ts,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_ts DESC, order_id DESC
        ) AS recency_rank
    FROM orders
)
SELECT
    order_id AS OrderID,
    customer_id AS CustomerID,
    order_ts AS LatestOrderTS,
    recency_rank AS Rnk
FROM ranked_orders
WHERE recency_rank = 1;

/*
Example 4: Identify calendar dates with no orders.

Approach:
1. Generate a complete daily calendar for 2026 using generate_series().
2. Aggregate orders by date.
3. LEFT JOIN orders onto the calendar so that dates without orders remain in the results.
4. Filter for dates where no matching order exists.
*/

-- Generate a complete calendar of dates for 2026
WITH calendar AS (
SELECT
CAST(day AS DATE) AS order_date
FROM generate_series(
DATE '2026-01-01',
DATE '2026-12-31',
INTERVAL 1 DAY
) AS t(day)
),
  
-- Count orders for each calendar date
daily_orders AS (
SELECT
CAST(order_ts AS DATE) AS order_date,
COUNT(*) AS order_count
FROM orders
WHERE order_ts >= DATE '2026-01-01'
AND order_ts < DATE '2027-01-01'
GROUP BY 1
)
 
-- Return only dates with no orders
SELECT
c.order_date,
COALESCE(o.order_count, 0) AS order_count,
o.order_count IS NULL AS no_orders
FROM calendar c
LEFT JOIN daily_orders o
ON c.order_date = o.order_date
WHERE no_orders = true
ORDER BY c.order_date DESC;

/*
Sanity check: count calendar days with and without orders in 2026.
This is a complementary diagnostic query to the one above.

- total_calendar_days: all dates in the generated 2026 calendar;
- days_with_orders: dates with at least one order;
- days_without_orders: calendar dates with no matching order;
- total_orders: total number of orders places in 2026.

SELECT
    COUNT(*) AS total_calendar_days,
    COUNT(*) FILTER (
        WHERE o.order_count IS NOT NULL
    ) AS days_with_orders,
    COUNT(*) FILTER (
        WHERE o.order_count IS NULL
    ) AS days_without_orders,
    SUM(COALESCE(o.order_count, 0)) AS total_orders
FROM calendar c
LEFT JOIN daily_orders o
ON c.order_date = o.order_date;
*/

/*
Example 5: Find top 3 price ranks per category including ties
*/

WITH product_price_ranks AS (
    SELECT
        product_id,
        category,
        unit_price,
        DENSE_RANK() OVER (
            PARTITION BY category
            ORDER BY unit_price DESC
        ) AS price_rank
    FROM products
)

SELECT
    product_id,
    category,
    unit_price,
    price_rank
FROM product_price_ranks
WHERE price_rank <= 3
ORDER BY
    category,
    price_rank;

/*
Thanks for visiting, any feedback is welcome!
*/