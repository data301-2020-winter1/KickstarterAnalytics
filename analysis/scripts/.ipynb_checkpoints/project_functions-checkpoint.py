import pandas as pd

def load_and_process(url_or_path_to_csv_file):

    # We are supposed to add the method chain here      
    df1 = (
        pd.read_csv(url)
        .dropna()
        .assign(GoalReachedPercentage = lambda x: x["pledged"] / x["goal"] * 100)
        .sort_values("GoalReachedPercentage", ascending = False)
        .reset_index(drop=True)
    )
    return df1
          
      
  
    







