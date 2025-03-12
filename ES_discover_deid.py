import re
import pickle

with open('num_counter.pkl', mode='rb') as f:
    counter = pickle.load(f)
print(counter)

input_list = ["HUP 89_annotations_file1.txt", "HUP89b_phaseII", "dataset_description.json", "sub-HUP89b", "ses-01012000", "sub-CNT89b-ses-01012000_run-01_ct.nii", "sub-HUP89_ses-01012000_task-rest_run-0000.edf"]
for file in input_list:
    if ' ' in file: 
        match = re.findall(r'HUP\s\d+', file) #removes w. white space
        print(file)
        print(match)
        if len(match) == 0:
            print("keep name: " + file)
        else:
            new_name = re.sub(match[0], "EPS-" + str(counter), file, count=1)
            print("New name: " + new_name)
    else:
        match = re.findall(r'sub-[a-zA-Z0-9]*', file) #doesn't care about white space sub-HUP\d+
        print(file)
        print(match)
        if len(match) == 0:
            print("keep name: " + file)
        else:
            new_name = re.sub(match[0], "sub-EPS-" + str(counter), file, count=1)
            print("New name: " + new_name)
counter += 1
#exec find