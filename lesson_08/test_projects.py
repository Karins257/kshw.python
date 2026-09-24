from uuid import uuid4


def test_create_project_positive(projects_api):
    title = f"SkyPro create test {uuid4()}"
    response = projects_api.create_project({"title": title})

    assert response.status_code == 201
    project_id = response.json()["id"]

    created_project = projects_api.get_project(project_id)
    assert created_project.status_code == 200
    assert created_project.json()["title"] == title

    projects_api.delete_project(project_id)


def test_create_project_without_title(projects_api):
    response = projects_api.create_project({})

    assert response.status_code == 400
    assert "error" in response.json()


def test_update_project_positive(projects_api, project):
    new_title = f"SkyPro updated test {uuid4()}"
    response = projects_api.update_project(
        project["id"],
        {"title": new_title},
    )

    assert response.status_code == 200
    assert response.json()["id"] == project["id"]

    updated_project = projects_api.get_project(project["id"])
    assert updated_project.json()["title"] == new_title


def test_update_missing_project(projects_api):
    response = projects_api.update_project(
        str(uuid4()),
        {"title": "Project does not exist"},
    )

    assert response.status_code == 404
    assert "error" in response.json()


def test_get_project_positive(projects_api, project):
    response = projects_api.get_project(project["id"])

    assert response.status_code == 200
    assert response.json()["id"] == project["id"]
    assert response.json()["title"] == project["title"]


def test_get_missing_project(projects_api):
    response = projects_api.get_project(str(uuid4()))

    assert response.status_code == 404
    assert "error" in response.json()
