import httpx

with httpx.Client() as client:
    login_url = "https://leta.mullvad.net/login"
    login_payload = {"account_number": "0123456789012345"} #Replace with your account number!
    login_response = client.post(login_url, data=login_payload, headers={"Origin": "https://leta.mullvad.net"})
    access_token_cookie = login_response.cookies.get("accessToken")


    if access_token_cookie:

        data = {
            "q": "test", #search for the word "test"
            "start": "1", #start from the first result
            "gl": "",
            "oc": "",
        }
        url = "https://leta.mullvad.net"


        with httpx.Client() as client:
            headers = {"Origin": "https://leta.mullvad.net", "Cookie": f"accessToken={access_token_cookie}"}
            response = client.post(url, data=data, headers=headers)


        if response.status_code == 200:
            print("Request succeeded!")
            print("Response:", response.text)
        else:
            print(f"Request failed with status code {response.status_code}")