import requests # сбор всей разметки страницы

cookies = {
    'secure_customer_sig': '',
    'localization': 'KZ',
    'cart_currency': 'KZT',
    '_tracking_consent': '%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22m%22%3A%22%22%2C%22p%22%3A%22%22%2C%22s%22%3A%22%22%7D%7D%2C%22v%22%3A%222.1%22%2C%22region%22%3A%22KZ19%22%2C%22reg%22%3A%22%22%7D',
    '_cmp_a': '%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D',
    '_shopify_y': 'b2f6a748-2324-4892-9a99-4d928c74c07e',
    '_orig_referrer': '',
    '_landing_page': '%2F',
    '_ks_scriptVersion': '311',
    '_ks_scriptVersionChecked': 'true',
    'cart': 'Z2NwLWV1cm9wZS13ZXN0MTowMUo4VkZNVzA3RUtENEY3MU1EOTFDR0owWA%3Fkey%3Ddbf47c8ebaf3613d6d6a3b632ffcda41',
    '_gid': 'GA1.2.130505531.1727499238',
    '_fbp': 'fb.1.1727499240048.39130434931743954',
    '_seedSeenWelcomeMat': 'true',
    'GLBE_SESS_ID': '744238364.558484689.62000001',
    'ftr_ncd': '6',
    '_hjSessionUser_3197066': 'eyJpZCI6ImY1ODg5ZGE4LTM5MTYtNWFmYS1iNDNhLWU5ZWQzMzk2ZGQwYSIsImNyZWF0ZWQiOjE3Mjc0OTkyMzYzMDEsImV4aXN0aW5nIjp0cnVlfQ==',
    'datadome': 'k8qLVlQV1SUbVuIeS6YNSzX2aiau7tpcuyYaltQIRwWHejXQlbOAcqXeCpXcp98LSlD9M8_cmy8Nl8gkzca8Y8g_13Be7vLuDRXdNqfP3QFQB_jgS3CWCD01I9bOBs8k',
    '_ks_userCountryUnit': '1',
    '_ks_countryCodeFromIP': 'KZ',
    'receive-cookie-deprecation': '1',
    '_shopify_sa_p': '',
    '_hjSession_3197066': 'eyJpZCI6IjJhMDBjM2M2LTZkNTYtNDFhYS1hYTFiLWZkYWMzOTk0YjZmMiIsImMiOjE3Mjc1MjA2MTA3MDcsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
    '_gat': '1',
    'shopify_pay_redirect': 'pending',
    'snize-recommendation': 'pyzfdrd2dsk',
    'GlobalE_Consent': '%7B%22required%22%3Afalse%2C%22groups%22%3A%7B%221%22%3A1%2C%222%22%3A1%2C%223%22%3A1%7D%7D',
    'keep_alive': '114b5cbc-7461-4fd8-b5bf-1866f90ab7ca',
    '_shopify_s': '3f6387a2-8d35-4493-8d3a-353571141cdc',
    '_shopify_sa_t': '2024-09-28T10%3A50%3A24.695Z',
    '_ga_XJVC3NDTFF': 'GS1.1.1727520611.4.1.1727520624.0.0.0',
    '_ga': 'GA1.1.914798617.1727499238',
    '_ga_JZ85N5WWY7': 'GS1.1.1727520611.4.1.1727520624.0.0.0',
    '_ga_WNZZTBNSWB': 'GS1.1.1727520611.4.1.1727520624.0.0.0',
    'geo_data': '{%22as%22:%22AS206026%20Kar-Tel%20LLC%22%2C%22asname%22:%22ipnet_kar-tel%22%2C%22mobile%22:true%2C%22proxy%22:false%2C%22city%22:%22Almaty%22%2C%22currency%22:{%22code%22:%22KZT%22}%2C%22country%22:{%22code%22:%22KZ%22%2C%22country%22:%22Kazakhstan%22}%2C%22countryCode%22:%22KZ%22%2C%22continent%22:%22Asia%22%2C%22continentCode%22:%22AS%22%2C%22isp%22:%22Kar-Tel%20LLC%22%2C%22lat%22:43.2433%2C%22lon%22:76.8646%2C%22org%22:%22Kar-Tel%20LLC%22%2C%22query%22:%22198.45.119.228%22%2C%22region%22:%2275%22%2C%22regionName%22:%22Almaty%22%2C%22status%22:%22success%22%2C%22timezone%22:%22Asia/Almaty%22%2C%22zip%22:%22%22%2C%22cloudflare%22:%22KZ%22%2C%22ttl%22:2386%2C%22env%22:%22PROD%22%2C%22build%22:%22ip-api%20cached%22%2C%22currencyCode%22:%22KZT%22%2C%22countryName%22:%22Kazakhstan%22%2C%22service%22:%22ip.lovely-app.com%22}',
    '__kla_id': 'eyIkZXhjaGFuZ2VfaWQiOiJoWXc3NG5yLWFjaUlVbUpDMDI3ZEJWWmNsTHl3YnA1Z21Wd0hETm1BNG04Lm5OS1hCVCJ9',
    'SHOPLIFT': '{"id":"c6ec686d-5319-4956-8117-ff27c7d89e9d","createdAt":"2024-09-28T05:33:31.745502Z","device":"desktop","utmSource":"","utmMedium":"","utmCampaign":"","utmContent":"","referrer":"","needsPersistence":false,"visitorTests":[],"storedAt":"2024-09-28T10:50:25.341Z","isProcessing":false}',
    'forterToken': '1b679bdefb154def9e921ac38b28877d_1727520625743__UDF43-m4_9ck_',
    'cart_ts': '1727520625',
    'cart_sig': '0d39e660dd2a8c8dd8c52c35ae1395bc',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'secure_customer_sig=; localization=KZ; cart_currency=KZT; _tracking_consent=%7B%22con%22%3A%7B%22CMP%22%3A%7B%22a%22%3A%22%22%2C%22m%22%3A%22%22%2C%22p%22%3A%22%22%2C%22s%22%3A%22%22%7D%7D%2C%22v%22%3A%222.1%22%2C%22region%22%3A%22KZ19%22%2C%22reg%22%3A%22%22%7D; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22sale_of_data_region%22%3Afalse%7D; _shopify_y=b2f6a748-2324-4892-9a99-4d928c74c07e; _orig_referrer=; _landing_page=%2F; _ks_scriptVersion=311; _ks_scriptVersionChecked=true; cart=Z2NwLWV1cm9wZS13ZXN0MTowMUo4VkZNVzA3RUtENEY3MU1EOTFDR0owWA%3Fkey%3Ddbf47c8ebaf3613d6d6a3b632ffcda41; _gid=GA1.2.130505531.1727499238; _fbp=fb.1.1727499240048.39130434931743954; _seedSeenWelcomeMat=true; GLBE_SESS_ID=744238364.558484689.62000001; ftr_ncd=6; _hjSessionUser_3197066=eyJpZCI6ImY1ODg5ZGE4LTM5MTYtNWFmYS1iNDNhLWU5ZWQzMzk2ZGQwYSIsImNyZWF0ZWQiOjE3Mjc0OTkyMzYzMDEsImV4aXN0aW5nIjp0cnVlfQ==; datadome=k8qLVlQV1SUbVuIeS6YNSzX2aiau7tpcuyYaltQIRwWHejXQlbOAcqXeCpXcp98LSlD9M8_cmy8Nl8gkzca8Y8g_13Be7vLuDRXdNqfP3QFQB_jgS3CWCD01I9bOBs8k; _ks_userCountryUnit=1; _ks_countryCodeFromIP=KZ; receive-cookie-deprecation=1; _shopify_sa_p=; _hjSession_3197066=eyJpZCI6IjJhMDBjM2M2LTZkNTYtNDFhYS1hYTFiLWZkYWMzOTk0YjZmMiIsImMiOjE3Mjc1MjA2MTA3MDcsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _gat=1; shopify_pay_redirect=pending; snize-recommendation=pyzfdrd2dsk; GlobalE_Consent=%7B%22required%22%3Afalse%2C%22groups%22%3A%7B%221%22%3A1%2C%222%22%3A1%2C%223%22%3A1%7D%7D; keep_alive=114b5cbc-7461-4fd8-b5bf-1866f90ab7ca; _shopify_s=3f6387a2-8d35-4493-8d3a-353571141cdc; _shopify_sa_t=2024-09-28T10%3A50%3A24.695Z; _ga_XJVC3NDTFF=GS1.1.1727520611.4.1.1727520624.0.0.0; _ga=GA1.1.914798617.1727499238; _ga_JZ85N5WWY7=GS1.1.1727520611.4.1.1727520624.0.0.0; _ga_WNZZTBNSWB=GS1.1.1727520611.4.1.1727520624.0.0.0; geo_data={%22as%22:%22AS206026%20Kar-Tel%20LLC%22%2C%22asname%22:%22ipnet_kar-tel%22%2C%22mobile%22:true%2C%22proxy%22:false%2C%22city%22:%22Almaty%22%2C%22currency%22:{%22code%22:%22KZT%22}%2C%22country%22:{%22code%22:%22KZ%22%2C%22country%22:%22Kazakhstan%22}%2C%22countryCode%22:%22KZ%22%2C%22continent%22:%22Asia%22%2C%22continentCode%22:%22AS%22%2C%22isp%22:%22Kar-Tel%20LLC%22%2C%22lat%22:43.2433%2C%22lon%22:76.8646%2C%22org%22:%22Kar-Tel%20LLC%22%2C%22query%22:%22198.45.119.228%22%2C%22region%22:%2275%22%2C%22regionName%22:%22Almaty%22%2C%22status%22:%22success%22%2C%22timezone%22:%22Asia/Almaty%22%2C%22zip%22:%22%22%2C%22cloudflare%22:%22KZ%22%2C%22ttl%22:2386%2C%22env%22:%22PROD%22%2C%22build%22:%22ip-api%20cached%22%2C%22currencyCode%22:%22KZT%22%2C%22countryName%22:%22Kazakhstan%22%2C%22service%22:%22ip.lovely-app.com%22}; __kla_id=eyIkZXhjaGFuZ2VfaWQiOiJoWXc3NG5yLWFjaUlVbUpDMDI3ZEJWWmNsTHl3YnA1Z21Wd0hETm1BNG04Lm5OS1hCVCJ9; SHOPLIFT={"id":"c6ec686d-5319-4956-8117-ff27c7d89e9d","createdAt":"2024-09-28T05:33:31.745502Z","device":"desktop","utmSource":"","utmMedium":"","utmCampaign":"","utmContent":"","referrer":"","needsPersistence":false,"visitorTests":[],"storedAt":"2024-09-28T10:50:25.341Z","isProcessing":false}; forterToken=1b679bdefb154def9e921ac38b28877d_1727520625743__UDF43-m4_9ck_; cart_ts=1727520625; cart_sig=0d39e660dd2a8c8dd8c52c35ae1395bc',
    'if-none-match': '"cacheable:2901b0f70d19b7dce5c33784499657ad"',
    'priority': 'u=0, i',
    'referer': 'https://kith.com/',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

response = requests.get('https://kith.com/pages/shop-mens', cookies=cookies, headers=headers)

with open('kith.html', 'w', encoding='utf-8') as f:
    f.write(response.text)