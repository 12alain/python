import sqlite3
from clean_data import missing_values_and_duplicated
def connexion() :
 data=missing_values_and_duplicated()
 # se connecter a la base sqlite
 conn=sqlite3.connect('datas.db')
# stocer le dataframe dans une base de donne 
 data.to_sql('data_cleaned',conn,if_exists='replace',index=False)
 print("Data stored in database")

 conn.close()
connexion()