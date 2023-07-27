from rest_framework.test import testcases

class ElevatorViewsetTestCase(testcases):

    fixtures = ['Elevator.json','Status.json']

    def test_list_elevator(self):

        response = self.client.get('/api/elevator/')
        assert response.status_code == 200

    def test_retrieve_elevator(self):

        response = self.client.get('/api/elev_retr/2/')
        assert response.status_code == 200

    