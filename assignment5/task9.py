users = []
for user in users:
    if user == "Admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
if users == []:
    print("We need to find more users!")
