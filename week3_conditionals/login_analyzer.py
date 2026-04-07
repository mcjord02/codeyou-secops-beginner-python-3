while True:
    name = input("\nEnter name (or type 'exit' to quit): ")
    if name.lower() == 'exit':
        print("Exiting the Login Analyzer.")
        break
    username = input("Enter username: ")
    failed_logins = int(input("Enter number of failed login attempts: "))
    critical_user = input("Is this a privileged user? (yes/no): ")


    print("\n====================================")
    print("Cyber Defense - Login Attempt Report")
    print("======================================")
    print('\n')    
    print(f"Name: {name}")
    print(f"Username: {username}")
    print(f"Failed Attempts: {failed_logins}")
    print(f"Privileged Account: {critical_user}")

    if failed_logins > 5 and critical_user.lower() == "yes":
        print(f"Risk Level: HIGH")
    if failed_logins > 5 and critical_user.lower() == "no":
        print(f"Risk Level: MEDIUM")
    if failed_logins > 0 and failed_logins < 6:
        print(f"Risk Level: LOW")
    if failed_logins > 5 and critical_user.lower() == "yes":
        print("Alert: [*] Privileged account shows multiple failed logins!")
    elif failed_logins > 5:
        print("[!] ALERT: Multiple failed logins detected.")
    elif failed_logins > 0:
        print("Alert: [+] Some failed attempts observed.")
    else:
        print("[+] No failed logins recorded.")


    from datetime import datetime
    report_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    print("Report Generated:", report_date)

    cont = input("\nProcess another user? (y/n):   ")
    if cont.lower() != 'y':
        print("Exiting the Login Analyzer.")
        break