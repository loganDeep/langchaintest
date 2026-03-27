import requests
import json

GRAFANA_URL = "http://localhost:3000"

API_TOKEN = "TOKENHERE"

DATASOURCE_UID = "ffemv7qkeuk8wf"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def create_dashboard(metric_name="payment_errors_count"):

    dashboard_payload = {
        "dashboard": {
            "id": None,
            "uid": None,
            "title": "Dynamic Payment Dashboard",
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

    response = requests.post(
        f"{GRAFANA_URL}/api/dashboards/db",
        headers=HEADERS,
        data=json.dumps(dashboard_payload)
    )

    print("Status:", response.status_code)
    print("Response:", response.text)


if __name__ == "__main__":
    create_dashboard("payment_errors_count")