import streamlit as st

st.set_page_config(page_title="JON",page_icon=":hala:",layout="wide")


def display_menu():
    print("Menu:")
    print("1. BURGER  - 25")
    print("2. HALO-HALO  - 65")
    print("3. FRENCH FRIES - 50")
    print("4. Quit")

def option_1():
    print("You selected BURGER. Price: 25")
    
def option_2():
    print("You selected HALO-HALO. PriCE: 65")

def option_3():
    print("You selected Option RENCH FRIES: 50")

def main():
    total_price = 0.0

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            option_1()
            total_price += 25
        elif choice == '2':
            option_2()
            total_price += 65
        elif choice == '3':
            option_3()
            total_price += 50
        elif choice == '4':
            print(f"Exiting the program. Total Price: ${total_price:.2f}. Thank You!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

