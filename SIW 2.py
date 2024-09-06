import numpy as np
import pandas as pd
import webbrowser

# This report is provided for the year 2024
df = pd.read_csv("freedom_index.csv")
all_country = df['Country'].to_numpy()
country_overall_score = dict(zip(df['Country'], df["Overall Score"]))

number_of_country = len(country_overall_score)
print(f"Statistics cover {number_of_country} countries")

# The "overall score" in the context of the Economic Freedom Index represents a composite score that
# summarizes a country's level of economic freedom based on various indicators and metrics.
best_country = max(country_overall_score, key=country_overall_score.get)
max_score = country_overall_score[best_country]

worst_country = min(country_overall_score, key=country_overall_score.get)
min_score = country_overall_score[worst_country]
print(f"The Best country is {best_country} with overall score {max_score}")
print(f"The Worst country is {worst_country} with overall score {min_score}")


def what_score_have_your_country(key):
    try:
        score = country_overall_score[key]
        position = sorted(country_overall_score.values(), reverse=True).index(score) + 1
        print(f"Your country {key} have score {score} and placed on position - {position}")
    except Exception as e:
        print("Incorrect countries name:", e)
        return None


what_score_have_your_country('Kazakhstan')

average_score = np.mean(df["Overall Score"])
median_overall_score = df['Overall Score'].median()
print(f"The average score of all country is - {round(average_score, 2)}")
print(f"The median score of all country is - {round(median_overall_score, 2)}")

print()
top_10_countries = df.sort_values(by='Overall Score', ascending=False).head(10)
bottom_10_countries = df.sort_values(by='Overall Score', ascending=True).head(10)
print("Top 10 Countries by Overall Score:")
print(top_10_countries[['Country', 'Overall Score']])
print()
print("Bottom 10 Countries by Overall Score:")
print(bottom_10_countries[['Country', 'Overall Score']])
print()

unique_country_scores = set()

for index, row in df.iterrows():
    unique_country_scores.add((row['Country'], row['Overall Score']))

print("Unique Country Names and Overall Scores:")
# for country, score in unique_country_scores:
# print(country, score)


result_html = top_10_countries.to_html()
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Economic Freedom Index Analysis</title>
</head>
<body>
    <h1>Top 10 Countries by Overall Score</h1>
    {result_html}
</body>
</html>
"""

# Write the HTML content to a file
with open('analysis_results.html', 'w') as f:
    f.write(html_content)

# Open the HTML file in the default web browser
webbrowser.open('analysis_results.html')




