import os
import threading
import queue
from rapidfuzz import fuzz
import tkinter as tk
from tkinter import messagebox, scrolledtext

def search_files(start_directory, search_name, results_queue, exact_matches):
    """Search for files or folders in a directory recursively with AI-based fuzzy matching."""
    try:
        for root, dirs, files in os.walk(start_directory):
            # Check for matching files and folders using fuzzy matching
            for name in files + dirs:
                match_score = fuzz.partial_ratio(search_name.lower(), name.lower())
                if match_score > 80:  # Threshold for a match (can be adjusted)
                    result_path = os.path.join(root, name)
                    if name.lower() == search_name.lower():
                        exact_matches.append(result_path)
                    else:
                        results_queue.put((result_path, match_score))
    except PermissionError:
        # Skip directories without permission
        pass

def search_drive(drive, search_name, results_queue, exact_matches):
    """Initiates the search on a specific drive."""
    search_files(drive, search_name, results_queue, exact_matches)

def real_time_search_gui(search_name, exact_match_var, subset_text):
    """Perform a real-time search for a file or folder with AI support and update GUI."""
    drives = [f"{chr(letter)}:\\" for letter in range(65, 91) if os.path.exists(f"{chr(letter)}:\\")]
    results_queue = queue.Queue()
    threads = []
    exact_matches = []  # To store exact matches

    # Start a thread for each drive
    for drive in drives:
        thread = threading.Thread(target=search_drive, args=(drive, search_name, results_queue, exact_matches))
        thread.start()
        threads.append(thread)

    def update_results():
        if exact_matches:
            exact_match_var.set("; ".join(exact_matches))
        try:
            while not results_queue.empty():
                result, score = results_queue.get_nowait()
                subset_text.insert(tk.END, f"{result} (Match Score: {score}%)\n")
                subset_text.see(tk.END)
        except queue.Empty:
            pass
        if any(thread.is_alive() for thread in threads):
            subset_text.after(100, update_results)

    update_results()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    if not exact_matches:
        messagebox.showinfo("Search Completed", "No exact matches found. Subset results are listed.")
    else:
        messagebox.showinfo("Search Completed", "Search completed. Exact matches and subsets are listed.")

def start_search(event=None):
    search_name = search_entry.get()
    if not search_name:
        messagebox.showwarning("Input Error", "Please enter a file or folder name.")
        return
    exact_match_var.set("Searching...")
    subset_text.delete(1.0, tk.END)
    threading.Thread(target=real_time_search_gui, args=(search_name, exact_match_var, subset_text)).start()

# Create GUI application
root = tk.Tk()
root.title("File and Folder Search")
root.geometry("600x400")

# Input field
tk.Label(root, text="Enter file or folder name:").pack(pady=5)
search_entry = tk.Entry(root, width=50)
search_entry.pack(pady=5)
search_entry.bind("<Return>", start_search)  # Bind Enter key to search

# Exact match result
tk.Label(root, text="Exact Matches:").pack(pady=5)
exact_match_var = tk.StringVar()
exact_match_entry = tk.Entry(root, textvariable=exact_match_var, width=50, state="readonly")
exact_match_entry.pack(pady=5)

# Copy button for exact match
def copy_exact_match():
    root.clipboard_clear()
    root.clipboard_append(exact_match_var.get())
    root.update()
    messagebox.showinfo("Copied", "Exact match address(es) copied to clipboard.")

tk.Button(root, text="Copy Exact Matches", command=copy_exact_match).pack(pady=5)

# Subset results
tk.Label(root, text="Subset Results:").pack(pady=5)
subset_text = scrolledtext.ScrolledText(root, width=70, height=15)
subset_text.pack(pady=5)

# Search button
tk.Button(root, text="Search", command=start_search).pack(pady=10)

# Run the application
root.mainloop()
