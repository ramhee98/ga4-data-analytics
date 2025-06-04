from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Metric, Dimension
from google.oauth2 import service_account

from src import config

def get_client():
    credentials = service_account.Credentials.from_service_account_file(config.CREDENTIALS_PATH)
    return BetaAnalyticsDataClient(credentials=credentials)

def fetch_data(start_date, end_date):
    client = get_client()
    request = RunReportRequest(
        property=f"properties/{config.GA4_PROPERTY_ID}",
        dimensions=[Dimension(name="date")],
        metrics=[Metric(name="sessions"), Metric(name="activeUsers"), Metric(name="screenPageViews")],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
    )
    response = client.run_report(request)
    return response
