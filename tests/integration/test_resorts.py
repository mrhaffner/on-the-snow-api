from project import create_app


def test_get_resorts():
    flask_app = create_app('flask_test.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/resorts')
        assert response.status_code == 200
        assert b'Alyeska Resort' in response.data
        assert b'"id": 331' in response.data
        assert len(response.get_json()) == 331