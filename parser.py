import requests
from bs4 import BeautifulSoup as bs

# 로그인할 유저정보를 넣어주자 (모두 문자열)
LOGIN_INFO = {"userId": "wsdclub", "userPassword": "gosdkdi123"}
# Session 생성, with 구문 안에서 유지
with requests.Session() as s:

    first_page = s.get("https://www.clien.net/service")
    html = first_page.text
    soup = bs(html, "html.parser")
    csrf = soup.find("input", {"name": "_csrf"})
    print(csrf["value"])

    LOGIN_INFO = {**LOGIN_INFO, **{"_csrf": csrf["value"]}}
    print(LOGIN_INFO)

    login_req = s.post("https://www.clien.net/service/login", data=LOGIN_INFO)

    print(login_req.status_code)

    if login_req.status_code != 200:
        raise Exception("로그인이 되지 않았습니다. ID&PW를 확인하세요")

    # 여기서 부터 로그인이 된 세션이 유지됩니다.
    post_one = s.get("https://www.clien.net/service/board/sold?category=판매")
    html = post_one.text
    soup = bs(html, "html.parser")

    # print(soup)
    # 판매장터 올라온 품목
    item_list = soup.findAll("div", {"class": "list_title"})

    # for li in item_list:
    #     item = li.find("span", {"class": "subject_fixed"})
    #     print(item)

    for idx, var in enumerate(item_list):
        item = var.find("span", {"class": "subject_fixed"})
        print(idx, item)

    # # HTTP GET Request: requests대신 s객체를 사용한다.
    # req = s.get("https://www.clien.net/service")

    # # HTML 소스 가져오기
    # html = req.text

    # # HTTP Header 가져오기
    # header = req.headers

    # # HTTP Status 가져오기 (200: 정상)
    # status = req.status_code

    # # HTTP가 정상적으로 되었는지 (True/False)
    # is_ok = req.ok

