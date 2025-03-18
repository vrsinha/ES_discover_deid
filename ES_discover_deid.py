import re
import pickle
import os

#with open('/Users/vrsinha/montageextractor/ES_discover_deid/num_counter.pickle', mode='rb') as f:
    #counter = pickle.load(f)
counter = 1
print(counter)
directory = "/Users/vrsinha/montageextractor/ES_discover_deid/prac_copycopy/"

for root, dirs, files in os.walk(directory, topdown=False):
    for filename in files:
        old_file_path = os.path.join(root, filename)
        if " " in filename:
            match = re.findall(r'HUP\s\d+', filename)
            if len(match) == 0:
                print("keep")
            else:
                new_filename = re.sub(match[0], "EPS-" + str(counter), filename, count=1)
                new_file_path = os.path.join(root, new_filename)
            if old_file_path != new_file_path:
                os.rename(old_file_path, new_file_path)
        else:
            match = re.findall(r'sub-[a-zA-Z0-9]*', filename)
            if len(match) == 0:
                print("keep")
            else:
                new_filename = re.sub(match[0], "EPS-" + str(counter), filename, count=1)
                new_file_path = os.path.join(root, new_filename)
                os.rename(old_file_path, new_file_path)
                print(new_file_path)
            #if old_file_path != new_file_path:
            #    os.rename(old_file_path, new_file_path)
            #    print(new_file_path)
        
        
        for dirname in dirs:
            old_dir_path = os.path.join(root, dirname)
            match = re.findall(r'sub-[a-zA-Z0-9]*', dirname)
            if len(match) == 0:
                print("keep")
            else:
                new_dirname = re.sub(match[0], "EPS-" + str(counter), dirname, count=1)
                new_dir_path = os.path.join(root, new_dirname)    
                if old_dir_path != new_dir_path:
                    os.rename(old_dir_path, new_dir_path)
counter += 1
print(counter)
#with open('num_counter.pkl', mode='wb') as f:
#    counter = pickle.load(f)
            

#input_list = ["HUP 89_annotations_file1.txt", "HUP89b_phaseII", "dataset_description.json", "sub-HUP89b", "ses-01012000", "sub-CNT89b-ses-01012000_run-01_ct.nii", "sub-HUP89_ses-01012000_task-rest_run-0000.edf"]
#for file in input_list:
#    if ' ' in file: 
#        match = re.findall(r'HUP\s\d+', file) #removes w. white space
#        print(file)
#        print(match)
#        if len(match) == 0:
#            print("keep name: " + file)
#        else:
#            new_name = re.sub(match[0], "EPS-" + str(counter), file, count=1)
#            print("New name: " + new_name)
#    else:
#        match = re.findall(r'sub-[a-zA-Z0-9]*', file) #doesn't care about white space sub-HUP\d+
#        print(file)
#        print(match)
#        if len(match) == 0:
#            print("keep name: " + file)
#        else:
#            new_name = re.sub(match[0], "sub-EPS-" + str(counter), file, count=1)
#            print("New name: " + new_name)
#counter += 1
#with open('num_counter.pkl', mode='wb') as f:
#    counter = pickle.load(f)
#exec find