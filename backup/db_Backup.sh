#!/bin/bash

DATE=$(/bin/date +"%Y-%m-%d_%H-%M")
BACKUP_DIR="/Database_Backup"
DB_NAME="notesdb"
DB_USER="notes_user"
DB_PASS='rra31CB$'

/bin/mkdir -p "$BACKUP_DIR"

# Backup
/usr/bin/mysqldump -u"$DB_USER" -p"$DB_PASS" "$DB_NAME" \
  > "$BACKUP_DIR/notes_backup_$DATE.sql"

# Delete backups older than 14 days
/usr/bin/find "$BACKUP_DIR" -type f -name "*.sql" -mtime +14 -delete

