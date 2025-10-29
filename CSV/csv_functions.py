import csv

# Function to read CSV data into a list
def read_csv_file(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


# Function to show first n rows
def head(data, n=5):
    return data[:n]


# Function to show last n rows
def tail(data, n=5):
    return data[-n:]


# Function to show number of rows and columns
def info(data):
    rows = len(data)
    cols = len(data[0]) if rows > 0 else 0
    print(f"Total Rows: {rows}")
    print(f"Total Columns: {cols}")


# Example usage
filename = "students.csv"
data = read_csv_file(filename)

print("=== HEAD ===")
for row in head(data):
    print(row)

print("\n=== TAIL ===")
for row in tail(data):
    print(row)

print("\n=== INFO ===")
info(data)
