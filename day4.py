# Simple Log Analyzer

logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

# Counters
error_count = 0
info_count = 0
warning_count = 0

# Process logs
for log in logs:
    log = log.upper()   # Ignore case sensitivity

    if "ERROR" in log:
        error_count += 1
    elif "INFO" in log:
        info_count += 1
    elif "WARNING" in log:
        warning_count += 1

# Print counts
print("ERROR Count:", error_count)
print("INFO Count:", info_count)
print("WARNING Count:", warning_count)

# Find most frequent log type
counts = {
    "ERROR": error_count,
    "INFO": info_count,
    "WARNING": warning_count
}

most_frequent = max(counts, key=counts.get)

print("Most Frequent Log Type:", most_frequent)