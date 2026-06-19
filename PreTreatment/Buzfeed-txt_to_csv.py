# This script converts a tab-separated text file of Buzzfeed articles into a CSV file for treatment purposes
import csv

input_path = "../OriginalDataSets/buzzfeed-v02.txt"
output_path = "../Notebooks/clean-buzzfeed-v02.csv"

rows = []
with open(input_path, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) < 4:
            continue
        
        url = parts[1]
        article_text = parts[3]
              
        rows.append([
            url, 
            article_text
            ])

with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["URL", "ArticleText"])
    writer.writerows(rows)

print("Done! Saved to:", output_path)