import os


if os.path.exists("env.py"):
    import env

# print("Hello KERRRYYYYYYYY")


# def gameLoop():
#     task = input("What would you like to do - ")
#     if task == os.environ.get("Super_Secret", "DebugMode"):
#         print("You win")

# gameLoop()

BASE_URL = os.environ.get("LIVE_WEBSITE", "https://lksdjf-e343-47ff-lkfsf-lksdjflk.ws-eu01.gitpod.io/")


DATA_BASE = os.environ.get("DATABASE_URL", "sqlite:///db.sqlite3")


print(BASE_URL+"login")


a href="sjldfjsdlf"