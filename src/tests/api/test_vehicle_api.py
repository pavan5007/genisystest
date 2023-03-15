import requests
import pytest
import json

url = "https://crudcrud.com/api/eb112b0689bd4cfb962d39f89122cfba/vehicle"
headers ={"Content-Type":"application/json"}

@pytest.mark.smoke
def test_create_user():
    payload = json.dumps({
    "name":"Car",
    "brand":"benz",
    "cost":10000000
    })
    response = requests.post(url=url,headers=headers,data=payload)
    assert response.status_code == 201
    result = response.json()
    assert result["_id"] is not None
    assert result["name"] == "Car"
    assert result["brand"] == "benz"
    assert result["cost"] == 10000000

@pytest.mark.smoke
def test_get_user():
    response = requests.get(url=url,headers=headers)
    assert response.status_code == 200
    result = response.json()
    if len(result) > 0:
        for data in result:
            assert data["_id"] is not None
            assert data["name"] is not None
            assert data["brand"] is not None
            assert data["cost"] is not None

@pytest.mark.smoke
def test_update_user():
    response = requests.get(url=url, headers=headers)
    result = response.json()
    id = result[0]["_id"]
    temp_url = url +'/'+id
    data =json.dumps({
    "name":"Truck",
    "brand":"benz",
    "cost":10000000
    })
    response = requests.put(temp_url,headers=headers,data=data)
    assert response.status_code == 200


@pytest.mark.smoke
def test_delete_user():
    response = requests.get(url=url, headers=headers)
    result = response.json()
    id = result[0]["_id"]
    temp_url = url +'/'+id
    response = requests.delete(temp_url)
    assert response.status_code == 200

