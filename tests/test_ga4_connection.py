# tests/test_ga4_connection.py

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Metric, Dimension
from google.oauth2 import service_account
import sys
import os

# Add project root to PYTHONPATH so we can import from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import config

def test_connection():
    credentials = service_account.Credentials.from_service_account_file(config.CREDENTIALS_PATH)
    client = BetaAnalyticsDataClient(credentials=credentials)

    request = RunReportRequest(
        property=f"properties/{config.GA4_PROPERTY_ID}",
        dimensions=[Dimension(name="date")],
        metrics=[Metric(name="sessions")],
        date_ranges=[DateRange(start_date="7daysAgo", end_date="yesterday")]
    )

    response = client.run_report(request)
    assert len(response.rows) > 0, "No rows returned from GA4 API"
    print("✅ GA4 API connection successful")
    for row in response.rows:
        print(f"{row.dimension_values[0].value}: {row.metric_values[0].value}")

if __name__ == "__main__":
    test_connection()
