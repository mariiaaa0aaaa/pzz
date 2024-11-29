import dns.message
import dns.query
import dns.name
import dns.rdatatype
from ftplib import FTP
import paramiko


# DNS Query
def perform_dns_query():
    try:
        queryname = dns.name.from_text("amazon.com")
        q = dns.message.make_query(queryname, dns.rdatatype.NS)
        print("Запит має вигляд:")
        print(q)
        print(" ")
        r = dns.query.udp(q, "8.8.8.8")
        print("Відповідь на запит:")
        print(r)
    except Exception as e:
        print(f"Помилка DNS-запиту: {e}")


# FTP Client
def perform_ftp():
    try:
        ftp = FTP('ftp.us.debian.org')
        ftp.login()
        print("FTP Login successful.")
        ftp.cwd('debian')
        print("Directory listing:")
        ftp.retrlines('LIST')

        # Download a file
        with open('README', 'wb') as fp:
            ftp.retrbinary('RETR README', fp.write)
            print("README file downloaded.")
        ftp.quit()
    except Exception as e:
        print(f"Помилка FTP-запиту: {e}")


# SSH Client
def perform_ssh():
    try:
        host = "192.168.56.101"
        username = "kali"
        password = "kali"

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)
        print(f"Підключення до SSH-сервера: {host}")

        stdin, stdout, stderr = ssh.exec_command("ls -l")
        print("Вивід команди:")
        print(stdout.read().decode())
        ssh.close()
    except Exception as e:
        print(f"Помилка SSH-запиту: {e}")


if __name__ == "__main__":
    print("Оберіть завдання для виводу: 1: DNS")
    print("                             2: FTP")
    print("                             3: SSH")

    choice = input("Введіть Ваш вибір (1, 2, або 3): ")
    if choice == "1":
        perform_dns_query()
    elif choice == "2":
        perform_ftp()
    elif choice == "3":
        perform_ssh()
    else:
        print("Неіснуючий вибір. Будь-ласка введіть 1, 2, або 3.")