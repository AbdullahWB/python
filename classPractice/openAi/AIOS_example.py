import openai
import subprocess


openai.api_key =("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")

def ask_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that converts plain English into safe and simple PowerShell commands. Only return the command."},
            {"role": "user", "content": f"Convert this to PowerShell: {prompt}"}
        ],
        temperature=0.3
    )
    command = response['choices'][0]['message']['content'].strip()
    return command

def run_powershell(command):
    try:
        result = subprocess.run(
            ["powershell", "-Command", command],
            capture_output=True,
            text=True
        )
        print(f"\nOutput:\n{result.stdout}")
        if result.stderr:
            print(f"\nError:\n{result.stderr}")
        return True
    except Exception as e:
        print(f"\nError running PowerShell command: {e}")
        return False

if __name__ == "__main__":
    print("AI Shell Assistant (Windows PowerShell Edition)")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_input = input("What do you want to do? → ")
        
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
            
        shell_cmd = ask_ai(user_input)
        print(f"\nPowerShell command:\n{shell_cmd}")
        
        while True:
            confirm = input("Run this command? (y/n/edit/exit): ").lower()
            
            if confirm == 'y':
                run_powershell(shell_cmd)
                break
            elif confirm == 'n':
                print("Command discarded.")
                break
            elif confirm == 'edit':
                shell_cmd = input("Edit the command: ")
                continue
            elif confirm == 'exit':
                print("Goodbye!")
                exit()
            else:
                print("Invalid option. Please choose y/n/edit/exit")
                continue
        
        while True:
            another_task = input("\nWould you like to perform another task? (y/n): ").lower()
            if another_task == 'y':
                print()
                break
            elif another_task == 'n':
                print("Goodbye!")
                exit()
            else:
                print("Please enter 'y' or 'n'")