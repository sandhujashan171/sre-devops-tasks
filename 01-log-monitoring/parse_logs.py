#!/usr/bin/env python3
import re
from collections import Counter

LOG_FILE = "/var/log/syslog"

class LogMonitor:
    LEVEL_PATTERN = re.compile(
        r"\b(ERROR|FAILED|INFO|WARNING)\b",
        re.IGNORECASE
    )

    def __init__(self, log_file=LOG_FILE):
        self.log_file = log_file

    def _read_log_lines(self):
        try:
            with open(self.log_file, "r", encoding="utf-8", errors="ignore") as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"{self.log_file} not found.")
            return []
        except PermissionError:
            print(f"Permission denied when trying to read {self.log_file}.")
            return []

    def parse_logs(self):
        lines = self._read_log_lines()
        if not lines:
            return

        log_levels = Counter()

        for line in lines:
            match = self.LEVEL_PATTERN.search(line)
            if match:
                log_levels[match.group(1).upper()] += 1

        for level, count in sorted(log_levels.items()):
            print(f"{level}: {count}")

if __name__ == "__main__":
    LogMonitor().parse_logs()