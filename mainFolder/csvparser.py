import re
from pathlib import Path
import pandas    # This libraray allows us to work with datasets

Usecols = ["Bedroom", "Outdoor", "Living Room", "Kitchen", "City"]

# This finds the exact folder where your script is currently saved
SCRIPT_DIR = Path(__file__).resolve().parent

# This points to 'locations.csv' inside that same folder
csv_path = SCRIPT_DIR / "locations.csv"

# Now read the dataframe using the smart path
dataframe = pandas.read_csv(csv_path, usecols=Usecols)

##Add ask user which description                                                                                                                  
terms =  ["Child"]

company_names_pattern = "|".join(re.escape(key_word.lower()) for key_word in terms)
company_names_refined_dataframe = dataframe[dataframe[Usecols].apply(lambda x: x.str.lower().str.contains(company_names_pattern, na=False, regex=True)).any(axis=1)]     # this will only produce APKs who have one of the key terms
company_names_refined_dataframe.to_csv("small_sample_refined.csv", index = False)
