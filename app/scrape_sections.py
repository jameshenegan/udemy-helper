import pandas as pd
from helpers import *
import os

def quick_fix(file_to_save):
    df = pd.read_csv(file_to_save)

    section_col = df['Section']

    section_nums_plus = section_col.str.split(":").apply(lambda x: x[0])
    section_nums = section_nums_plus.apply(lambda x: x[7:])

    section_titles = section_col.str.split(":").apply(lambda x: x[1])

    df['SectionNum'] = section_nums
    df['SectionTitle'] = section_titles
    return df[['SectionNum', 'SectionTitle', 'Time']]

file_to_read = os.path.join("..", "txt", "sample_sections.txt")

clear_terminal()
make_intro_text_0_sections()

make_intro_text_1()
file_to_save = input("Output file name:  ") + ".csv"
file_to_save = os.path.join("..", "csv", file_to_save)

text_from_file = get_text(file_to_read) 

(section_names,lengths) = get_section_titles_and_lengths(text_from_file)


df = pd.DataFrame(
    list(zip(section_names, lengths)),
    columns= ["Section", "Time"]
    )

df = df[['Section', 'Time']]

df.to_csv(file_to_save, index = False)

df = quick_fix(file_to_save)

df = clean_time(df)[['SectionNum', 'SectionTitle', 'hours', 'minutes']]

df['minutes'] = df['minutes'].apply(lambda x: int(x)) 
df['hours'] = df['hours'].apply(lambda x: int(x)) 
df['time(minutes)'] = 60 * df['hours'] + df['minutes']
df = df[['SectionNum', 'SectionTitle', 'time(minutes)']]

df.to_csv(file_to_save, index = False)


print("File created!")