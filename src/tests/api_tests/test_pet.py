from . import Pet, post_request, get_request


import pytest


@pytest.fixture(autouse=True, scope="session")
def pet() -> Pet:
    pet = Pet()
    return pet


class TestPet:

    def test_positive_scenario_adding_pet_to_store(self, pet):
        expected_data = pet.generate_valid_add_pet_to_store_body()
        pet.info = expected_data
        response = post_request(
            url="https://petstore.swagger.io/v2/pet",
            json=expected_data
        )
        actual_data = response.json()
        pet.id = actual_data['id']
        assert expected_data == actual_data
        assert response.status_code == 200

    def test_negative_scenario_adding_pet_to_store(self, pet):
        response = post_request(
            url="https://petstore.swagger.io/v2/pet",
            json=pet.generate_invalid_add_pet_to_store_body()
        )
        if response.status_code not in range(400, 500):
            pytest.fail(
                f"\nINVALID status code={response.status_code}\n"
                f"Expected status code in range 400-499 (Client Error)"
            )

    def test_find_pet_by_id(self, pet):
        response = get_request(url=f"https://petstore.swagger.io/v2/pet/{pet.id}")
        actual_data = response.json()
        expected_data = pet.info
        assert actual_data == expected_data
        assert response.status_code == 200

    def test_updating_an_existing_pet(self, pet):
        ...

    def test_delete_pet(self, pet):
        ...