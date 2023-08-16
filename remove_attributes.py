from download import download_data
def remove_attribut():
    # Load the data using the download_data() function
    data = download_data()

    # List of attributes that are not needed
    cols_to_remove = ['length', 'margin_up']
    
    # Loop through the columns to remove
    for col in cols_to_remove:
        # Drop the specified column from the DataFrame
        data.drop([col], axis=1, inplace=True)
    
    # Return the modified data after attribute removal
    return data

