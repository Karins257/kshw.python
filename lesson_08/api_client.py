import os

import requests


class YougileProjectsApi:
    def __init__(self, token=None, base_url=None):
        self.base_url = (
            base_url
            or os.getenv("YOUGILE_BASE_URL")
            or "https://yougile.com/api-v2"
        ).rstrip("/")
        self.token = token or os.getenv("YOUGILE_API_TOKEN")

        if not self.token:
            raise ValueError(
                "Set the YOUGILE_API_TOKEN environment variable"
            )

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def create_project(self, payload):
        return requests.post(
            f"{self.base_url}/projects",
            headers=self.headers,
            json=payload,
            timeout=15,
        )

    def update_project(self, project_id, payload):
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
            json=payload,
            timeout=15,
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
            timeout=15,
        )

    def delete_project(self, project_id):
        return self.update_project(project_id, {"deleted": True})
