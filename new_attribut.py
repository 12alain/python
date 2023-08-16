from clean_data import missing_values_and_duplicated
def new_tribut():
    # recuperation des donnee nettoyer
    data=missing_values_and_duplicated()
    # fabrication de nouveau attribut
    data=data.rename(columns={'is_genuine':'genuine','diagonal':'diagonale'})
    return data
