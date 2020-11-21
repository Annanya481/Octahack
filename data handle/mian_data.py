import pandas as pd 
import numpy as np
from data_init import initial_input

def main_data(db_path):
    data = initial_input("rake/loc.csv")

    key_words = ", ".join(data[1])
    
    df_main = pd.read_csv(db_path)
    df_main = df_main.append({"Location":data[0], "Keywords":key_words},ignore_index=True)
    
    df_main.to_csv(db_path, index=False)
    
main_data("/home/aradhya/Desktop/hacks/octahack/rake/key_location.csv") 
