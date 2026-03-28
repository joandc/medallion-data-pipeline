# Assignment 3 - Data Pipeline for Statistical Analysis

## Overview

This project implements Project Part 1 using Weather and Air Quality Pipeline Data and Python. It builds a medallion-style ETL pipeline that:

- ingests weather and air-quality data from Open-Meteo
- stores raw snapshots in Bronze
- cleans and standardizes source data in Silver
- joins both sources into a Gold dataset for later statistical testing

The project is designed so Project Part 2 can use the Gold dataset in a Streamlit app. The current analysis plan focuses on one-sample t-test, two-sample t-test, and proportion z-test support.

## Chosen API Pack

This implementation uses:

- Open-Meteo Historical Weather
- Open-Meteo Air Quality

The pipeline pulls data for two cities:

- Toronto
- Vancouver

Using two cities gives the Gold dataset a natural grouping variable for future two-sample comparisons and proportion tests.

## Repository Layout

```text
.
|-- README.md
|-- requirements.txt
|-- .env.example
|-- .gitignore
|-- analysis_preview.md
|-- data/
|   |-- bronze/
|   |-- silver/
|   `-- gold/
|-- ingest/
|-- transform/
`-- notebooks/
```

## Bronze, Silver, Gold

### Bronze

Raw Open-Meteo API responses are saved exactly as returned under:

- `data/bronze/open_meteo_weather/`
- `data/bronze/open_meteo_air_quality/`

Each file uses a timestamped filename so multiple snapshots can be retained.

### Silver

The Silver layer contains one cleaned table per source:

- `data/silver/weather_daily_clean.csv`
- `data/silver/air_quality_daily_clean.csv`

Weather data is flattened from daily arrays. Air-quality data is aggregated from hourly observations to daily metrics.

### Gold

The Gold layer joins Silver datasets on `date` and `city` into:

- `data/gold/weather_air_quality_daily.csv`

Derived features, based on analysis_preview.md, include:

- `rainy_day`

## How To Run

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
uv add requests pandas
```

3. Optionally create a `.env` file from `.env.example`.
4. Run stages separately:

```bash
uv run python ingest/run_ingestion.py
uv run python transform/build_silver.py
uv run python transform/build_gold.py
```

## Join and Missing-Value Strategy

- Silver weather and air-quality tables are joined on `date` and `city`.
- The Gold build uses an inner join so only dates present in both cleaned sources are included.
- Missing hourly air-quality values are ignored during daily aggregation when possible through pandas aggregation defaults.
- Any remaining rows missing required Gold fields are dropped before output.

## Gold Dataset Purpose

The Gold dataset is intentionally small and designed for Part 2 statistical analysis. It supports:

- a one-sample t-test using `aqi_max`
- a two-sample t-test using `pm25_mean` grouped by `rainy_day`
- a proportion z-test using `rainy_day` grouped by `city`

Example future questions:

- Is average daily AQI different from a benchmark value?
- Do PM2.5 levels differ on rainy versus non-rainy days?
- Is the proportion of rainy days higher in Toronto than in Vancouver?

## AI Usage

AI tools used:

- ChatGPT

What AI helped with:

- assignment breakdown
- repository scaffolding
- ETL boilerplate structure
- planning how to shape the Gold dataset for later hypothesis testing

One thing verified manually:

- the project structure and feature set were checked against the assignment brief to make sure Weather and Air Quality Pipeline Data, Bronze snapshot requirements, and Gold analysis requirements were all covered.
