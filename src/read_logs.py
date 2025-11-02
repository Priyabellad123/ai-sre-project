import pandas as pd

def read_log_file(path = "data/log_sample.txt"):
    """Read a log file and return its contents as a pandas DataFrame."""
    with open(path, 'r', encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]
    df = pd.DataFrame(lines, columns=['raw'])
    df['timestamp'] = pd.to_datetime(df['raw'].str.slice(0, 19), format='%Y-%m-%d %H:%M:%S', errors='coerce')
    df['log_level'] = df['raw'].str.slice(20).str.split(' ', n=1).str[0]
    df['message'] = df['raw'].str.slice(20).str.split(' ', n=1).str[1]
    return df


if __name__ == "__main__":
    df = read_log_file()
    print(df.head())
    print(f"Total log entries: {len(df)}")

