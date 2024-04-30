from PyPDF2 import PdfWriter
import os
import glob

# Set filepath
filepath = 'C:/Users/laura/Downloads'
os.chdir(filepath)

# Define merger
merger = PdfWriter()

# Create for loop where file type = pdf
for file in glob.glob("*.pdf"):
    # File name has to contain a certain word
    if file.__contains__('factuur'):
        # Add those matching files to a new combined file
        merger.append(file)
        merger.write('combined_file.pdf')
        merger.close()

print("Merging completed!")
