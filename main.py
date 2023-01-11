import socket

def get_ip_by_hostname(hostname:str)->str:
    try:
        ip = socket.gethostbyname(hostname)
        return f'Hostname: {hostname}\nIP address: {ip}'
    except socket.gaierror as error:
        return f'Invalid Hostname - {error}'


def main():
    hostname = input('Please enter a website address(URL): ')
    print(get_ip_by_hostname(hostname))

if __name__ == '__main__':
    main()
