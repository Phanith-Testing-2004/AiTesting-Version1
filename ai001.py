import os
import platform

MEMORY_FILE = "ai_memory.txt"

def load_memory():
    memory = {}
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as file:
                for line in file:
                    if ":" in line:
                        key, value = line.strip().split(":", 1)
                        memory[key.strip().lower()] = value.strip()
        except Exception as e:
            print(f"⚠️ Error loading memory: {e}")
    return memory

def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        for key, value in memory.items():
            file.write(f"{key}: {value}\n")

def learn(memory):
    user_input = input("✍️ Enter fact (e.g., 'capital of France: Paris'): ")
    if ":" in user_input:
        key, value = user_input.split(":", 1)
        key = key.strip().lower()
        value = value.strip()
        memory[key] = value
        print(f"✅ Learned: '{key}' is '{value}'")
        save_memory(memory)
    else:
        print("❌ Format error. Use: 'key: value'")

def ask(memory):
    question = input("❓ What do you want to ask: ").strip().lower()
    if question in memory:
        print(f"🤖 {question.capitalize()} is {memory[question]}")
    else:
        print("🤷 I don't know that yet. You can teach me!")

def do_action():
    command = input("🛠️ What should I do? ").strip().lower()
    system = platform.system()

    if "note" in command:
        if system == "Darwin":  
            os.system("open -a TextEdit")
        elif system == "Windows":
            os.system("notepad")
        elif system == "Linux":
            editors = ["gedit", "nano", "vim", "kate", "xed"]
            for editor in editors:
                if os.system(f"which {editor} > /dev/null 2>&1") == 0:
                    os.system(f"{editor} &")
                    break
            else:
                print("⚠️ No supported text editor found.")
        else:
            print("⚠️ Unsupported operating system.")

    elif "code" in command:
        if system == "Darwin":
            os.system("open -a 'Visual Studio Code'")
        elif system == "Windows":
            os.system("code")
        elif system == "Linux":
            editors = ["code", "code-insiders", "codium"]
            for editor in editors:
                if os.system(f"which {editor} > /dev/null 2>&1") == 0:
                    os.system(f"{editor} &")
                    break
            else:
                print("⚠️ VS Code is not installed or not in PATH.")
        else:
            print("⚠️ Unsupported operating system.")

    elif "tor" in command:
        if system == "Darwin":
           
            os.system("open -a 'Tor Browser'")
        elif system == "Windows":
            
            tor_path = r"C:\Program Files\Tor Browser\Browser\firefox.exe"
            if os.path.exists(tor_path):
                os.startfile(tor_path)
            else:
                print("rk ot see te bro!")
        elif system == "Linux":
            
            if os.system("which tor-browser > /dev/null 2>&1") == 0:
                os.system("tor-browser &")
            else:
                print("rk ot see te bro!")
        else:
            print("eror hx bro!")

    elif "chrome" in command:
        if system == "Darwin":
            os.system("open -a 'Google Chrome'")
        elif system == "Windows":
           
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            if os.path.exists(chrome_path):
                os.startfile(chrome_path)
            else:
                print("rk ot see te bro!.")
        elif system == "Linux":
           
            browsers = ["google-chrome", "chrome", "chromium-browser"]
            for browser in browsers:
                if os.system(f"which {browser} > /dev/null 2>&1") == 0:
                    os.system(f"{browser} &")
                    break
            else:
                print("⚠️ Google Chrome not found or not in PATH.")
        else:
            print("⚠️ Unsupported operating system.")

    elif "say hello" in command:
        print("👋 Hello! I'm your AI assistant.")

    else:
        print("⚙️ I don't know how to do that yet.")

def show_menu():
    print("\n========== AI MENU ==========")
    print("1. Teach me something new")
    print("2. Ask me a question")
    print("3. Tell me to do something")
    print("4. Exit")
    print("=============================")

def main():
    memory = load_memory()
    print("🤖 Simple AI Assistant Started!")

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            learn(memory)
        elif choice == "2":
            ask(memory)
        elif choice == "3":
            do_action()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
