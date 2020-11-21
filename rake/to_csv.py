from rake_ext import final_out
import pandas as pd 
import numpy as np

# lst_1 = []
# lst_2 = []
# lst_1.append("Bangalore")
# lst_1.append("PUNE")
# lst_2.append('Writers write descriptive paragraphs because their purpose is to describe something. Their point is that something is beautiful or disgusting or strangely intriguing. Writers write persuasive and argument paragraphs because their purpose is to persuade or convince someone. Their point is that their reader should see things a particular way and possibly take action on that new way of seeing things. Writers write paragraphs of comparison because the comparison will make their point clear to their readers')
# lst_2.append("On July 16, 1969, the Apollo 11 spacecraft launched from the Kennedy Space Center in Florida. Its mission was to go where no human being had gone before—the moon! The crew consisted of Neil Armstrong, Michael Collins, and Buzz Aldrin. The spacecraft landed on the moon in the Sea of Tranquility, a basaltic flood plain, on July 20, 1969. The moonwalk took place the following day. On July 21, 1969, at precisely 10:56 EDT, Commander Neil Armstrong emerged from the Lunar Module and took his famous first step onto the moon’s surface. He declared, “That’s one small step for man, one giant leap for mankind.” It was a monumental moment in human history!")
# df = pd.DataFrame(lst_1)

# df['NOTE'] = lst_2
# df.columns = ['LOCATION', "NOTE"]

# df.to_csv('test.csv', index=False)

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
