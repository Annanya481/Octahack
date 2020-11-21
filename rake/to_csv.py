from rake_ext import final_out
import pandas as pd 
import numpy as np



def get_note(path):
    df = pd.read_csv(path)
    locations = np.array(df["LOCATION"])
    
    Note = np.array(df["NOTE"])
    rake_out = []
    
    for i in Note:
        key_word = final_out(i)
    
        rake_out.append(key_word)

    df_new = pd.DataFrame(locations)
    df_new["NOTE"] = rake_out

    df_new.columns = ["Location", "Keywords"]
    df_new.to_csv("key_location.csv", index=False)
