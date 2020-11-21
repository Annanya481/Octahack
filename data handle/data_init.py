from rake_ext import final_out
import pandas as pd 
import numpy as np 

def initial_input(csv_path):
    df = pd.read_csv(csv_path)
    note = np.array(df['Note'])
    loacation = np.array(df['Location'])
    return loacation[0], final_out(note[0])
