import csv

in_file_name = "Eskom_Data.csv"
out_file_name = "Eskom_Data_Sorted.csv"   

def clean_data(in_file, out_file):
    with open(in_file) as f_in:
        contents = f_in.read()
        contents = contents.replace(' AM CAT', '')
        contents = contents.replace(' PM CAT', '')
        contents = contents.replace(' (A)', '')
        contents = contents.replace(' (V)', '')
        contents = contents.replace(',"', '')
        contents = contents.replace('timestamp', 'Date,Time')
        contents = contents.replace(' ', ',')
        with open(out_file, 'w') as f_out:
            f_out.write(contents)
            
clean_data(in_file_name, out_file_name)
        
        

