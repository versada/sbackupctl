# Context

There is quite a need for easy to use odoo backing up package. The idea is for
the backup strategy to be easily extendable since different projects use
different strategies for backups. For example,- rclone for cloud offsite
backups, borgbackup for both onsite and offsite backups, gsutil cp for offsite
backups.

In addition, there are sometimes things which needs to be done before the
backup step takes place. For example to pg\_dump a database to a directory.
This should be done only once so it would be nice to have a simple framework
(dir structure) to extend the default strategy.

# Installation

# Usage
