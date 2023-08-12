import pandas as pd   
def download_data():
        df=pd.read_csv('./data/billets.csv',sep=";")
        return df
