import os

class Config:
    # Telegram API credentials (obtained from https://my.telegram.org/apps)
    API_ID = int(os.getenv("API_ID", "27394279"))  # Replace 1234567 with your API ID
    API_HASH = os.getenv("API_HASH", "90a9aa4c31afa3750da5fd686c410851")  # Replace with your API Hash

    # Bot token (obtained from @BotFather on Telegram)
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7721902522:AAHamnJnM9f1AjWPvhl4NpzLeoM_d5TW6Dw")  # Replace with your Bot Token

    # Session name for Pyrogram (can be any string, or leave as default)
    SESSION_NAME = os.getenv("SESSION_NAME", "Screenshot")  # Default in-memory session

    # Telegram channel ID for logging (e.g., -1001234567890)
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002288135729"))  # Replace with your channel ID

    # Database URL (e.g., for PostgreSQL or SQLite)
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://telegramguy21:tnkIwvbNkJ5U3fZ7@botsuse.bpgag.mongodb.net/?retryWrites=true&w=majority&appName=Botsuse")  # Replace with your DB URL

    # List of authorized user IDs (Telegram user IDs)
    AUTH_USERS = [int(i) for i in os.getenv("AUTH_USERS", "7465574522").split()]  # Replace with user IDs

    # Maximum concurrent processes per user
    MAX_PROCESSES_PER_USER = int(os.getenv("MAX_PROCESSES_PER_USER", "2"))  # Adjust as needed

    # Maximum duration for trimming media (in seconds)
    MAX_TRIM_DURATION = int(os.getenv("MAX_TRIM_DURATION", "600"))  # Adjust as needed

    # Telegram channel ID for tracking (or False if not used)
    TRACK_CHANNEL = os.getenv("TRACK_CHANNEL", "False")
    TRACK_CHANNEL = int(TRACK_CHANNEL) if TRACK_CHANNEL != "False" else False  # Handle False or channel ID

    # Delay for slow speed processes (in seconds)
    SLOW_SPEED_DELAY = int(os.getenv("SLOW_SPEED_DELAY", "5"))  # Adjust as needed

    # Host URL or IP (leave empty if not used)
    HOST = os.getenv("HOST", "")  # Replace with host if needed

    # Timeout for processes (in seconds)
    TIMEOUT = int(os.getenv("TIMEOUT", "1800"))  # 30 minutes; adjust as needed

    # Debug mode (True for debugging, False for production)
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"  # Set to True for debugging

    # Number of worker processes
    WORKER_COUNT = int(os.getenv("WORKER_COUNT", "20"))  # Adjust as needed

    # Custom header for IAM (leave empty if not used)
    IAM_HEADER = os.getenv("IAM_HEADER", "")  # Replace with header if needed

    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    ]
