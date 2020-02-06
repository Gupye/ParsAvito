import subprocess


def get_lic():
    current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'))
    f = open('carlos.txt', 'w')
    lic = int(input())
    UUID = current_machine_id[46:82]
    f.write(UUID)  # запись в файл идентификатора компьютера
    f.write(lic)  # запись в файл лицензии
    f.close()
    set_file = open('test23.txt')  # открытие локального лицензионного файла
    lic_file = open('test231.txt')  # открытие файла с лицензиями с сервера
    loc_lic = set_file.read()
    all_lic = lic_file.read()
    if loc_lic in all_lic:
        print('hello')
    else:
        print('Украли')