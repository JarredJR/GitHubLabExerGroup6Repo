import pandas as pd
from hoopstatsview import HoopStatsView

def cleanStats(df):
    print("[INFO] Cleaning FG, 3PT, FT columns...")
    for col in ["FG", "3PT", "FT"]:
        made_col = col + "M"
        att_col = col + "A"

        if col in df.columns:
            df[[made_col, att_col]] = df[col].str.split("-", expand=True).astype(int)
            df.drop(columns=[col], inplace=True)
        else:
            print(f"[WARNING] Column {col} not found in the CSV.")

    print("[INFO] Cleaning done.")
    return df

def main():
    print("[INFO] Loading CSV data...")
    try:
        frame = pd.read_csv("cleanbrogdonstats.csv")
        print("[INFO] File loaded successfully.")
    except FileNotFoundError:
        print("[ERROR] cleanbrogdonstats.csv not found. Make sure it's in the same folder.")
        return

    print("[INFO] Starting data cleaning...")
    cleaned_frame = cleanStats(frame)

    print("[INFO] Launching GUI...")
    HoopStatsView(cleaned_frame).mainloop()

if __name__ == "__main__":
    main()
