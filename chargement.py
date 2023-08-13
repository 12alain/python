import urllib.request 
import pandas as pd
def download_data():
        url = ('https://raw.githubusercontent.com/12alain/python/master/data/billets.csv')  # URL du fichier à télécharger
        filename, headers = urllib.request.urlretrieve(url, "billets.csv")
        df=pd.read_csv(filename,sep=";")
        return df
download_data()
print(download_data())