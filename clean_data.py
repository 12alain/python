from chargement import download_data
def missing_values_and_duplicated(datas):
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
    return datas
missing_values_and_duplicated(download_data())
