#not finished
# TODO: HOW TO HANDLE FAILED FILE

#list the filename in the directory
from os import listdir
#to filter flie name
import re


directory_path = '/Users/panxuanyou/Downloads/偵查科技/'
filename_list = listdir(directory_path)
print(filename_list)

pattern = r'^IMG_[0-9]+'
#matched_filename_list = [re.match(pattern, filename).group() for filename in filename_list]

matched_filename_list = [filename for filename in filename_list if re.match(pattern, filename)]
print(matched_filename_list)

pattern2 = r'[0-9]+'
num_matched_filename_list = [int(re.compile(pattern2).search(elm).group()) for elm in matched_filename_list]
num_matched_filename_list.sort()
print(num_matched_filename_list)

extension_string = '.JPG'

filepath_gnr = (directory_path + 'IMG_' + str(filename) + extension_string for filename in num_matched_filename_list)
filename_of_incremental_num_gnr = (str(i) for i in range(1,len(num_matched_filename_list)+1))
for p in filepath_gnr:
    print(p)
for n in filename_of_incremental_num_gnr:
    print(n)


filepath_and_out_num = [(filepath, out_num) for filepath, out_num in zip(filepath_gnr, filename_of_incremental_num_gnr)]




def rename_to_incremental_num_from_one():
    for filepath, out_num in filepath_and_out_num:
        with open(filepath, 'rb') as fin:
            with open((directory_path + out_num + extension_string), 'wb') as fout:
                fout.write(fin.read())

def main():
    execute_anyway_until_there_is_not_file_to_rename = True
    while execute_anyway_until_there_is_not_file_to_rename:
        try:
            rename_to_incremental_num_from_one()
        except:
            break

if __name__ == '__main__':
    main()







