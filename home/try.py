import os

# Check if the path exist

folder_path = r"C:\Users\gayat\OneDrive\Desktop\Manjeet Dokumente\Udacity\Projects\Project1\Project1_AC\home\pet_images"
jpg_files = []

if os.path.exists(folder_path):
    print("Path exists!")
else:
    print("Path does not exist!")

# printing the contents of the pet_images folder

for filename in os.listdir(folder_path):
    if filename.endswith('.jpg'):
        jpg_files.append(filename)
        print(f"Added: {filename}")

print(f"Total .jpg files found: {len(jpg_files)}")




