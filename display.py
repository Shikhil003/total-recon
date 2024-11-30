import requests
import tkinter as tk
import pyfiglet
import webbrowser
from googlesearch import search
import jwt
from termcolor import colored
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

# Function to display the ASCII art for "Total Recon"
def show_banner():
    figlet = pyfiglet.figlet_format("Total Recon", font="slant")
    print(figlet)
    print("Twitter - @shikhilpau                                                                   @VIEH GROUP\n")
    print("WELCOME TO TOTAL RECON")

# Function to check HTTP status code
def check_http_status():
    url = simpledialog.askstring("HTTP Status Checker", "Enter the URL:")
    try:
        response = requests.get("http://" + url)
        messagebox.showinfo("HTTP Status Code", f"URL: {url}\nHTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function for subdomain bruteforcing
# Function for subdomain bruteforcing
def bruteforce_subdomains():
    path2 = simpledialog.askstring("Subdomain Bruteforcer", "Enter your domain:")
    open2=open(r"C:\Users\Dell\Desktop\project\TOTAL RECON\2m-subdomains.txt").read().splitlines()
    results = []
    for line1 in open2:
        newurl = line1 + "." + path2
        try:
            response1 = requests.get("http://" + newurl, timeout=5)
            print(f"Trying {newurl} - Status: {response1.status_code}")
            if response1.status_code in [200, 403, 302]:
                results.append((response1.status_code, newurl))
        except requests.exceptions.ConnectionError:
            print(f"Connection error with {newurl}")
            continue
    if results:
        result_message = "\n".join(f"{status} - {url}" for status, url in results)
        messagebox.showinfo("Results", f"Here are your results:\n{result_message}")
    else:
        messagebox.showinfo("Results", "No subdomains found.")

# Function for directory bruteforcing
def bruteforce_directories():
    path3 = simpledialog.askstring("Directory Bruteforcer", "Enter your domain:")
    open3 = open(r"C:\Users\Dell\Desktop\project\TOTAL RECON\dirbig.txt").read().splitlines()
    results = []
    for line2 in open3:
        newurl1 = "http://" + path3 + "/" + line2
        try:
            response2 = requests.get(newurl1, timeout=5)
            print(f"Trying {newurl1} - Status: {response2.status_code}")
            if response2.status_code in [200, 403, 302]:
                results.append((response2.status_code, newurl1))
        except requests.exceptions.ConnectionError:
            print(f"Connection error with {newurl1}")
            continue
    if results:
        result_message = "\n".join(f"{status} - {url}" for status, url in results)
        messagebox.showinfo("Results", f"Here are your results:\n{result_message}")
    else:
        messagebox.showinfo("Results", "No directories found.")

# Function for Google dorking
def automated_google_dorking():
    path4 = simpledialog.askstring("Google Dorker", "Enter the Target Domain:")
    open4 = open(r"TOTAL RECON\gdorks.txt").read().splitlines()
    for line3 in open4:
        newurl2 = f"site:{path4} {line3}"
        webbrowser.open("https://google.com/search?q=" + newurl2)

def bruteforce_jwt():
    file2 = "TOTAL RECON/secrets.txt"  # Directly specify the path to secrets.txt
    try:
        with open(file2) as secrets:
            token1 = simpledialog.askstring("JWT Bruteforcer", "Enter your token:")
            algo = simpledialog.askstring("JWT Bruteforcer", "Enter algorithm:")
            
            for secret in secrets:
                try:
                    payload = jwt.decode(token1, secret.rstrip(), algorithms=[algo])
                    messagebox.showinfo("Success", f"Token decoded successfully with secret: {secret.rstrip()}")
                    break  # Stop if the token is successfully decoded
                except jwt.InvalidTokenError:
                    print(colored(f"Invalid Token: {secret.rstrip()}", 'red'))
                except jwt.ExpiredSignatureError:
                    print(colored(f"Token Expired: {secret.rstrip()}", 'red'))
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{file2}' not found. Please make sure it is in the specified directory.")

# Setting up the Tkinter window
app = tk.Tk()
app.title("Total Recon")
app.geometry("400x400")

# Load and display the background image
try:
    # Use raw string to prevent invalid escape sequences and replace ANTIALIAS with LANCZOS
    bg_image = Image.open(r"c:\Users\Dell\Desktop\project\TOTAL RECON\com.jpg")
    bg_image = bg_image.resize((400, 400), Image.LANCZOS)  # Resize the image to fit the window
    bg_img = ImageTk.PhotoImage(bg_image)

    # Create a label for the background image and place it to fill the entire window
    bg_label = tk.Label(app, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Set to fill the window

    # Overlay widgets on top of the background image
    label = tk.Label(app, text="Select an option to use:", font=("Helvetica", 12), bg="white", fg="black")
    label.place(relx=0.5, rely=0.1, anchor="center")  # Center the label at the top

    # Creating buttons for each option with a slightly transparent white background
    button1 = tk.Button(app, text="1. Check HTTP Status Code", command=check_http_status, bg="#ffffff", relief="raised")
    button2 = tk.Button(app, text="2. Bruteforce Subdomains", command=bruteforce_subdomains, bg="#ffffff", relief="raised")
    button3 = tk.Button(app, text="3. Bruteforce Hidden Directories", command=bruteforce_directories, bg="#ffffff", relief="raised")
    button4 = tk.Button(app, text="4. Perform Automated Google Dorking", command=automated_google_dorking, bg="#ffffff", relief="raised")
    button5 = tk.Button(app, text="5. Bruteforce JWT Signature", command=bruteforce_jwt, bg="#ffffff", relief="raised")

    # Place buttons vertically centered on the window
    button1.place(relx=0.5, rely=0.3, anchor="center")
    button2.place(relx=0.5, rely=0.4, anchor="center")
    button3.place(relx=0.5, rely=0.5, anchor="center")
    button4.place(relx=0.5, rely=0.6, anchor="center")
    button5.place(relx=0.5, rely=0.7, anchor="center")

except Exception as e:
    print(f"Image load error: {e}")

# Run the application
app.mainloop()

