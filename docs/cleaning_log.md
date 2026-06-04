\# Cleaning Log



\## Missing Value Report



Checked using:



```python

df.isna().sum()

```



Result:



\* timestamp: 0

\* temperature\_c: 0

\* humidity\_pct: 0

\* co2\_ppm: 0

\* yield\_kg: 0



\## Validation Rules



Rows were retained only if:



\* humidity\_pct between 50 and 100

\* temperature\_c between 10 and 35

\* co2\_ppm between 400 and 2000

\* yield\_kg is not null



\## Missing Value Handling



Short gaps in sensor columns were forward-filled:



\* temperature\_c

\* humidity\_pct

\* co2\_ppm



Maximum fill length: 2 rows.



\## Duplicate Handling



Duplicate timestamps were removed using:



```python

drop\_duplicates(subset=\["timestamp"], keep="last")

```



\## Final Dataset



Final row count: 365



Output file:



```text

data/interim/02\_cleaned.parquet

```



Target column null count:



```text

0

```



