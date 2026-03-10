
from huggingface_hub import HfApi
import os

print("--- Starting V2 upload script ---")
try:
    # HfApi automatically finds the token from `huggingface-cli login`
    print("Initializing HfApi...")
    api = HfApi()
    
    folder_to_upload = "hf-earn"
    
    print(f"Files to be uploaded from '{folder_to_upload}': {os.listdir(folder_to_upload)}")

    repo_url = api.upload_folder(
        folder_path=folder_to_upload,
        repo_id="msjhon/earn",
        repo_type="space",
        commit_message="Upload app files via corrected Python script"
    )
    print(f"\nSUCCESS! Your files have been uploaded to the Space.")
    print(f"You can view your space here: {repo_url}")

except Exception as e:
    print(f"\n--- AN ERROR OCCURRED ---")
    if "401" in str(e):
         print("Error details: Authorization failed (401 Client Error).")
         print("Please make sure you are logged in. Run 'huggingface-cli login' and try again.")
    else:
         print(f"Error details: {e}")
    print("-------------------------")

print("--- Upload script finished ---")
