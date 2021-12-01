from datetime import datetime
from pathlib import Path
import tinify
import time

#Enter the tinijpg API key here
tinify.key = ''
#Enter the path for the directory that contains the folder with images
our_directory = Path('/home/bharathg/Documents/Work/Detailers-India/Product-Images-renamed')

#Iterating through the folders in parent directory
for direc in our_directory.iterdir():
    count = 1
    #iterating through the image files contained in each directory
    for files in direc.iterdir():
    	
    	#getting details about the directories
        directory_name = files.parent.name
        directory = files.parent 
        #getting the extension of the file
        ext = files.suffix
        
        #Formatting the new name
        new_name = (directory_name + '-' + str(count) + ext).lower().replace(" ", "-")
        print(f'{files} has been renamed to {new_name}')
        count += 1
        #renaming the file
        files.rename(Path(directory, new_name))
        

print('\n\nThe files have been renamed')
input('press enter to continue to compress the images')
for direc in our_directory.iterdir():
    for files in direc.iterdir():
        print(f'Compressing {files.name}...')
        source = tinify.from_file(files)
        source.to_file(files)
        print(f'Successfully compressed {files}')
        time.sleep(1)


print(f'We have used {tinify.compression_count} compressions out of 500 for this month')


