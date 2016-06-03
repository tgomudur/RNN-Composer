
# coding: utf-8

# # Data PreProcessing

# This script is used to create the input.txt needed for training the char-rnn. Here, we will remove all the metadata in the .krn files and keep only the musical notes information from each file and create a single large file. The resulting file will be used as input for the char-rnn.

# In[2]:

# Lets initialize all the imports and file paths
import os
import glob

INPUT_PATH = "../Dataset/"
OUTPUT_PATH = "../RNN/data/music_scores/"
OUTPUT_FILENAME = "input.txt"
MEASURE_MARKER = "@\n"


# In[10]:

# Using glob to do unixstyle pattern matching to get all the '.krn' files

krn_files = glob.glob(INPUT_PATH + '*/*.krn')
#print len(krn_files)


# In[12]:

for file in krn_files:
    buffer = []
    print file
    with open(file) as infile:
        lines = infile.readlines()
        found_first = False
        for line in lines:
            # Ignoring metadata
            if line.startswith('!'):
                continue
            # Marking measures
            elif line.startswith('='):
                buffer.append(MEASURE_MARKER)
                found_first = True
            else:
                if found_first:
                    buffer.append(line)
    if not os.path.exists(os.path.dirname(OUTPUT_PATH)):
        os.makedirs(os.path.dirname(OUTPUT_PATH))
    with open(OUTPUT_PATH + OUTPUT_FILENAME, 'a+') as outfile:
        outfile.writelines(buffer)

print "Done"


# In[ ]:




# In[ ]:




# In[ ]:



