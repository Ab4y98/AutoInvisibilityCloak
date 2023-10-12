from asyncio import sleep
import os
import subprocess
import random
import string

post_exp_tools = {"SeatBelt": "https://github.com/GhostPack/Seatbelt.git", 
                  "SharPersist": "https://github.com/mandiant/SharPersist.git", 
                  "SharpKatz": "https://github.com/b4rtik/SharpKatz.git",
                  "StandIn": "https://github.com/FuzzySecurity/StandIn.git", 
                  "Watson": "https://github.com/rasta-mouse/Watson.git", 
                  "SharpZeroLogon": "https://github.com/leitosama/SharpZeroLogon.git", 
                  "SharpUp": "https://github.com/GhostPack/SharpUp.git", 
                  "SharpView": "https://github.com/tevora-threat/SharpView.git", 
                  "SharpHound": "https://github.com/BloodHoundAD/SharpHound.git"}

def generate_goofy_name():
    prefixes = ["Zig", "Zog", "Bop", "Doodle", "Fizzle", "Goober", "Moo", "Quirk", "Squiggle", "Wobble"]
    suffixes = ["noodle", "muffin", "pickle", "whiz", "gobble", "snicker", "doodle", "blob", "flap", "flop"]

    goofy_name = random.choice(prefixes) + random.choice(suffixes)
    return goofy_name

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:  
        os.system('clear')

def download_tool(tool_name):
    tool_dir = os.path.join("obf_tools", tool_name)
    
    # Check if the tool exists in the specified directory
    if os.path.exists(tool_dir):
        print(f"{tool_name} already exists in the directory.")
        exit(0)
    else:
        # If the tool doesn't exist, clone the Git repository
        try:
            os.chdir("obf_tools")
            subprocess.run(["git", "clone", post_exp_tools[tool_name]])
            print(f"{tool_name} has been successfully downloaded from the Git repository.")
        except Exception as e:
            print(f"Error downloading {tool_name}: {e}")
    
    # Return the full path of the tool
    return os.path.abspath(tool_name)

def obfuscate(method, tool_dir):
    new_tool_name = generate_goofy_name()
    os.chdir("../")
    os.chdir("InvisibilityCloak")
    print(tool_dir)
    command = f"python InvisibilityCloak.py -d {tool_dir} -n {new_tool_name} -m {method}"
    print(f"Running command: {command}")
    subprocess.run(command, shell=True)



def main():
    clear_screen()
    ascii_art = """
     _         _       ___            _     _ _     _ _ _ _          ____ _             _    
    / \  _   _| |_ ___|_ _|_ ____   _(_)___(_) |__ (_) (_) |_ _   _ / ___| | ___   __ _| | __
   / _ \| | | | __/ _ \| || '_ \ \ / / / __| | '_ \| | | | __| | | | |   | |/ _ \ / _` | |/ /
  / ___ \ |_| | || (_) | || | | \ V /| \__ \ | |_) | | | | |_| |_| | |___| | (_) | (_| |   < 
 /_/   \_\__,_|\__\___/___|_| |_|\_/ |_|___/_|_.__/|_|_|_|\__|\__, |\____|_|\___/ \__,_|_|\_\\
                                                              |___/                                                                 
    """

    print(ascii_art)

    print("Here are some post-exploitation tools and their GitHub repositories:\n")
    for tool, repo in post_exp_tools.items():
        print(f"{tool}")

    tool_name = input("\nEnter the name of the tool you want to download: ")
    
    print("Choose a text transformation method:")
    print("1. Base64")
    print("2. ROT13")
    print("3. Reverse")
    choice = input("Enter the number of your choice (1/2/3): ")

    if choice == "1":
        method = "base64"
    elif choice == "2":
        method = "rot13" 
    elif choice == "3":
        method = "reverse"
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        exit(1)
        
    tool_dir = download_tool(tool_name)
    obfuscate(method, tool_dir)


if __name__ == "__main__":
    main()