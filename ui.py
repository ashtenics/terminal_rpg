def print_header(title):
    text = f" {title.upper()} "
    print("\n" + "=" * 50)
    print(f"{text:=^50}")
    print("=" * 50 + "\n")

def print_alert(message):
    print("\n" + "!" * 50)
    print(f" ALERT: {message} ")
    print("!" * 50 + "\n")

def get_user_choice(prompt_text="What will you do?"):
    print("━" * 40)
    choice = input(f" {prompt_text}\n ❯ ").strip().lower()
    print("━" * 40)
    return choice

def print_travel_message(destination):
    print(f"\n ➔ Entering: [ {destination.upper()} ]")
    print(" ──────────────────────────────────────────────────")
