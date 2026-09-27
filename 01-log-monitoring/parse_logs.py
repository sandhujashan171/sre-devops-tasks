#!/usr/bin/env python3
import re
from collections import Counter

LOG_FILE = "/var/log/syslog"


class LogMonitor:
    LEVEL_PATTERN = re.compile(
        r"\b(INFO|WARNING|WARN|FAILED|FAIL|ERROR|CRITICAL)\b",
        re.IGNORECASE,
    )

    def __init__(self, log_file=LOG_FILE):
        self.log_file = log_file

    def _read_log_lines(self):
        try:
            with open(self.log_file, "r", encoding="utf-8", errors="ignore") as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Log file {self.log_file} not found.")
            return None
        except PermissionError:
            print(f"Permission denied when trying to read {self.log_file}.")
            return None

    def parse_logs(self):
        lines = self._read_log_lines()
        if lines is None:
            return

        log_levels = Counter()
        recent_errors = []

        for line in lines:
            match = self.LEVEL_PATTERN.search(line)
            if not match:
                continue

            log_level = match.group(0).upper()
            if log_level == "WARN":
                log_level = "WARNING"

            log_levels[log_level] += 1
            if log_level in {"ERROR", "CRITICAL", "FAILED", "FAIL"}:
                recent_errors.append(line.strip())

        print("=" * 50)
        print("       SYSLOG MONITORING REPORT       ")
        print("=" * 50)
        print(f"Total lines scanned: {len(lines)}")
        print("-" * 50)
        print("[log levels breakdown]")

        if not log_levels:
            print("No log levels found.")
        else:
            for level, count in sorted(log_levels.items()):
                print(f"{level}: {count}")

        print("-" * 50)
        print("[recent critical events (last 5)]")
        if not recent_errors:
            print("No recent errors found.")
        else:
            for error in recent_errors[-5:]:
                print(f" - {error}")

        print("=" * 50)


if __name__ == "__main__":
    LogMonitor().parse_logs()           
