# Polyhouse Data Quality Report

Total observations: 365

Date range: 2024-01-01 00:00:00 → 2024-12-30 00:00:00


## Summary Statistics

|               |   count |     mean |       std |    min |    25% |    50% |    75% |     max |        cv |
|:--------------|--------:|---------:|----------:|-------:|-------:|-------:|-------:|--------:|----------:|
| temperature_c |     365 |  21.9867 |  1.41241  |  18.15 |  21.01 |  21.97 |  22.88 |   26.37 | 0.0642392 |
| humidity_pct  |     365 |  86.7433 |  3.06779  |  78.1  |  84.6  |  86.7  |  88.7  |   94.8  | 0.0353664 |
| co2_ppm       |     365 | 901.162  | 78.2652   | 608    | 854    | 904    | 949    | 1154    | 0.0868493 |
| yield_kg      |     365 |  17.1394 |  0.679041 |  15.31 |  16.7  |  17.13 |  17.63 |   18.85 | 0.0396187 |

## Insights

- Humidity remains within the expected polyhouse operating range.
- Yield shows variation across observations, indicating changing growing conditions.
- CO₂ values stay within the configured validation thresholds.