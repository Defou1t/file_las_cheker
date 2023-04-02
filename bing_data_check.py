import os
from datetime import datetime


def check_date_in_file(file_path: str):
    file_name = os.path.basename(file_path)
    split_file_name = file_name.split('_')
    date_from_file_name = split_file_name[-3]
    with open(file_path, 'r') as f:
        content = f.read()
    start_index = content.find('DATE.') + 34
    end_index = content.find(':     DATE')
    date_from_content = content[start_index:end_index].strip()
    update_date = False
    try:
        date_from_content = datetime.strptime(date_from_content, '%d/%m/%Y').strftime('%Y-%m-%d')
        if date_from_content != date_from_file_name:
            print(f'Date in file {file_name} is incorrect. Current date: {date_from_content}. Correct date: {date_from_file_name}')
            update_date = True
        #else:
         #   print(f'Date in file {file_name} is correct: {date_from_file_name}')
    except ValueError:
        print(f'Error: Date in file {file_name} does not match expected format. Date in file: {date_from_content}')
        update_date = True
    if update_date:
        user_input = input('Would you like to update the date in the file? (y/n): ')
        if user_input.lower() == 'y':
            new_date = datetime.strptime(date_from_file_name, '%Y-%m-%d').strftime('%d/%m/%Y')
            update_date_in_file(file_path, new_date)
            print(f'Date in file {file_name} has been updated to {new_date}')
        else:
            print(f'Date in file {file_name} was not updated')

def update_date_in_file(file_path: str, new_date: str):
    with open(file_path, 'r') as f:
        content = f.read()
    start_index = content.find('DATE.') + 34
    end_index = content.find(':     DATE')
    date_from_content = content[start_index:end_index]
    new_content = content[:start_index] + new_date.rjust(len(date_from_content)) + content[end_index:]
    with open(file_path, 'w') as f:
        f.write(new_content)

def check_well_in_file(file_path: str):
    file_name = os.path.basename(file_path)
    well_from_file_name = '_'.join(file_name.split('_')[:2])
    with open(file_path, 'r') as f:
        content = f.read()
    start_index = content.find(' WELL. ') + 34
    end_index = content.find(':     WELL')
    well_from_content = content[start_index:end_index].strip()
    if well_from_content != well_from_file_name:
        print(f'Error: WELL in file {file_name} is incorrect. Current WELL: {well_from_content}. Correct WELL: {well_from_file_name}')
    #else:
        #print(f'WELL in file {file_name} is correct: {well_from_file_name}')
        #print('WELL in all files in correct')

def check_fld_in_file(file_path: str):
    file_name = os.path.basename(file_path)
    fld_from_file_name = file_name.split('_')[0]
    with open(file_path, 'r') as f:
        content = f.read()
    start_index = content.find(' FLD .') + 34
    end_index = content.find(':     FIELD')
    fld_from_content = content[start_index:end_index].strip()
    if fld_from_content != fld_from_file_name:
        print(f'Error: FLD in file {file_name} is incorrect. Current FLD: {fld_from_content}. Correct FLD: {fld_from_file_name}')
    #else:
     #   print(f'FLD in file {file_name} is correct: {fld_from_file_name}')

def check_ctry_in_file(file_path: str):
    file_name = os.path.basename(file_path)
    with open(file_path, 'r') as f:
        content = f.read()
    start_index = content.find(' CTRY.') + 34
    end_index = content.find(':     COUNTRY')
    ctry_from_content = content[start_index:end_index].strip()
    if ctry_from_content != 'Ukraine':
        print(f'Error: CTRY in file {file_name} is incorrect. Current CTRY: {ctry_from_content}. Correct CTRY: Ukraine')
    #else:
        #print(f'CTRY in file {file_name} is correct: Ukraine')

def check_all_fields_in_file(parent_folder: str):

    las_folder = os.path.join(parent_folder, 'las')
    for file_name in os.listdir(las_folder):
        if file_name.endswith('.las'):
            file_path = os.path.join(las_folder, file_name)
            check_well_in_file(file_path)
            check_fld_in_file(file_path)
            check_ctry_in_file(file_path)
            check_date_in_file(file_path)
    print('All is correct')

check_all_fields_in_file(input('Folder:'))