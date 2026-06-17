# This script cleans the CSV file of Snopes articles for treatment purposes. Troubleshooting of encoding issues with the help of ChatGPT4.0
import pandas as pd

df = pd.read_csv(
    "OriginalDataSets\\snopes_checked_v02.csv",
    encoding="cp1252" #problem with the UTF-8 encoding, resolved with help of ChatGPT4.0
)

df_clean = df[[
    "article_origin_url_phase1",
    "original_article_text_phase2"
]].rename(columns={
    "article_origin_url_phase1": "URL",
    "original_article_text_phase2": "ArticleText"
})

df_clean.to_csv("Notebooks\\clean-snopes_checked_v02.csv", index=False)

print(df_clean.head())

print("Done!")