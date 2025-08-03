# main.py

def analyze_log(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    suspicious = []

    for line in lines:
        if "Failed password" in line or "authentication failure" in line:
            suspicious.append(line)

    print(f"[!] Found {len(suspicious)} suspicious log entries:\n")
    for entry in suspicious:
        print(entry.strip())

if __name__ == "__main__":
    log_file = "sample.log"
    analyze_log(log_file)
