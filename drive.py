from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 
import os 

# Authenticate with Google Drive
gauth = GoogleAuth() 
gauth.LocalWebserverAuth()     
drive = GoogleDrive(gauth) 

# Path to the directory containing files to upload
path = r"C:\Users\manav\OneDrive\Desktop\Nesscale Solution"

# Function to upload files to Google Drive
def upload_to_drive(file_path):
    try:
        # Extract file name from path
        file_name = os.path.basename(file_path)
        
        # Create Google Drive file object
        f = drive.CreateFile({'title': file_name}) 
        
        # Set content of the file
        f.SetContentFile(file_path) 
        
        # Upload the file to Google Drive
        f.Upload() 
        
        # Print the URL of the uploaded file
        print(f"Uploaded {file_name} to Google Drive successfully.")
        print("File URL:", f['alternateLink'])
        
    except Exception as e:
        print(f"Error uploading {file_path}: {e}")

# Iterate through files in the directory
for x in os.listdir(path):
    file_path = os.path.join(path, x)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue
     
    # Upload the file
    upload_to_drive(file_path)
