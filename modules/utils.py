from tabulate import tabulate

def print_table(data, headers):
    if not data:
        print("No data found.")
        return
    print(tabulate(data, headers=headers, tablefmt="grid"))
