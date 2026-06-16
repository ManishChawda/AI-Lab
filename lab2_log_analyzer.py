import json

log_file = "server.log"

errors = []
warnings = []
info = []

with open(log_file, "r") as file:
    for line in file:
        line = line.strip()

        if "ERROR" in line:
            errors.append(line)

        elif "WARNING" in line:
            warnings.append(line)

        elif "INFO" in line:
            info.append(line)

data = {
    "error_count": len(errors),
    "warning_count": len(warnings),
    "info_count": len(info),
    "errors": errors,
    "warnings": warnings
}

print(json.dumps(data, indent=4))
