import pandas as pd
from helpers import *
import os

###################################
# Where is your text file located?
###################################
file_to_read = os.path.join("..", "txt", "sample_lessons.txt")

###################################
# Make introduction text
###################################

clear_terminal()
make_intro_text_0()

####################################
# Ask for the name of output file
####################################

make_intro_text_1()
file_to_save = input("Output file name:  ") + ".csv"
file_to_save = os.path.join("..", "csv", file_to_save)
clear_terminal()

###############################################
# Ask for the name of the Section in the course
###############################################

make_intro_text_2()
section_name = input("Section Name:  ")

################################################
# Load in the text from the file
################################################

text_from_file = get_text(file_to_read) 

################################################
# Extract relevant data from the text
################################################

(lesson_names,lengths) = get_titles_and_lengths(text_from_file)
clear_terminal()

#################################################
# Make a dataframe out the data
#################################################

df = pd.DataFrame(
    list(zip(lesson_names, lengths)),
    columns= ["Lesson", "Time"]
    )

df['Section'] = section_name
df = df[['Section', 'Lesson', 'Time']]

##################################################
# Save the Dataframe to a CSV file
##################################################

df.to_csv(file_to_save, index = False)

print("File created!")