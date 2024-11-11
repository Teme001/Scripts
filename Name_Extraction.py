import os

def extract_names_from_filenames(folder_path, prefix_to_remove, output_file):
    # List to store extracted names without the prefix
    cleaned_names = []

    # Loop through each file in the specified folder
    for filename in os.listdir(folder_path):
        # Check if filename starts with the prefix and is a file
        if filename.startswith(prefix_to_remove) and os.path.isfile(os.path.join(folder_path, filename)):
            # Remove the prefix from the filename
            cleaned_name = filename[len(prefix_to_remove):]  # Slice off the prefix
            cleaned_names.append(cleaned_name)

    # Write all cleaned names to the output file
    with open(output_file, 'w') as out_file:
        for name in cleaned_names:
            out_file.write(name + '\n')

# Set the folder path to the 'hello' folder in the current directory
folder_path = './test/chat_history'
prefix_to_remove = 'subpage_'
output_file = 'output_names_chatHistory.txt'

# Run the extraction
extract_names_from_filenames(folder_path, prefix_to_remove, output_file)
