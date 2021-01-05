Fail2ban
=========

![Test Ansible Role](https://github.com/rbrightling/role-fail2ban/workflows/Test%20Ansible%20Role/badge.svg?branch=main) [![Ansible Galaxy](http://img.shields.io/badge/galaxy-rbrightling.fail2ban-660198.svg?style=flat)](https://galaxy.ansible.com/rbrightling/fail2ban)

Install and configure Fail2ban. Service to scan log files and ban ip addresses which show malicious signs.

**NOTE:** Distributions generally provide a custom jail configuration, which this role leaves in place and provides 
configuration overrides using the .local as recommended. 

Requirements
------------

Ansible 2.8+

Supported Distributions:
  - Debian Buster
  - RedHat 8

**NOTE**: By default sshd jail is enabled with the systemd backend.

Role Variables
--------------

```yaml
# defaults file for fail2ban
# Values set to null are ignored and loaded from default system configuration (if option is present).

# Configuration
# #############
#
# Set the log level output
fail2ban_log_level: INFO
# Values: CRITICAL, ERROR, WARNING, NOTICE, INFO, DEBUG.

# Set the target output for logging
fail2ban_log_target: "/var/log/fail2ban.log"
# Values: STDOUT, STDERR, SYSLOG, SYSOUT, `file path`

# Used with SYSLOG `fail2ban_log_target`
fail2ban_syslog_socket: auto
# Values: auto, `file_path`

# set socket file
fail2ban_socket: "/var/run/fail2ban/fail2ban.sock"

# set the pid file
fail2ban_pidfile: "/var/run/fail2ban/fail2ban.pid"

# set a persistant data store, or use memory only
fail2ban_db_file: "/var/lib/fail2ban/fail2ban.sqlite3"
# Values: NONE, :memory, `file_path`

# Age at which bans are purged from the database
fail2ban_db_purge_age: 7d

# Jail Configuration
# ##################

# Ignore local own ip address from rules.
fail2ban_ignore_self: true

# Ignore a given ip address, CIDR or DNS from matching rules.
fail2ban_ignore_ip: null #(string, list)

# External command to test ip to ignore 
fail2ban_ignore_command: null

# Time that a host is banned for
fail2ban_ban_time: 1h

# Host is banned if `max_retry` is breeched in `find_time`
fail2ban_find_time: 10m
fail2ban_max_retry: 5

# Backend used to check file modifications.
fail2ban_backend: null
# Values:
#   - pyinotify
#   - gamin
#   - polling
#   - systemd
#   - auto

# Specifies if jails sould trust hostnames in logs
fail2ban_use_dns: null
# values:
#   - yes: lookup hostname in DNS
#   - warn: lookup hostname in DNS but it will be logged as a warning
#   - no: hostname won't be used for banning, but will be logged.
#   - raw: uses raw value (no hostname)

# log file encoding
fail2ban_log_encoding: auto

# jails enabled or disabled
fail2ban_enabled: false

# mode of the filters
fail2ban_mode: null

# Jail Actions
# ############

# destination email address
fail2ban_destemail: "root@localhost"

# sender email address
fail2ban_sender: "root@{{ ansible_fqdn }}"

# email mta
fail2ban_mta: null

# Jails
# #####
#
# Override default jail settings and enabled individual predefied jails by the distribution.
# NOTE: Some jails only have a default configuration on specified distributions.

# SSH Servers
# Recommend adding ignoreip for management ip address
fail2ban_jail_sshd: "{{ fail2ban__jail_sshd }}"
# Debian/RedHat:
#   enabled: true
#   backend: "systemd"

fail2ban_jail_dropbear: null
fail2ban_jail_selinux_ssh: null

# HTTP Servers
fail2ban_jail_apache_auth: null
fail2ban_jail_apache_badbots: null
fail2ban_jail_apache_noscript: null
fail2ban_jail_apache_overflows: null
fail2ban_jail_apache_nohome: null
fail2ban_jail_apache_botsearch: null
fail2ban_jail_apache_fakegooglebot: null
fail2ban_jail_apache_modsecurity: null
fail2ban_jail_apache_shellshock: null
fail2ban_jail_openhab_auth: null
fail2ban_jail_nginx_http_auth: null
fail2ban_jail_nginx_limit_req: null
fail2ban_jail_nginx_botsearch: null
fail2ban_jail_php_url_fopen: null
fail2ban_jail_suhosin: null
fail2ban_jail_lighttpd_auth: null

# webmail and groupware
fail2ban_jail_roundcube_auth: null
fail2ban_jail_openwebmail: null
fail2ban_jail_horde: null
fail2ban_jail_groupoffice: null
fail2ban_jail_sogo_auth: null
fail2ban_jail_tine20: null

# Web Applications
fail2ban_jail_drupal_auth: null
fail2ban_jail_guacamole: null
fail2ban_jail_monit: null
fail2ban_jail_webmin_auth: null
fail2ban_jail_froxlor_auth: null

# HTTP Proxy Servers
fail2ban_jail_squid: null
fail2ban_jail_3proxy: null
fail2ban_jail_proftpd: null
fail2ban_jail_pure_ftpd: null
fail2ban_jail_gssftpd: null
fail2ban_jail_wuftpd: null
fail2ban_jail_vsftpd: null

# Mail Servers
fail2ban_jail_assp: null
fail2ban_jail_courier_smtp: null
fail2ban_jail_postfix: null
fail2ban_jail_postfix_rbl: null
fail2ban_jail_sendmail_auth: null
fail2ban_jail_sendmail_reject: null
fail2ban_jail_qmail_rbl: null
fail2ban_jail_dovecot: null
fail2ban_jail_sieve: null
fail2ban_jail_solid_pop3d: null
fail2ban_jail_exim: null
fail2ban_jail_exim_spam: null
fail2ban_jail_kerio: null
fail2ban_jail_courier_auth: null
fail2ban_jail_postfix_sasl: null
fail2ban_jail_perdition: null
fail2ban_jail_squirrelmail: null
fail2ban_jail_cyrus_imap: null
fail2ban_jail_uwimap_auth: null

# DNS Servers
fail2ban_jail_named_refused: null
fail2ban_jail_nsd: null

# Miscellaneous
fail2ban_jail_asterisk: null
fail2ban_jail_freeswitch: null
fail2ban_jail_znc_adminlog: null # (Redhat)
fail2ban_jail_mysqld_auth: null
fail2ban_jail_mongodb_auth: null
fail2ban_jail_recidive: null
fail2ban_jail_pam_generic: null
fail2ban_jail_xinetd_fail: null
fail2ban_jail_stunnel: null
fail2ban_jail_ejabberd_auth: null
fail2ban_jail_counter_strike: null
fail2ban_jail_softethervpn: null # (RedHat)
fail2ban_jail_gitlab: null # (Redhat)
fail2ban_jail_grafana: null # (RedHat)
fail2ban_jail_bitwarden: null # (RedHat)
fail2ban_jail_centreon: null # (RedHat)
fail2ban_jail_nagios: null
fail2ban_jail_oracleims: null
fail2ban_jail_directadmin: null
fail2ban_jail_portsentry: null
fail2ban_jail_pass2allow_ftp: null
fail2ban_jail_murmur: null
fail2ban_jail_screensharingd: null
fail2ban_jail_haproxy_http_auth: null
fail2ban_jail_slapd: null
fail2ban_jail_domino_smtp: null
fail2ban_jail_phpmyadmin_syslog: null
fail2ban_jail_zoneminder: null
fail2ban_jail_traefik_auth: null # (RedHat)
```

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: "include fail2ban role"
      include_role:
        name: fail2ban
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
