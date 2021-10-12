from project import create_app


def test_resorts_get():
    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get('/resorts')
        assert response.status_code == 200
        assert b'Alyeska Resort' in response.data
        assert b'"id": 331' in response.data
        assert len(response.get_json()) == 331

def test_resorts_id_get():
    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get('/resorts/33')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data["average_snowfall"], int)
        assert isinstance(data["base"], int)
        assert isinstance(data["days_open_last_year"], int)
        assert isinstance(data["double"], int)
        assert isinstance(data["fast_eights"], int)
        assert isinstance(data["fast_quads"], int)
        assert isinstance(data["fast_sixes"], int)
        assert isinstance(data["longest_run"], float)
        assert isinstance(data["mi_night_skiing"], int) or data["mi_night_skiing"] is None
        assert isinstance(data["mi_pistes"], int) or data["mi_pistes"] is None
        assert isinstance(data["mi_snow_making"], int) or data["mi_snow_making"] is None
        assert isinstance(data["projected_days_open"], int)
        assert isinstance(data["quad"], int)
        assert isinstance(data["runs"], int)
        assert isinstance(data["skiable_terrain"], int)
        assert isinstance(data["snow_making"], int)
        assert isinstance(data["summit"], int)
        assert isinstance(data["surface"], int)
        assert isinstance(data["terrain_parks"], int)
        assert isinstance(data["total"], int)
        assert isinstance(data["trams"], int)
        assert isinstance(data["triple"], int)
        assert isinstance(data["url"], str)
        assert isinstance(data["vertical_drop"], int)
        assert isinstance(data["years_open"], int)
        assert data["id"] == 33
        assert data["name"] == "Crested Butte Mountain Resort"
        assert data["night_skiing"] == 1 or data["night_skiing"] == 0
        assert data["state"] == "colorado"

def test_resorts_by_state_get():
    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get('/resorts/states/colorado')
        assert response.status_code == 200
        assert b"Snowbird" not in response.data
        assert b"Vail" in response.data
        data = response.get_json()
        assert data[0]["name"] == "Arapahoe Basin Ski Area"
        assert data[2]["id"] == 30
        assert len(response.get_json()) == 22

