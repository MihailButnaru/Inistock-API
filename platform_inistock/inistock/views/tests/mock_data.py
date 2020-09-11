from typing import Dict, List


def mock_input_data_person() -> Dict:
    return {
        "person": {
            "first_name": "Test",
            "last_name": "Smith",
            "date_of_birth": "2020-01-01",
            "email": "testsmith@hotmail.com",
        }
    }


def mock_output_data_person() -> Dict:
    return {
        "person_id": 18,
        "first_name": "Test",
        "last_name": "Smith",
        "date_of_birth": "2020-01-01",
        "email": "testsmith@hotmail.com",
    }


def mock_input_data_share() -> Dict:
    return {
        "share": {
            "company": "Tesla",
            "symbol": "TSLA",
            "shares": "10",
            "type": "sell",
            "date": "2020-01-01",
            "price": 1417,
            "amount": 5000,
            "currency": "GB",
            "note": "great investment",
        }
    }


def mock_output_data_share() -> Dict:
    return {
        "share_id": 2,
        "company": "Tesla",
        "symbol": "TSLA",
        "shares": 10,
        "type": "sell",
        "date": "2020-01-01",
        "price": 1417.0,
        "amount": 5000.0,
        "currency": "GB",
        "note": "great investment",
    }


def mock_output_data_shares() -> List:
    return [
        {
            "share_id": 2,
            "company": "Tesla",
            "symbol": "TSLA",
            "shares": 10,
            "type": "sell",
            "date": "2020-01-01",
            "price": 1417.0,
            "amount": 5000.0,
            "currency": "GB",
            "note": "great investment",
        },
        {
            "share_id": 3,
            "company": "Tesla",
            "symbol": "TSLA",
            "shares": 10,
            "type": "sell",
            "date": "2020-01-01",
            "price": 1417.0,
            "amount": 5000.0,
            "currency": "GB",
            "note": "great investment",
        },
    ]
