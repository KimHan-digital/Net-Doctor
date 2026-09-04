import sys
import socket
import subprocess
import datetime
import os
import platform
import netifaces

def log_write(message):
    if not os.path.exists("logs"):
        os.makedirs("logs")


    now = datetime.datetime.now()
    time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")

    log_line = f"[{time_stamp}] {message}"
    print(log_line)

    today = now.strftime("%Y-%m-%d")
    file_name = f"logs/{today}.log"

    with open(file_name, "a", encoding="utf-8") as file:
        file.write(log_line + "\n")

def get_network_information():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    gateway_ip = "Not Found"
    subnet_mask = "Not Found"

    try:
        gateway_dict = netifaces.gateways()
        if 'default' in gateway_dict and netifaces.AF_INET in gateway_dict['default']:
            gateway_ip = gateway_dict['default'][netifaces.AF_INET][0]
            interface_name = gateway_dict['default'][netifaces.AF_INET][1]


            addrs = netifaces.ifaddresses(interface_name)
            if netifaces.AF_INET in addrs:
                for addr in addrs[netifaces.AF_INET]:
                    if 'netmask' in addr:
                        subnet_mask = addr['netmask']
                        break
    except Exception as e:
        pass

    return{
        "hostname": hostname,
        "local_ip": local_ip,
        "gateway": gateway_ip,
        "subnet": subnet_mask
    }

def ping_me(target):
    operating_system = platform.system()

    if operating_system == "Windows":
        command = ["ping", "-n", "1", target]
    else:
        command = ["ping", "-c", "1", target]

    try:
        answer = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=2
        )
    
        return answer.returncode == 0
    
    except subprocess.TimeoutExpired:

        return False

def main():

    print("--- NETWORK INFORMATION AND PİNG TEST STARTING ---")

    information = get_network_information()

    log_write(f"Device Name (Hostname)  : {information['hostname']}")
    log_write(f"Local IP (Local IP)        : {information['local_ip']}")
    log_write(f"Gateway (Gateway)        : {information['gateway']}")
    log_write(f"Subnet (Subnet)    : {information['subnet']}")

    
    log_write("Checking internet connection (8.8.8.8)...")
    internet_status = ping_me("8.8.8.8")
    if internet_status:
        log_write("✅ Internet connection AVAİLABLE.")
    else:
        log_write("❌ There is NO internet connection, or it is very slow!")

    if information['gateway'] != "Not Found":
        log_write(f"Pinging the gateway ({information['gateway']})...")
        gateway_status = ping_me(information['gateway'])
        if gateway_status:
            log_write("✅ The gateway is accessible.")
        else:
            log_write("❌ Gateway unreachable! Connection to the modem/router is lost")

    print("--- TEST COMPLETED ---")


if __name__ == "__main__":
    main()