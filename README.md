# README: AI-Powered File and Folder Search Tool  

This project is a **real-time file and folder search tool** with **AI-based fuzzy matching**, allowing users to search for files across all available drives efficiently. It utilizes **RapidFuzz** for approximate matching, **multi-threading** for fast searching, and a **Tkinter GUI** for easy interaction.

---

## Features  
- **Search Across All Drives**: Automatically scans all available drives (C:\, D:\, etc.).  
- **AI-Powered Fuzzy Matching**: Finds close matches even if the exact name is unknown.  
- **Exact Match Detection**: Lists files that match the input name exactly.  
- **Subset Results with Match Scores**: Displays similar file names along with a percentage similarity score.  
- **Clipboard Copy**: Easily copy the exact match file paths.  
- **Multi-Threaded Performance**: Improves speed by scanning multiple drives in parallel.  

---

## Use Cases  
1. **Quick File Retrieval**: Find misplaced or forgotten files and folders.  
2. **Partial Name Search**: Locate files even if you remember only part of their name.  
3. **Data Recovery**: Search for lost files after accidental deletion (if not permanently erased).  
4. **Large Storage Management**: Useful for users managing multiple drives or large datasets.  
5. **Enhancing Search Speed**: AI-based fuzzy matching improves search accuracy and efficiency.  
6. **Digital Forensics**: Identify specific files by their approximate names in an investigation.  

---

## Prerequisites  
- **Windows OS** (Tested on Windows 10/11)  
- **Python 3.8 or higher**  

---

## Installation  
1. **Clone the repository** or copy the script file to your system:  
   ```bash
   git clone https://github.com/your-repo/FileSearchTool.git  
   cd FileSearchTool  
   ```  
2. **Install required dependencies**:  
   ```bash
   pip install rapidfuzz tkinter  
   ```  
   *(Tkinter is included with Python by default, but ensure it's installed.)*  

---

## How to Run  
1. Save the script as `file_search.py`.  
2. Run the script using:  
   ```bash
   python file_search.py  
   ```  

---

## How to Use  
1. **Enter a file or folder name** in the input field.  
2. **Press "Enter"** or click the **"Search"** button.  
3. The tool will scan **all available drives** and display:  
   - **Exact Matches** (if found).  
   - **Subset Results** with match scores (if similar files exist).  
4. **Click "Copy Exact Matches"** to copy file paths to the clipboard.  

---

## Key Components  
- **`search_files(start_directory, search_name, results_queue, exact_matches)`**  
  - Recursively searches for files and folders using fuzzy matching.  
- **`real_time_search_gui(search_name, exact_match_var, subset_text)`**  
  - Manages real-time searching across multiple drives.  
- **Multi-threading** is used to speed up the search process.  
- **Tkinter GUI** provides an easy-to-use interface.  

---

## Known Limitations  
- Requires **permission** to scan some system directories.  
- Large storage devices may take longer to scan.  
- Fuzzy matching may produce **false positives** if the threshold is too low.  

---

## Example Output  
Upon running the tool, the window will display:  
- **Exact Matches:** `C:\Users\Documents\example.txt`  
- **Subset Results:**  
  ```
  C:\Backup\example_backup.txt (Match Score: 85%)
  D:\Projects\example_v2.txt (Match Score: 82%)
  ```

---

## Closing the Application  
- Click the **"X"** button on the window or press **`Ctrl + C`** in the terminal.  

---

Enjoy fast and AI-powered file searching! 🚀
