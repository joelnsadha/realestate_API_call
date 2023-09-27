import pandas
import pandas as pd
import requests
import json


def extract_dataframe(pages):
    """
    Takes number of pages to scrape and returns listings in a pandas DataFrame.
    For better performance, run no more than 10 pages at a time
    :param pages: Int number of web pages to scrape.
    :return: Pandas Dataframe
    """
    ids = []
    user_ids = []
    titles = []
    regions = []
    locations = []
    prices = []
    bedrooms = []
    bathrooms = []
    user_phones = []


    # Run a for loop for number of pages to return
    for page in range(1, pages+1):
        cookies = {
        'first_visit': '1695471844',
        'uid': '9ec940e6be470e14719a31968c61a9db2aa962cc',
        'lang': 'en',
        '_gcl_au': '1.1.2131952790.1695471841',
        'g_state': '{"i_l":0}',
        'app': '7af23abe2dba492b85e76f1ba76c3ba3',
        'change-language-popup': '1',
        'rid': 'jiji.ug',
        '_js2': 'BIkP6-p6dFzL44CZfsbOU1-VdF0OQc-c_H3UWdjJkjI%3D',
        'app_sid': '1695483519957',
        }

        headers = {
            'authority': 'jiji.ug',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'first_visit=1695471844; uid=9ec940e6be470e14719a31968c61a9db2aa962cc; lang=en; _gcl_au=1.1.2131952790.1695471841; g_state={"i_l":0}; app=7af23abe2dba492b85e76f1ba76c3ba3; change-language-popup=1; rid=jiji.ug; _js2=BIkP6-p6dFzL44CZfsbOU1-VdF0OQc-c_H3UWdjJkjI%3D; app_sid=1695483519957',
            'referer': 'https://jiji.ug/houses-apartments-for-sale',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-csrf-token': 'ImRhZDVkZjQyZmNkNThlOTUzZGJmYjk2YjZkYWU4NzhlMWY5NWQ2NjUi.ZQ8FlQ.jbzO8T3DVLFa_-lexiGJ2zGZLhY',
            'x-listing-id': '4S9lXpSw727vwUXc',
        }

        params = {
            'slug': 'houses-apartments-for-sale',
            'init_page': 'true',
            'page': f'{page}',
            'webp': 'true',
            'lsmid': '1695483663957',
        }

        # Get API response from jiji.ug
        response = requests.get('https://jiji.ug/api_web/v1/listing',
                                params=params,
                                cookies=cookies,
                                headers=headers
                                ).json()

        # Get ads from API response
        ads = response['adverts_list']['adverts']

        # Append ad details to lists
        for ad in ads:
            ids.append(ad['id'])
            user_ids.append(ad['user_id'])
            user_phones.append(ad['user_phone'])
            titles.append(ad['title'])
            regions.append(ad["region_item_text"])
            locations.append(ad["region_name"])
            prices.append(ad["price_obj"]["value"])

            # Check to see if "attrs" is not empty
            if ad['attrs']:
                # Loop through the "attrs" list and extract the "Bedrooms" value if it exists
                for attr in ad['attrs']:
                    if attr.get("name") == "Bedrooms":
                        bedroom_value = attr.get("value")
                        if bedroom_value is not None:
                            bedrooms.append(bedroom_value)
            else:
                # If "attrs" is empty, append "na" to the list
                bedrooms.append("na")

            # Check to see if attrs is not empty
            if ad['attrs']:
                # Loop through the "attrs" list and extract the "Bedrooms" value if it exists
                for attr in ad['attrs']:
                    if attr.get("name") == "Bathrooms":
                        bathroom_value = attr.get("value")
                        if bathroom_value is not None:
                            bathrooms.append(bathroom_value)
            else:
                bathrooms.append("na")

        # Create dictionary from extracted data
        data = {
            "id": ids,
            "user_id": user_ids,
            "user_phone": user_phones,
            "title": titles,
            "region": regions,
            "location": locations,
            "price": prices,
            "bedroom": bedrooms,
            "bathroom": bathrooms
        }

    # Create pandas dataframe
    df = pd.DataFrame(data)

    return df


