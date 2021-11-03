import json
import os


def restart_service(service):
    if os.name == 'nt':
        print('restart_service(%s): You are running Windows. systemctl does not exist' % service)
        return
    try:
        cmd = 'systemctl restart ' + service + '.service'
        os.system(cmd)
        print(service, ' service was restarted.')
    except Exception as e:
        print.warning('unable to restart service' + e)


def main():
    current_versions_path = '/opt/hyper/base/current_versions.json'
    firmware_config_path = '/opt/hyper/base/firmware_config.json'

    print('\n********************************************\n')

    print("Fixing curent_versions.json...")
    with open(current_versions_path, 'r+') as current_file:
        current = json.load(current_file)
    print('Before fix: ', current)
    current['thermocouple']['version'] = 1
    print()
    print('After fix: ', current)
    os.remove(current_versions_path)
    with open(current_versions_path, "a") as current_file:
        current_file.write(json.dumps(current))

    print('\n********************************************\n')

    print("Fixing firmware_config.json...")
    with open(firmware_config_path, 'r+') as current_file:
        current = json.load(current_file)
    print('Before fix: ', current)
    print()
    current['THERMOCOUPLE']['version'] = 1
    print('After fix: ', current)
    os.remove(firmware_config_path)
    with open(firmware_config_path, "a") as current_file:
        current_file.write(json.dumps(current))

    print('\n********************************************\n')

    print('Confirming file contents...')
    with open(current_versions_path, 'r+') as current_file:
        current = json.load(current_file)
        print("\ncurrent_versions.json contents: ")
        for device in current:
            print('\t', device, current[device])
    with open(firmware_config_path, 'r+') as current_file:
        current = json.load(current_file)
        print("\nfirmware_config.json contents: ")
        for device in current:
            print('\t', device, current[device])


    print('\n********************************************\n')
    restart_service('hyperbase')

    print("\nThat's it. Thermocouple should not get stuck in an endless update loop now")


main()