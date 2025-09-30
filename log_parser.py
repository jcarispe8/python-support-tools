# log_parser.py
# Extracts error lines from a log file and prints them

def extract_errors(log_path):
    with open(log_path, 'r') as file:
        for line in file:
            if "ERROR" in line:
                print(line.strip())

# Example usage
# extract_errors('system_logs.txt')
