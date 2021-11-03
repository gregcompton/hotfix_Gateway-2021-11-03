import json
import os


def restart_service(service):
    if os.name == 'nt':
        print('restart_service(%s): You are running Windows. systemctl does not exist' % service)
        return
    try:
        cmd = 'systemctl restart ' + service + '.service'
        os.system(cmd)
    except Exception as e:
        print.warning('unable to restart service' + e)


def main():
    current_path = '/opt/hyper/base/current_versions.json'

    with open(current_path, 'r+') as current_file:
        current = json.load(current_file)

    print(current)

    current['thermocouple']['version'] = 1

    print(current)

    os.remove(current_path)

    with open(current_path, "a") as current_file:
        current_file.write(json.dumps(current))

    restart_service('hyperbase')

    print("\nThat's it. Thermocouple should not get stuck in an endless update loop now")


main()