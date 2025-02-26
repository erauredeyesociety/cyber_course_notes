import os
import shutil

def move_and_rename_assets(base_path):
    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)
        gitbook_assets_path = os.path.join(folder_path, ".gitbook", "assets")
        
        if os.path.isdir(folder_path) and os.path.isdir(gitbook_assets_path):
            new_assets_path = os.path.join(folder_path, f"{folder}assets")
            
            # Move assets to new location
            if os.path.exists(new_assets_path):
                shutil.rmtree(new_assets_path)  # Remove existing folder if necessary
            shutil.move(gitbook_assets_path, new_assets_path)
            
            # Remove the now empty .gitbook directory
            gitbook_path = os.path.join(folder_path, ".gitbook")
            shutil.rmtree(gitbook_path, ignore_errors=True)
            
            # Update .md files
            update_markdown_files(folder_path, folder)
            
            print(f"Moved and renamed assets: {gitbook_assets_path} -> {new_assets_path}")

def update_markdown_files(folder_path, folder_name):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        
        if file.endswith(".md") and os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            updated_content = content.replace(".gitbook/assets/", f"{folder_name}assets/")
            
            if updated_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)
                print(f"Updated markdown file: {file_path}")

if __name__ == "__main__":
    base_directory = os.getcwd()  # Change this if running from a different directory
    move_and_rename_assets(base_directory)
    print("Process completed!")
