# SQL injection on PortSwigger "WHERE clause" lab — EXAMPLE write-up
**Class:** SQLi  ·  **Target:** PortSwigger Apprentice lab (SQLi in WHERE clause)  ·  **Date:** 2026-06-__

> This is an EXAMPLE showing the format. Replace with your own solve, in your own words. Do not submit this file as-is — write your own once you've actually solved the lab.

## The bug
The product-category filter put my input straight into a SQL `WHERE` clause, so I could change what the query returned.

## What I sent
In the category parameter:
```
'+OR+1=1--
```

## Why it worked
The app built the query as `... WHERE category = '<my input>' AND released = 1`. My `' OR 1=1--` made the condition always true and commented out the rest, so it returned every product, including unreleased ones.

## The fix
Use parameterised queries (prepared statements) so user input is data, never part of the SQL. Never string-concatenate input into a query.

## What I learned
If user input reaches a query unparameterised, you can rewrite the query's logic — the `--` comment trick is how you discard the rest of the statement.
