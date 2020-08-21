def get_hours(your_list):
    if len(your_list) == 2:
        return your_list[0]
    else:
        return "0hr"

def get_minutes(your_list):
    if len(your_list) == 1:
        return your_list[0]
    else:
        return your_list[1]

def clean_time(df):
    time_col = df['Time']
    split_time_col = time_col.str.split()

    df['hours'] = split_time_col.apply(lambda x : get_hours(x))
    df['minutes'] = split_time_col.apply(lambda x : get_minutes(x))

    df['hours'] = df['hours'].apply(lambda x: x[0])
    df['minutes'] = df['minutes'].apply(lambda x: x[:-3])

    return df        

def clear_terminal():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

def make_intro_text_0():
    print("-------------------------")
    print("Udemy Course Info Scraper")
    print("-------------------------")
    print("")
    print("We will convert the contents of 'sample_lessons.txt' to a CSV file.")

def make_intro_text_0_sections():
    print("-------------------------")
    print("Udemy Course Info Scraper")
    print("-------------------------")
    print("")
    print("We will convert the contents of 'sample_sections.txt' to a CSV file.")    

def make_intro_text_1():        
    print("What should the name of the CSV file be?")
    print("For example, type 'file' to create 'file.csv'")
    print("")

def make_intro_text_2():    
    print("What is the name of the section?")
    print("Example: 11. Microservice Architectures")
    print("")

def get_text(file_name):

    text = ""

    with open(file_name,'r') as file:
        text = file.read()

    return text

def get_titles_and_lengths(text):

    split_string = text.split("\n")

    section_names = []
    lengths = []

    for j in range(len(split_string)):
        try:
            if split_string[j+1][-3:] == "min":
                section_names.append(split_string[j])
                lengths.append(split_string[j+1][:-3])
        except:
            print("oops")

    return(section_names, lengths)

def get_section_titles_and_lengths(text):

    split_string = text.split("\n")

    begin_desc_line_num = 0
    end_desc_line_num = 0
    description = ""

    descriptions = []
    lengths = []

    for j in range(len(split_string)):
        current_line = split_string[j]

        # if we are on a line that begins with "Section"
        if current_line[:7] == "Section":
            begin_desc_line_num = j
            
        # if we are on a line with information about time ... 
        if current_line[-3:] == "min":


            end_desc_line_num = j - 1            

            # get the time
            time = current_line.split("|")[1]


            # get the lines with the description of the section
            end_desc_line_num = j - 1
            if begin_desc_line_num == end_desc_line_num:
                description = split_string[begin_desc_line_num]
            else:
                description = ""
                for i in range(begin_desc_line_num, end_desc_line_num + 1):
                    description += split_string[i] + " "
            descriptions.append(description)
            lengths.append(time)

    return(descriptions, lengths)    
   