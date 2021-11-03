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

    print("Fixing curent_versions.json...")
    with open(current_versions_path, 'r+') as current_file:
        current = json.load(current_file)
    print(current)
    current['thermocouple']['version'] = 1
    print(current)
    os.remove(current_versions_path)
    with open(current_versions_path, "a") as current_file:
        current_file.write(json.dumps(current))

    print("\nFixing firmware_config.json...")
    with open(firmware_config_path, 'r+') as current_file:
        current = json.load(current_file)
    print(current)
    print(current['THERMOCOUPLE']['version'])
    current['THERMOCOUPLE']['version'] = 1
    print(current)
    os.remove(firmware_config_path)
    with open(firmware_config_path, "a") as current_file:
        current_file.write(json.dumps(current))

    print('\nConfirming file contents...')
    with open(firmware_config_path, 'r+') as current_file:
        current = json.load(current_file)




    restart_service('hyperbase')

    print("\nThat's it. Thermocouple should not get stuck in an endless update loop now")


main()