import os

# Specify the path to your notebook
notebook_path = 'PSet4 P4 KTX887.ipynb'

# Run the conversion command
os.system(f'jupyter nbconvert --to pdf "{notebook_path}"')
