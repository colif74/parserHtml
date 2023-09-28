import requests

cookies = {
    '_ym_uid': '1661490011984052894',
    'yandexuid': '1260235541673687955',
    'yuidss': '1260235541673687955',
    'i': '/zFAXGJRW9qk5QQ8jjLFx8CFK1Xqd/nRzuGPW1nSAQHohE1Q9W8Uza45A1fuUd+JYYFMJ2pvxiWHWAt/81oUFSUJdFw=',
    'ymex': '1976850016.yrts.1661490016#1993889878.yrtsi.1678529878',
    'gdpr': '0',
    'L': 'X1tTcXpmf2pkZ2IGf1ZiYkpXUVJIWkhZNTgPEyFtXA==.1681187582.15309.349278.af1af8145dbed7e8d2fa21ad09cdf944',
    'yandex_login': 'colif74',
    'font_loaded': 'YSv1',
    '_ym_d': '1686027161',
    'AMP_332f8b000f': 'JTdCJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJkZXZpY2VJZCUyMiUzQSUyMmIyNGFhNjA2LTJlODYtNGEyOS1iNjI1LWU1NzAyOWQ2ZWJiMyUyMiUyQyUyMmxhc3RFdmVudFRpbWUlMjIlM0ExNjg2OTE3NDE1MjE5JTJDJTIyc2Vzc2lvbklkJTIyJTNBMTY4NjkxNzQxNTA1MCUyQyUyMnVzZXJJZCUyMiUzQTE1MDQ2NTYzJTdE',
    'is_gdpr': '0',
    'is_gdpr_b': 'CPzMERDgvwEoAg==',
    'my': 'YwA=',
    'uxs_uid': 'ff9c85f0-3f22-11ee-a187-5f296a67a12a',
    'yandex_gid': '166895',
    '_ym_isad': '2',
    'Session_id': '3:1695800647.5.0.1681187582713:F2QSsg:5e.1.2:1|257066145.0.2.3:1681187582|3:10276355.422024.uIFp9sjRoWZZX2sZ2sgo-P1LaaE',
    'sessar': '1.1182.CiAIwXwgKQNiAIMLN3ejrT4YhtdYpVUZ8jB4PT3iGbM9iw.ax2hubSJDNCFNf_R35H6RbIA6xQLtuqnKPJNFuc8Oh0',
    'sessionid2': '3:1695800647.5.0.1681187582713:F2QSsg:5e.1.2:1|257066145.0.2.3:1681187582|3:10276355.422024.fakesign0000000000000000000',
    '_yasc': 'XHlvnPPYqLemrhdtXh/92VwAmcQdtQJSD8cH+tHbGDF6XH2Dz4xWAqJQ9TsP4atQDZjZxLEcVg==',
    'bh': 'Ej8iTWljcm9zb2Z0IEVkZ2UiO3Y9IjExNyIsIk5vdDtBPUJyYW5kIjt2PSI4IiwiQ2hyb21pdW0iO3Y9IjExNyIaBSJ4ODYiIg8iMTE3LjAuMjA0NS40MyIqAj8wOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUloiTWljcm9zb2Z0IEVkZ2UiO3Y9IjExNy4wLjIwNDUuNDMiLCJOb3Q7QT1CcmFuZCI7dj0iOC4wLjAuMCIsIkNocm9taXVtIjt2PSIxMTcuMC41OTM4LjkyIiI=',
    'yp': '2011164299.pcs.0#1727336187.p_sw.1695800187#1724993511.p_cl.1693457511#1698479048.hdrc.0#1996547582.udn.cDpjb2xpZjc0#1724993513.p_undefined.1693457512#1704209717.szm.1_5:1360x768:789x411#1697946164.ygu.1',
    'bh': 'EkEiTWljcm9zb2Z0IEVkZ2UiO3Y9IjExNyIsICJOb3Q7QT1CcmFuZCI7dj0iOCIsICJDaHJvbWl1bSI7dj0iMTE3IhoFIng4NiIiDyIxMTcuMC4yMDQ1LjM2IioCPzAyAiIiOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUlsiTWljcm9zb2Z0IEVkZ2UiO3Y9IjExNy4wLjIwNDUuMzYiLCAiTm90O0E9QnJhbmQiO3Y9IjguMC4wLjAiLCAiQ2hyb21pdW0iO3Y9IjExNy4wLjU5MzguODkiWgI/MA==',
    'ys': 'udn.cDpjb2xpZjc0#wprid.1695800850479505-12693305556077848376-balancer-l7leveler-kubr-yp-sas-71-BAL-2488#c_chck.2215095127',
    'cycada': 'wknqbLsnkyu0RcgZ6KPoTkGL8DMeqMz9VaR6iCneeh4=',
}

headers = {
    'authority': 'yandex.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    # 'cookie': '_ym_uid=1661490011984052894; yandexuid=1260235541673687955; yuidss=1260235541673687955; i=/zFAXGJRW9qk5QQ8jjLFx8CFK1Xqd/nRzuGPW1nSAQHohE1Q9W8Uza45A1fuUd+JYYFMJ2pvxiWHWAt/81oUFSUJdFw=; ymex=1976850016.yrts.1661490016#1993889878.yrtsi.1678529878; gdpr=0; L=X1tTcXpmf2pkZ2IGf1ZiYkpXUVJIWkhZNTgPEyFtXA==.1681187582.15309.349278.af1af8145dbed7e8d2fa21ad09cdf944; yandex_login=colif74; font_loaded=YSv1; _ym_d=1686027161; AMP_332f8b000f=JTdCJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJkZXZpY2VJZCUyMiUzQSUyMmIyNGFhNjA2LTJlODYtNGEyOS1iNjI1LWU1NzAyOWQ2ZWJiMyUyMiUyQyUyMmxhc3RFdmVudFRpbWUlMjIlM0ExNjg2OTE3NDE1MjE5JTJDJTIyc2Vzc2lvbklkJTIyJTNBMTY4NjkxNzQxNTA1MCUyQyUyMnVzZXJJZCUyMiUzQTE1MDQ2NTYzJTdE; is_gdpr=0; is_gdpr_b=CPzMERDgvwEoAg==; my=YwA=; uxs_uid=ff9c85f0-3f22-11ee-a187-5f296a67a12a; yandex_gid=166895; _ym_isad=2; Session_id=3:1695800647.5.0.1681187582713:F2QSsg:5e.1.2:1|257066145.0.2.3:1681187582|3:10276355.422024.uIFp9sjRoWZZX2sZ2sgo-P1LaaE; sessar=1.1182.CiAIwXwgKQNiAIMLN3ejrT4YhtdYpVUZ8jB4PT3iGbM9iw.ax2hubSJDNCFNf_R35H6RbIA6xQLtuqnKPJNFuc8Oh0; sessionid2=3:1695800647.5.0.1681187582713:F2QSsg:5e.1.2:1|257066145.0.2.3:1681187582|3:10276355.422024.fakesign0000000000000000000; _yasc=XHlvnPPYqLemrhdtXh/92VwAmcQdtQJSD8cH+tHbGDF6XH2Dz4xWAqJQ9TsP4atQDZjZxLEcVg==; bh=Ej8iTWljcm9zb2Z0IEVkZ2UiO3Y9IjExNyIsIk5vdDtBPUJyYW5kIjt2PSI4IiwiQ2hyb21pdW0iO3Y9IjExNyIaBSJ4ODYiIg8iMTE3LjAuMjA0NS40MyIqAj8wOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUloiTWljcm9zb2Z0IEVkZ2UiO3Y9IjExNy4wLjIwNDUuNDMiLCJOb3Q7QT1CcmFuZCI7dj0iOC4wLjAuMCIsIkNocm9taXVtIjt2PSIxMTcuMC41OTM4LjkyIiI=; yp=2011164299.pcs.0#1727336187.p_sw.1695800187#1724993511.p_cl.1693457511#1698479048.hdrc.0#1996547582.udn.cDpjb2xpZjc0#1724993513.p_undefined.1693457512#1704209717.szm.1_5:1360x768:789x411#1697946164.ygu.1; bh=EkEiTWljcm9zb2Z0IEVkZ2UiO3Y9IjExNyIsICJOb3Q7QT1CcmFuZCI7dj0iOCIsICJDaHJvbWl1bSI7dj0iMTE3IhoFIng4NiIiDyIxMTcuMC4yMDQ1LjM2IioCPzAyAiIiOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUlsiTWljcm9zb2Z0IEVkZ2UiO3Y9IjExNy4wLjIwNDUuMzYiLCAiTm90O0E9QnJhbmQiO3Y9IjguMC4wLjAiLCAiQ2hyb21pdW0iO3Y9IjExNy4wLjU5MzguODkiWgI/MA==; ys=udn.cDpjb2xpZjc0#wprid.1695800850479505-12693305556077848376-balancer-l7leveler-kubr-yp-sas-71-BAL-2488#c_chck.2215095127; cycada=wknqbLsnkyu0RcgZ6KPoTkGL8DMeqMz9VaR6iCneeh4=',
    'device-memory': '4',
    'downlink': '10',
    'dpr': '1.5',
    'ect': '4g',
    'referer': 'https://yandex.ru/',
    'rtt': '100',
    'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"117.0.2045.36"',
    'sec-ch-ua-full-version-list': '"Microsoft Edge";v="117.0.2045.36", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.89"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36',
    'viewport-width': '350',
}

params = {
    'text': 'pornohub',
    'lr': '166895',
    'clid': '2411726',
    'suggest_reqid': '126023554167368795508517705987239',
}

response = requests.get('https://rt.pornhub.com/', params=params, cookies=cookies, headers=headers)

with open('resalt.html', 'w') as file:
    file.write(response.text)