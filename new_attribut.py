from clean_data import missing_values_and_duplicated
from download import download_data
def new_tribut():
    # recuperation des donnee nettoyer
    data=download_data()
    # fabrication de nouveau attribut
    data=data.rename(columns={'is_genuine':'genuine','diagonal':'diagonale'})
    return data

