from tkinter import Tk, filedialog

def main():
    root = Tk()
    root.withdraw() 

    path = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if path:
        print("Selected file:", path)
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            print("\n--- File contents (first 200 chars) ---")
            print(f.read(200))
    else:
        print("No file selected.")

if __name__ == "__main__":
    main()
