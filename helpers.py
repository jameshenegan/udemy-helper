def clear_terminal():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

def make_intro_text_0():
    print("-------------------------")
    print("Udemy Course Info Scraper")
    print("-------------------------")
    print("")
    print("We will convert the contents of 'sample.txt' to a CSV file.")

def make_intro_text_1():        
    print("What should the name of the CSV file be?")
    print("For example, type 'section11' to create 'section11.csv'")
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