WITH random_transaction AS (
   SELECT '2024-01-01'::timestamptz + '10 seconds'::interval * g AS transaction_date,
       generate_series(1, 1000) AS transaction_id,
       (random() * 10)::numeric(10, 2) AS amount, 
       (random() * 1000)::int + 1 AS customer_id
   FROM generate_series(1, 1000) g
)
INSERT INTO transaction (
         transaction_date,
         transaction_id,
         amount,
         customer_id
)
SELECT transaction_date, 
    transaction_id
    amount,
    customer_id
FROM random_transactions;