#!/bin/bash
ARCHIVE_DIR="$HOME/sre-devops-tasks/01-log-monitoring/archive"
REPORT_FILE="$HOME/sre-devops-tasks/01-log-monitoring/cron_report.txt"

DATE=$(date +"%Y-%m-%d_%H-%M")
BACKUP_NAME="report_backup_$DATE.tar.gz"

if [ -f "$REPORT_FILE" ]; then
    tar -czf "$ARCHIVE_DIR/$BACKUP_NAME" "$REPORT_FILE"
    echo "Success: Archived report to $BACKUP_NAME"
else
    echo "Error: $REPORT_FILE not found. Nothing to archive."
fi
