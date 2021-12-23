import paramiko

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    
    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('-- Output ___')
        for line in output:
            print(line.strip())

if __name__ == "__main__":
    import getpass
    user = input('Username: ')
    passwd = getpass.getpass('Password: ')

    ip = input('Enter server IP: ')
    port = int(input('Enter port: '))
    cmd = input('Enter command: ')
    ssh_command(ip, port, user, passwd, cmd)