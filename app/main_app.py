import streamlit as st
from datetime import date, timedelta

from src.fetch_data import fetch_data
from src.process_data import response_to_dataframe
from src.visualize import plot_sessions_users
from src.visualize import plot_sessions_vs_users

st.title("GA4 Data Analytics Dashboard")

start_date = st.date_input("Start Date", date.today() - timedelta(days=7))
end_date = st.date_input("End Date", date.today() - timedelta(days=1))

if st.button("Fetch and Visualize Data"):
    response = fetch_data(str(start_date), str(end_date))
    df = response_to_dataframe(response)
    st.write(df)

    st.subheader("Summary")
    total_sessions = df["sessions"].sum()
    total_active_users = df["activeUsers"].sum()
    col1, col2 = st.columns(2)
    col1.metric("Total Sessions", f"{total_sessions:,}")
    col2.metric("Total Active Users", f"{total_active_users:,}")
    st.caption(f"Average Sessions per Day: {df['sessions'].mean():.1f}")

    plot_sessions_users(df)
    plot_sessions_vs_users(df)
