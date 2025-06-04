import matplotlib.pyplot as plt

def plot_sessions_users(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["date"], df["sessions"], label="Sessions", marker="o")
    plt.plot(df["date"], df["activeUsers"], label="Active Users", marker="o")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.legend()
    plt.title("Sessions and Users over Time")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
