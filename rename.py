import os

def rename_html_and_folder():
    # Get user input for renaming
    old_html_path = input("Enter the full path of the HTML file: ").strip()
    
    # Remove quotes if present at the start and end
    if old_html_path.startswith('"') and old_html_path.endswith('"'):
        old_html_path = old_html_path[1:-1]
    
    new_html_name = input("Enter the new HTML file name (without extension): ").strip()
    new_html_name += ".html"  # Ensure .html extension is added

    # Extract directory and old file name
    dir_path = os.path.dirname(old_html_path)
    old_html_name = os.path.basename(old_html_path)
    old_folder_name = old_html_name.rsplit('.', 1)[0] + "_files"  # Remove .html but no _files at the end
    new_folder_name = new_html_name.rsplit('.', 1)[0]  # Keep same logic for new folder
    new_html_path = os.path.join(dir_path, new_html_name)
    old_folder_path = os.path.join(dir_path, old_folder_name)
    new_folder_path = os.path.join(dir_path, new_folder_name)

    # Check if the HTML file exists
    if not os.path.exists(old_html_path):
        print(f"Error: {old_html_path} not found!")
        return

    # Rename the HTML file
    try:
        os.rename(old_html_path, new_html_path)
        print(f"Renamed {old_html_path} to {new_html_path}")
    except Exception as e:
        print(f"Error renaming file: {e}")
        return

    # Rename the corresponding folder
    if os.path.exists(old_folder_path) and os.path.isdir(old_folder_path):
        try:
            os.rename(old_folder_path, new_folder_path)
            print(f"Renamed folder {old_folder_path} to {new_folder_name}")
        except Exception as e:
            print(f"Error renaming folder: {e}")
    else:
        print(f"Warning: Folder {old_folder_path} not found!")

    # Update references inside the HTML file
    try:
        with open(new_html_path, "r", encoding="utf-8") as file:
            content = file.read()

        content = content.replace(old_folder_name, new_folder_name)

        with open(new_html_path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"Updated references inside {new_html_name}")

    except Exception as e:
        print(f"Error updating HTML content: {e}")

# Run the function
if __name__ == "__main__":
    while True:
        start = input("Start (Y) or Stop (N)? :").strip().lower()
        if start == 'y':
            rename_html_and_folder()
        else:
            print("Exiting program.")
            break

