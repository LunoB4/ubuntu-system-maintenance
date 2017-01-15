import os


def sys_update(system_functions):
    """ update system"""
    print('[!]updating system..\n')
    os.system(system_functions['update'])


def sys_autoremove(system_functions):
    """ autoremove packages"""
    print('\n[!]autoremoving packages...\n')
    os.system(system_functions['autoremove'])


def sys_clean(system_functions):
    """ clear apt cache"""
    print('\n[!]cleaning out apt cache...\n')
    os.system(system_functions['clean'])


def sys_log(system_functions):
    """ remove old .gz logs"""
    log = False
    logs = os.listdir('/var/log')

    for l in logs:
        if l.endswith('.gz'):
            log = True
    if log:
        o = input('[*]delete old log files y/n :')
        if o == 'y':
            print('\n[!]removing log backups...\n')
            os.system(system_functions['log'])
        else:
            print('\n[!]skipping logs...\n')
    else:
        print('\n[!]no log backups to remove...\n')


def main():
    system_functions = {
        'update': 'sudo apt update && sudo apt dist-upgrade',
        'autoremove': 'sudo apt autoremove',
        'clean': 'sudo apt autoclean && sudo apt clean',
        'log': 'sudo rm -r /var/log/*.gz'
        }

    sys_update(system_functions)
    sys_autoremove(system_functions)
    sys_clean(system_functions)
    sys_log(system_functions)


if __name__ == '__main__':
    main()
