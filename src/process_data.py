import pandas as pd

def response_to_dataframe(response):
    data = {"date": [], "sessions": [], "activeUsers": [], "pageViews": []}
    for row in response.rows:
        data["date"].append(row.dimension_values[0].value)
        data["sessions"].append(int(row.metric_values[0].value))
        data["activeUsers"].append(int(row.metric_values[1].value))
        data["pageViews"].append(int(row.metric_values[2].value))
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    return df
