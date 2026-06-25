# Done with AI assistance Gemini 3.1 Pro

import pandas as pd

# CSV file
file_path = "../PreTreatment/contentious subjects classification.csv"
# avoid reading errors
df = pd.read_csv(file_path, sep=';', quotechar='"', on_bad_lines='skip')

# Intermediate dictionary to store cleaned data
topics = {}

# Extraction and cleaning of the data
for index, row in df.iterrows():
    sub_cat = row['(Sub-Category)']
    nlp_words_raw = row['Key NLP words targets']
    
    if pd.isna(sub_cat) or pd.isna(nlp_words_raw):
        continue
        
    sub_cat = str(sub_cat).strip()
    words_str = str(nlp_words_raw).strip()
    
    while words_str.startswith('"') and words_str.endswith('"'):
        words_str = words_str[1:-1]
        
    words_list = [w.strip().strip('"\'') for w in words_str.split(',')]
    words_list = [w for w in words_list if w]  # Exclude potential empty elements
    
    topics[sub_cat] = words_list

# Formatting and writing the result
output_file = "../OriginalDataSets/env_topics.py"

with open(output_file, "w", encoding="utf-8") as f:
    f.write("topics = {\n")
    
    items = list(topics.items())
    for i, (sub_cat, words) in enumerate(items):
        f.write(f'    "{sub_cat}": [\n')
        
        # Formatting with line breaks (e.g., 4 words per line for readability)
        chunk_size = 4
        for j in range(0, len(words), chunk_size):
            chunk = words[j:j+chunk_size]
            # Add quotes around each word
            chunk_formatted = ", ".join([f'"{w}"' for w in chunk])
            
            # If this is not the last line of words for this sub-category, add a comma
            if j + chunk_size < len(words):
                f.write(f'        {chunk_formatted},\n')
            else:
                f.write(f'        {chunk_formatted}\n')
                
        # If this is not the last sub-category in the dict, close with a comma and add a blank line
        if i < len(items) - 1:
            f.write('    ],\n\n')
        else:
            f.write('    ]\n')
            
    f.write("}\n")

print(f"Done! Saved to: '{output_file}'.")