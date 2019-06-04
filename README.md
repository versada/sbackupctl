# Simple Backup Controller 
[![Build Status](https://drone.versada.eu/api/badges/versada/sbackupctl/status.svg?branch=master)](https://drone.versada.eu/versada/sbackupctl)
[![Latest Version @ Cloudsmith](https://api-prd.cloudsmith.io/badges/version/versada/cradle/deb/versada-sbackupctl/latest/d=ubuntu%252Fbionic/?badge_token=gAAAAABc9j34ck4yF2C4H4JD3EfRQrTt8TFtBJ8efzgH4T8bxFHBN-MyjWTfWvx_A3l2hOhwkDXVWnL7JLA-2lYnt_sfvnYVYtIHix5uS9z5nZPG3IV4ZzY%3D&render=true)](https://cloudsmith.io/~versada/repos/cradle/packages/detail/deb/versada-sbackupctl/latest/d=ubuntu%252Fbionic/)

An opinionated way to make backups. Basically,- a python script which launches
executables in a predefined sequence and wraps some common backup management commands.

# Installation

For Ubuntu 16.04, 18.04 we provide packages. They can be installed via:
```
curl -1sLf \
    'https://dl.cloudsmith.io/public/versada/cradle/cfg/setup/bash.deb.sh' \
    | sudo bash
apt-get install versada-sbackupctl
```

# Configuration

The description below will be based on using the sample backup strategy. This includes:

1. Making a postgres backup via `pg_dump`
2. Backing up some directory via `borgbackup`
3. And pinging cron service [healthchecks.io](https://healthchecks.io)

Copy sample files:
```
cp -R /usr/share/sbackupctl/* /opt/sbackupctl
```

Change default env variables at `/opt/sbackupctl/env`:
```
BORG_BACKUP_DIRS - colon delimited paths to backup
BORG_PASSPHRASE - passhprase to use to encrypt the repository
BORG_REPO - borg archive repository
HEALTHCHECK_TOKEN - token used to ping healthcheck service
PGDATABASE - database to backup via pg_dump
```

Periodic backups are enabled via
[systemd.timers](`https://www.freedesktop.org/software/systemd/man/systemd.timer.html`)
for timer file at `/lib/systemd/system/sbackupctl.timer`:
```
systemctl enable sbackupctl.timer
systemctl start sbackupctl.timer
```

# Usage

To do a backup there are 2 ways:
```
envdir /opt/sbackupctl/env sbackupctl backup
systemd start sbackupctl.service
```

To list all backups
```
envdir /opt/sbackupctl/env sbackupctl list
```

To get one of the backups
```
# $ARCHIVE_ID comes from sbackupctl list command
cd /tmp && envdir /opt/sbackupctl/env sbackupctl get $ARCHIVE_ID
```
