import requests


def prep_data(data_list):
    data = {}
    for i in range(len(data_list)):
        data[f"value{i+1}"] = data_list[i]
        i += 1
    return data


def send_data(endpoint, data):
    response = requests.post(
        endpoint,
        json=prep_data(data)
    )
    print(response)
