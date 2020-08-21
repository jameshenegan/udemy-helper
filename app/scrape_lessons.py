import pandas as pd
from helpers import *
import os

file_to_read = os.path.join("..", "txt", "sample_lessons.txt")

clear_terminal()
make_intro_text_0()

make_intro_text_1()
file_to_save = input("Output file name:  ") + ".csv"
file_to_save = os.path.join("..", "csv", file_to_save)

clear_terminal()
make_intro_text_2()
section_name = input("Section Name:  ")

text_from_file = get_text(file_to_read) 

(lesson_names,lengths) = get_titles_and_lengths(text_from_file)

clear_terminal()

df = pd.DataFrame(
    list(zip(lesson_names, lengths)),
    columns= ["Lesson", "Time"]
    )

df['Section'] = section_name
df = df[['Section', 'Lesson', 'Time']]

df.to_csv(file_to_save, index = False)


print("File created!")