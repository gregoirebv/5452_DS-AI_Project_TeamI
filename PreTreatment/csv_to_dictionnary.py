import pandas as pd

# 1. Configuration et lecture du fichier CSV
file_path = "PreTreatment//contentious subjects classification.csv"
# Utilisation de quotechar et on_bad_lines pour éviter les erreurs de lecture
df = pd.read_csv(file_path, sep=';', quotechar='"', on_bad_lines='skip')

# Dictionnaire intermédiaire pour stocker les données nettoyées
topics = {}

# 2. Extraction et nettoyage des données
for index, row in df.iterrows():
    sub_cat = row['(Sub-Category)']
    nlp_words_raw = row['Key NLP words targets']
    
    # On ignore les lignes où la sous-catégorie ou les mots-clés sont vides
    if pd.isna(sub_cat) or pd.isna(nlp_words_raw):
        continue
        
    sub_cat = str(sub_cat).strip()
    words_str = str(nlp_words_raw).strip()
    
    # Nettoyage des guillemets d'encadrement générés par le format CSV
    while words_str.startswith('"') and words_str.endswith('"'):
        words_str = words_str[1:-1]
        
    # Séparation par virgule et nettoyage individuel de chaque mot
    # On enlève les espaces et les guillemets (simples ou doubles) autour de chaque mot
    words_list = [w.strip().strip('"\'') for w in words_str.split(',')]
    words_list = [w for w in words_list if w] # Exclusion des potentiels éléments vides
    
    topics[sub_cat] = words_list

# 3. Formatage et écriture du résultat (exactement comme demandé)
# Nous allons écrire le résultat dans un fichier texte/python pour pouvoir le récupérer facilement
output_file = "OriginalDataSets\\env_topics.py"

with open(output_file, "w", encoding="utf-8") as f:
    f.write("topics = {\n")
    
    items = list(topics.items())
    for i, (sub_cat, words) in enumerate(items):
        f.write(f'    "{sub_cat}": [\n')
        
        # Formatage avec retours à la ligne (ex: 4 mots par ligne pour la lisibilité)
        chunk_size = 4
        for j in range(0, len(words), chunk_size):
            chunk = words[j:j+chunk_size]
            # Rajoute les guillemets autour de chaque mot
            chunk_formatted = ", ".join([f'"{w}"' for w in chunk])
            
            # Si ce n'est pas la dernière ligne de mots de cette sous-catégorie, on met une virgule
            if j + chunk_size < len(words):
                f.write(f'        {chunk_formatted},\n')
            else:
                f.write(f'        {chunk_formatted}\n')
                
        # Si ce n'est pas la dernière sous-catégorie du dico, on ferme avec une virgule et on saute une ligne
        if i < len(items) - 1:
            f.write('    ],\n\n')
        else:
            f.write('    ]\n')
            
    f.write("}\n")

print(f"Extraction terminée avec succès ! Le résultat a été sauvegardé dans '{output_file}'.")