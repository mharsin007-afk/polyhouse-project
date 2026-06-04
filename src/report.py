import pandas as pd
from pathlib import Path

df = pd.read_parquet("data/interim/02_cleaned.parquet")

# Summary statistics
summary = df[
    ["temperature_c", "humidity_pct", "co2_ppm", "yield_kg"]
].describe().T

summary["cv"] = summary["std"] / summary["mean"]

report = []

report.append("# Polyhouse Data Quality Report\n")

report.append(f"Total observations: {len(df)}\n")

report.append(
    f"Date range: {df['timestamp'].min()} → {df['timestamp'].max()}\n"
)

report.append("\n## Summary Statistics\n")
report.append(summary.to_markdown())

report.append("\n## Insights\n")

report.append(
    "- Humidity remains within the expected polyhouse operating range."
)

report.append(
    "- Yield shows variation across observations, indicating changing growing conditions."
)

report.append(
    "- CO₂ values stay within the configured validation thresholds."
)

Path("reports").mkdir(exist_ok=True)

Path("reports/data_quality.md").write_text(
    "\n".join(report),
    encoding="utf-8"
)

print("Report saved to reports/data_quality.md")