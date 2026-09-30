#!/bin/bash

# Define the exact file paths
ARCHIVE_DIR="$HOME/sre-devops-tasks/01-log-monitoring/archive"
REPORT_FILE="$HOME/sre-devops-tasks/01-log-monitoring/cron_report.txt"

# Create a timestamp (Year-Month-Day_Hour-Minute)
DATE=$(date +"%Y-%m-%d_%H-%M")
BACKUP_NAME="report_backup_$DATE.tar.gz"

# Check if the report exists, then compress it
if [ -f "$REPORT_FILE" ]; then
    tar -czf "$ARCHIVE_DIR/$BACKUP_NAME" "$REPORT_FILE"
    echo "Success: Archived report to $BACKUP_NAME"
else
    echo "Error: $REPORT_FILE not found. Nothing to archive."
fi
