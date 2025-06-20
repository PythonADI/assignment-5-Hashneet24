usernames = ["Leonardo", "Jason", "Marry", "Admin", "Tim", "Jasmine", "Jenny"]
for username in usernames:
    if username == "Admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")