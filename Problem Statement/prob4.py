"""
Web Server Configuration System
"""

# Server IP (tuple, immutable)
server_ip = (192, 168, 1, 100)

# Allowed IPs (list, mutable)
allowed_ips = ['192.168.1.101', '192.168.1.102']

while True:
    print("\n--- Web Server Configuration ---")
    print("1. Add allowed IP")
    print("2. Remove allowed IP")
    print("3. Display configuration")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        new_ip = input("Enter IP address to allow: ")
        allowed_ips.append(new_ip)
        print(f"Added {new_ip} to allowed IPs.")

    elif choice == '2':
        rem_ip = input("Enter IP address to remove: ")
        if rem_ip in allowed_ips:
            allowed_ips.remove(rem_ip)
            print(f"Removed {rem_ip} from allowed IPs.")
        else:
            print("IP address not found in allowed list.")

    elif choice == '3':
        print("\nCurrent Configuration:")
        print("Server IP:", '.'.join(map(str, server_ip)))
        print("Allowed IPs:", allowed_ips)

    elif choice == '4':
        print("Exiting configuration system.")
        break
    else:
        print("Invalid choice. Please try again.")

# Prevent updating server_ip by not providing any option to change it and using a tuple (immutable)
