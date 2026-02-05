

# Notes App – Production Deployment on AWS EC2

## System Architecture
<img 
src="C:\Users\abdel\OneDrive\Desktop\DevOps\Dev_Projects\Note-Taker\Note-Taker-W
ebsite-Application\systemArch\System_Arch.png" width="700">


## Project Overview

This project demonstrates a **production-ready deployment** of a simple note-taking web application using **Flask**, **MariaDB**, **Gunicorn**, and **Nginx**, hosted on an **AWS EC2 instance**.
The project also includes a **robust backup strategy** using **LVM** and **automated database backups** via **cron**.

The goal of this project is to showcase **DevOps fundamentals**, including Linux administration, service management, database handling, automation, and basic frontend enhancement.

---
## Tech Used

* **OS**: Ubuntu 24.04 (EC2)
* **Backend**: Python (Flask)
* **Database**: MariaDB
* **Web Server**: Nginx
* **WSGI Server**: Gunicorn
* **Automation**: systemd, cron
* **Backup Storage**: LVM mounted volume
* **Frontend**: HTML, CSS, Bootstrap, Animations

---

## Project Structure

```
Notes-app/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── css/
│       └── style.css (optional)
├── myenv/ in .gitignore
```

---

## Application Features

* Create and save notes
* Display notes with timestamps (latest first)
* Responsive UI with animations
* Dark mode toggle
* Production deployment (no development server exposed)

---

##  Deployment Steps Summary

### EC2 Setup

* Ubuntu 24.04 EC2 instance
* Security Group:

  * Port 22 (SSH)
  * Port 80 (HTTP)

---

### 2 - Database Setup (MariaDB)

```sql
CREATE DATABASE notes_db;
CREATE USER 'notes_user'@'localhost' IDENTIFIED BY '********';
GRANT ALL PRIVILEGES ON notes_db.* TO 'notes_user'@'localhost';
FLUSH PRIVILEGES; # refresht the privileges
```
---

### 3 - Flask Application

* Flask handles routing and database interaction
* Uses `flask-mysqldb` for MariaDB connectivity

---

### 4 - Gunicorn + systemd

Gunicorn is managed as a systemd service for reliability:

* Auto start on boot
* Auto restart on failure
* Runs under non-root Linux user

---

### 5 - Nginx Reverse Proxy

* Listens on port 80
* Proxies requests to Gunicorn
* Flask ports are not exposed publicly
---
## Backup Strategy

### Storage

* Dedicated **LVM logical volume**
* Mounted at `/Database_Backup`
* Persistent via `/etc/fstab`

### Backup Script

* Uses `mysqldump`
* Timestamped backup files
* Automatic cleanup (retention: 14 days)

```bash
/usr/local/bin/db_Backup.sh
```

### Automation (Cron)

Weekly automated backup (example):

```cron
0 8 * * 5 /usr/local/bin/db_backup.sh >> /var/log/db_backup.log 2>&1
```

---
## Validation

* Manual restore tested
* Cron execution verified via logs
* Backup files verified in `/Database_Backup`

---

## Security Considerations

* No application services run as root
* Database access via dedicated DB user
* Internal services bound to `127.0.0.1`
* External access limited to ports 22 and 80
---

## What This Project Demonstrates

* Linux system administration
* Web application deployment
* Service management with systemd
* Secure database handling
* Backup automation
* Real-world DevOps workflow
---
## Future Improvements
* HTTPS with Let's Encrypt
* S3 offsite backups
* Backup encryption
* CI/CD pipeline
* Monitoring and alerting
---

*This project is intended for learning and demonstration purposes and reflects real-world DevOps practices. for DEPI*
