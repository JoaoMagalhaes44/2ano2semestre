import subprocess

username = 'root'
password = 'Jonyguga29'
database = 'mydb'
backup_file = 'backup_20230606_111052.sql' # Nome do ficheiro

command = f"mysql -u {username} -p{password} {database} < {backup_file}"
try:
    subprocess.run(command, shell=True, check=True)
    print("Backup file loaded successfully.")
except subprocess.CalledProcessError as e:
    print(f"Failed to load backup file: {e}")
