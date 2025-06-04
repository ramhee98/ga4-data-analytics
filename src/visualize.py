import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_sessions_users(df):
    # Group by date to avoid overlapping lines
    df_grouped = df.groupby("date", as_index=False)[["sessions", "activeUsers", "pageViews"]].sum()
    df_grouped = df_grouped.sort_values("date")

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_grouped["date"], df_grouped["sessions"], label="Sessions", marker="o")
    ax.plot(df_grouped["date"], df_grouped["activeUsers"], label="Active Users", marker="o")
    ax.plot(df_grouped["date"], df_grouped["pageViews"], label="Page Views", marker="o")
    ax.set_xlabel("Date")
    ax.set_ylabel("Count")
    ax.set_title("Sessions, Active Users, and Page Views Over Time")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def plot_sessions_vs_users(df):
    fig, ax = plt.subplots(figsize=(6, 6))
    sns.regplot(x="sessions", y="activeUsers", data=df, ax=ax)
    ax.set_xlabel("Sessions")
    ax.set_ylabel("Active Users")
    ax.set_title("Sessions vs Active Users")
    ax.grid(True)
    st.pyplot(fig)

def plot_sessions_vs_pageviews(df):
    fig, ax = plt.subplots(figsize=(6, 6))
    sns.regplot(x="sessions", y="pageViews", data=df, ax=ax)
    ax.set_xlabel("Sessions")
    ax.set_ylabel("Page Views")
    ax.set_title("Sessions vs Page Views")
    ax.grid(True)
    st.pyplot(fig)
