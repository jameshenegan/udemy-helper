import pandas as pd
from helpers import *

file_to_read = "sample_sections.txt"

clear_terminal()
make_intro_text_0_sections()

make_intro_text_1()
file_to_save = input("Output file name:  ") + ".csv"

text_from_file = get_text(file_to_read) 

(section_names,lengths) = get_section_titles_and_lengths(text_from_file)


df = pd.DataFrame(
    list(zip(section_names, lengths)),
    columns= ["Section", "Time"]
    )

df = df[['Section', 'Time']]

df.to_csv(file_to_save, index = False)

print("File created!")