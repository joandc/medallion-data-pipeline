# analysis_preview.md

## Statistical Questions

This Gold dataset is designed to support the following Part 2 questions:

1. Is average daily AQI different from a benchmark value?
2. Do PM2.5 levels differ on rainy days versus non-rainy days?
3. Is the proportion of rainy days higher in Toronto than in Vancouver?

## Outcome Variables

The main outcome variables for these questions are:

- `aqi_max`
- `pm25_mean`
- `rainy_day`

## Grouping Variables

The main grouping variables for these questions are:

- `city`
- `rainy_day`

## Binary Variables

The key binary variable for these questions is:

- `rainy_day`

## Hypothesis Examples

### Question 1

Is average daily AQI different from a benchmark value?

Null hypothesis:

- the mean daily AQI is equal to a benchmark value

Alternative hypothesis:

- the mean daily AQI is different from a benchmark value

Best-fit test:

- one-sample t-test

### Question 2

Do PM2.5 levels differ on rainy days versus non-rainy days?

Null hypothesis:

- the mean PM2.5 level is the same on rainy days and non-rainy days

Alternative hypothesis:

- the mean PM2.5 level is different on rainy days and non-rainy days

Best-fit test:

- two-sample t-test

### Question 3

Is the proportion of rainy days higher in Toronto than in Vancouver?

Null hypothesis:

- the proportion of rainy days is the same in Toronto and Vancouver

Alternative hypothesis:

- the proportion of rainy days is higher in Toronto than in Vancouver

Best-fit test:

- proportion z-test

## Best-Fit Tests

This Gold dataset directly supports the three required test types:

- one-sample t-test using `aqi_max`
- two-sample t-test using `pm25_mean` grouped by `rainy_day`
- proportion z-test using `rainy_day` grouped by `city`

## Dataset Features Added for These Questions

To support these analyses, the Gold dataset includes:

- `aqi_max` for benchmark comparison
- `pm25_mean` for continuous air-quality comparison
- `rainy_day` as a binary weather indicator
- `city` as a grouping variable for location-based comparison
