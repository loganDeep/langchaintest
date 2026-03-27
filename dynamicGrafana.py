import requests
import json

GRAFANA_URL = "http://localhost:3000"
API_TOKEN = "TOKENHERE"
DATASOURCE_UID = "datasourceid"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def create_dashboard(metric_name: str = "payment_errors_count") -> None:
    """
    Create a Grafana dashboard with a single timeseries panel for the given metric.
    """
    dashboard_payload = {
        "dashboard": {
            "id": None,
            "uid": None,
            "title": f"Dynamic Dashboard: {metric_name}",
            "timezone": "browser",
            "schemaVersion": 38,
            "version": 1,
            "panels": [
                {
                    "type": "timeseries",
                    "title": f"{metric_name} Over Time",
                    "datasource": {
                        "type": "prometheus",
                        "uid": DATASOURCE_UID
                    },
                    "targets": [
                        {
                            "expr": metric_name,
                            "refId": "A"
                        }
                    ],
                    "gridPos": {
                        "x": 0,
                        "y": 0,
                        "w": 24,
                        "h": 10
                    }
                }
            ]
        },
        "overwrite": True
    }

    try:
        response = requests.post(
            f"{GRAFANA_URL}/api/dashboards/db",
            headers=HEADERS,
            data=json.dumps(dashboard_payload)
        )
        response.raise_for_status()
        print(f"Dashboard for '{metric_name}' created successfully.")
    except requests.RequestException as e:
        print(f"Failed to create dashboard: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print("Response:", e.response.text)

if __name__ == "__main__":
    # Change the metric name here as needed
    create_dashboard("payment_errors_count")