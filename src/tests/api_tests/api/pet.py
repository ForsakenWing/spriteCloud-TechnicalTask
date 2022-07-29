from faker import Faker
from random import randint
import logging


logger = logging.getLogger('faker')
logger.setLevel(logging.INFO)


fake = Faker()


class Pet:

    id: int
    info: dict

    @staticmethod
    def generate_valid_add_pet_to_store_body():
        return {
                "id": int(fake.msisdn()),
                "category": {
                    "id": int(fake.msisdn()),
                    "name": fake.name()
                },
                "name": fake.name(),
                "photoUrls": [
                    fake.url() for _ in range(randint(2, 10))
                ],
                "tags": [
                    {
                        "id": int(fake.msisdn()),
                        "name": fake.name()
                    }
                ],
                "status": fake.job()
            }

    @staticmethod
    def generate_invalid_add_pet_to_store_body():
        return {
            "id": "ABRACADABRA",
            "category": {
                "id": "WHICH?",
                "name": 111111
            },
            "name": 11111,
            "photoUrls": [
                "I AM NOT URL"
            ],
            "tags": [
                {
                    "id": "I AM NOT VALID TAG ID",
                    "name": 11111
                }
            ],
            "status": 3333
        }

