from chargement import download_data

import os 

def missing_values_and_duplicated():
  datas=download_data()
  for i in datas.columns:
    p=datas[i].isnull().sum()
    if p!=0:
      if datas[i].dtype in [int, float]:
         datas[i].fillna(value=datas[i].mean(),inplace=True)
      else :
        mode_value = datas[i].mode()[0]
        datas[i].fillna(value=mode_value, inplace=True)
    # Traitement des valeurs dupliquées
  datas.drop_duplicates(inplace=True)
  #creaton du dossier data_cleaned si il n'existe pas 
  if not os.path.exists('data_cleaned'):
    os.makedirs('data_cleaned')
  # chemin du fichier 
  csv=os.path.join('data_cleaned','data_cleaned.csv')

  # stoc les valeurs da 
  datas.to_csv(csv,index=False)
  return "data_clean.csv"

