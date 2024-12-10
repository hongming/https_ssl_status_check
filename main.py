import ssl
import socket
from datetime import datetime
import os

def check_https_status(domain):
    try:
        # Remove "http://" or "https://" from domain if present
        domain = domain.replace("http://", "").replace("https://", "").strip()
        # Connect to the domain on port 443 to retrieve SSL information
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                # Get expiration date from certificate
                expiry_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y GMT')
                return True, expiry_date
    except Exception as e:
        # Return False and the error for debugging purposes
        return False, str(e)

def main():
    input_file = 'domains.txt'
    output_file = f'domains_check_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'

    # Ensure the input file exists
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return
    
    print("Checking")
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            domain = line.strip()
            if not domain:
                continue
            https_status, detail = check_https_status(domain)
            if https_status:
                result = f"{domain}: HTTPS is working, certificate expires on {detail}"
            else:
                result = f"{domain}: HTTPS check failed, error: {detail}"
            print(f"{domain} domains https status checked, next...")
            outfile.write(result + '\n')
    
    print(f"Check completed. Results saved in {output_file}.")

if __name__ == "__main__":
    main()
