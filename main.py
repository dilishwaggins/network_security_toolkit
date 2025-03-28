#!/usr/bin/env python3

from modules import port_scanner, bandwidth_monitor, traffic_analyzer, ssl_checker

def show_menu():
    print("\033[1;32m")  # Green Bold Text
    print(r"""
 ███╗   ██╗███████╗████████╗██████╗ ██╗    ██╗ ██████╗ ██╗   ██╗
 ████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║    ██║██╔═══██╗╚██╗ ██╔╝
 ██╔██╗ ██║█████╗     ██║   ██████╔╝██║ █╗ ██║██║   ██║ ╚████╔╝ 
 ██║╚██╗██║██╔══╝     ██║   ██╔═══╝ ██║███╗██║██║   ██║  ╚██╔╝  
 ██║ ╚████║███████╗   ██║   ██║     ╚███╔███╔╝╚██████╔╝   ██║   
 ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝      ╚══╝╚══╝  ╚═════╝    ╚═╝   
                                                                
   🌐 Network Security Toolkit - Modular & Lightweight
    """)
    print("\033[0m")  # Reset color
    print("1. Port Scanner")
    print("2. Bandwidth Monitor")
    print("3. Traffic Analyzer")
    print("4. SSL Certificate Checker")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            port_scanner.run()
        elif choice == "2":
            bandwidth_monitor.run()
        elif choice == "3":
            traffic_analyzer.run()
        elif choice == "4":
            ssl_checker.run()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

