import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_fail2ban_installed(host):
    fail2ban_package_name = "fail2ban"
    assert host.package(fail2ban_package_name).is_installed


def test_fail2ban_service(host):
    fail2ban_service_name = "fail2ban"
    service = host.service(fail2ban_service_name)
    assert service.is_running
    assert service.is_enabled


def test_fail2ban_jail_status(host):
    cmd_status = host.run("/usr/bin/fail2ban-client status")
    assert re.search("Jail list:.*sshd", cmd_status.stdout)
