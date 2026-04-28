CREATE DATABASE marketing_data;

USE marketing_data;

-- First question to be answered: how many rows does the database have?

SELECT COUNT(*) AS total_rows
FROM ab_test;

-- Secondly, we need to check how are users split between the two groups:

SELECT 
    test_group,
    COUNT(*) AS users,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS pct_of_total
FROM ab_test
GROUP BY test_group;

/* Based on the results, we can notice something important: group distribution is not the same: 
Exactly 96% of users are in the ad group and only 4% saw the PSA.
This is not a balanced experiment, and it matters for results interpretation. */

-- Here's how to answer the core question "do people who see ads convert at a higher rate":

SELECT 
    test_group,
    COUNT(*) AS total_users,
    SUM(CASE WHEN converted = TRUE THEN 1 ELSE 0 END) AS converted_users,
    ROUND(
        SUM(CASE WHEN converted = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 
        2
    ) AS conversion_rate_pct
FROM ab_test
GROUP BY test_group;

-- The ad group converts at 2.55% and the PSA group at 1.79%. What's the percentage difference? We can calculate the lift: [(2.55% - 1.79%)/1.79%] = +42.5%

/* 
That's a relative lift of 42.5% — a meaningful difference. 
Is it real, or could it have happened by chance?
That is the central question of A/B testing, and it's not optional to answer. 
We need a statistical significance test before making any business recommendation.
*/

-- Not all users in the ad group saw the same number of ads. Does seeing more ads make you more likely to convert? To calculate AVG ads seen per each group:

SELECT
	test_group,
    COUNT(*) AS users,
    ROUND(AVG(total_ads), 1) AS avg_ads_seen
FROM ab_test
GROUP BY test_group;

-- In order to calculate the median, the following query doesn't work in MySQL:

SELECT 
    test_group,
    ROUND(AVG(total_ads), 1) AS avg_ads_seen,
    MIN(total_ads) AS min_ads,
    MAX(total_ads) AS max_ads,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY total_ads) AS median_ads
FROM ab_test
GROUP BY test_group;

-- To calculate the median in MySQL, we need to do something else, employing both subqueries and window functions:

SELECT
    test_group,    
    AVG(total_ads) AS median_ads
FROM (
    SELECT
        test_group,
        total_ads,
        ROW_NUMBER() OVER (PARTITION BY test_group ORDER BY total_ads) AS rn,
        COUNT(*) OVER (PARTITION BY test_group) AS cnt
    FROM ab_test
) AS t
WHERE rn IN (FLOOR((cnt + 1) / 2), FLOOR((cnt + 2) / 2))
GROUP BY test_group;

-- Both groups average 24.8 ads seen, with a median of 13. Then, we need to look at conversion rate by ad volume:

SELECT 
    CASE 
        WHEN total_ads BETWEEN 1 AND 10 THEN '1-10 ads'
        WHEN total_ads BETWEEN 11 AND 50 THEN '11-50 ads'
        WHEN total_ads BETWEEN 51 AND 100 THEN '51-100 ads'
        ELSE '100+ ads'
    END AS ads_bucket,
    COUNT(*) AS users,
    ROUND(
        SUM(CASE WHEN converted = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 
        2
    ) AS conversion_rate_pct
FROM ab_test
WHERE test_group = 'ad'
GROUP BY ads_bucket
ORDER BY conversion_rate_pct DESC;

/* Conversion rate increases consistently with ad exposure — there is no drop-off at high volumes. 
Users who saw 100 or more ads converted at 17.14%, compared to 0.33% for those who saw fewer than 10.
This raises an important analytical question: are high-frequency users converting because they saw more ads,
or were they already high-intent buyers who happened to encounter more ads along the way?
SQL can show you the correlation. It cannot establish the cause.
That distinction matters when you present findings to a stakeholder. */

-- Which day of the week drives the most conversions?

SELECT 
    most_ads_day,
    COUNT(*) AS users,
    SUM(CASE WHEN converted = TRUE THEN 1 ELSE 0 END) AS conversions,
    ROUND(
        SUM(CASE WHEN converted = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 
        2
    ) AS conversion_rate_pct
FROM ab_test
WHERE test_group = 'ad'
GROUP BY most_ads_day
ORDER BY conversion_rate_pct DESC;

-- Which hour of the day drives the most conversions?

SELECT 
    most_ads_hour,
    COUNT(*) AS users,
    SUM(CASE WHEN converted = TRUE THEN 1 ELSE 0 END) AS conversions,
    ROUND(
        SUM(CASE WHEN converted = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 
        2
    ) AS conversion_rate_pct
FROM ab_test
WHERE test_group = 'ad'
GROUP BY most_ads_hour
ORDER BY conversion_rate_pct DESC;

/* By day: Monday is the strongest at 3.32%, with Saturday the weakest at 2.13%.
The spread across the week is 1.19 percentage points — noticeable but not dramatic.

By hour: The top hours are 16:00 (3.09%) and 20:00 (3.03%), followed closely by 15:00 and 21:00.
Mid-to-late afternoon and early evening consistently outperform other time windows.
That tells a marketing team exactly where to concentrate spend. */

-- We need to calculate the amount of non converting users, so that we can infere statistical measures via PYthon scipy, therefore we need to make a subquery:

SELECT
	total_users,
    converted_users,
    total_users - converted_users as non_converting_users,
    conversion_rate_pct
FROM ( SELECT 
		test_group,
		COUNT(*) AS total_users,
		SUM(CASE WHEN converted = TRUE THEN 1 ELSE 0 END) AS converted_users,
		ROUND(
        SUM(CASE WHEN converted = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 
        2
		) AS conversion_rate_pct
	FROM ab_test
	GROUP BY test_group) AS t;

/* With the results of the last query, we can run the following python codem which will return a chi-square of 54.01 and a p-value of 2e-13:

from scipy.stats import chi2_contingency

contingency = [
    [14423, 550154],  # ad: converted, not converted --> Subquery values in SQL
    [420,   23104]    # psa: converted, not converted --> Subquery values in SQL
]

chi2, p, dof, expected = chi2_contingency(contingency)
print(f"Chi-square: {chi2:.2f}, p-value: {p:.2e}")

The result is highly significant — the probability of seeing a difference this large by chance is essentially zero. This means the ad campaign worked.
The relative lift of 43% is also a number worth putting in front of a stakeholder. It is a much clearer way to communicate impact than the raw rate difference. */

-- To summarise results:

SELECT 
    test_group,
    COUNT(*) AS total_users,
    SUM(CASE WHEN converted = TRUE THEN 1 ELSE 0 END) AS conversions,
    ROUND(
        SUM(CASE WHEN converted = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 
        2
    ) AS conversion_rate_pct,
    ROUND(AVG(total_ads), 1) AS avg_ads_seen
FROM ab_test
GROUP BY test_group;

/* Key findings:

The ad campaign drove a 43% relative lift in conversion rate compared to the control group (2.55% vs 1.79% across 588,000 users)
The difference is statistically significant (chi-square = 54, p < 0.001) — this is not noise
Conversion rate increases steadily with ad frequency, reaching 17% for users who saw 100 or more ads
Monday and mid-to-late afternoon (14:00-16:00) and early evening (20:00-21:00) are the highest-converting windows

*/

-- TO BE REVIEWED AND ADDED TO PORTFOLIO