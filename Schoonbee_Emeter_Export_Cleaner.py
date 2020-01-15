import csv

in_file_name = "Eskom_Data.csv"
out_file_name = "Eskom_Data_Sorted.csv"   

def clean_data(in_file, out_file):
    ''' Removes text that clashes with text to columns '''
    with open(in_file) as f_in:
        contents = f_in.read()
        contents = contents.replace(' AM CAT', '')
        contents = contents.replace(' PM CAT', '')
        contents = contents.replace(' (A)', '')
        contents = contents.replace(' (V)', '')
        contents = contents.replace(',"', '')
        #seperates timestamp to date, time to allow for two columns
        contents = contents.replace('timestamp', 'Date,Time')
        #replaces spaces with commas to allow for date/time seperation
        contents = contents.replace(' ', ',')
        with open(out_file, 'w') as f_out:
            f_out.write(contents)
            
clean_data(in_file_name, out_file_name)
        
        

