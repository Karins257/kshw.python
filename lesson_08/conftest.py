import os
from uuid import uuid4

import pytest

from api_client import YougileProjectsApi


@pytest.fixture(scope="session")
def projects_api():
    token = os.getenv("YOUGILE_API_TOKEN")
    if not token:
        pytest.skip("YOUGILE_API_TOKEN is not set")
    return YougileProjectsApi(token=token)


@pytest.fixture
def project(projects_api):
    title = f"SkyPro API test {uuid4()}"
    response = projects_api.create_project({"title": title})
    assert response.status_code == 201

    project_id = response.json()["id"]
    yield {"id": project_id, "title": title}

    projects_api.delete_project(project_id)
