import requests

header = {
   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' ,
   'accept-language': 'ar,en-US;q=0.9,en;q=0.8' ,
   'cookie': '_gcl_au=1.1.1590758377.1722584574; _hjSessionUser_911455=eyJpZCI6ImEyMWFiMGYyLTkzYjktNWIyYS04MmRiLTI1Yjc3YzdiMWVjYSIsImNyZWF0ZWQiOjE3MjI1ODQ1NzU5NTYsImV4aXN0aW5nIjp0cnVlfQ==; intercom-device-id-tsadiujc=5fd57dc5-a113-478e-8b09-c7cce2c0c624; _hjHasCachedUserAttributes=true; __saaid=c9DGvnmN02apjJWwTS8oDnumvBho96ErZ07UPZ3H; remember_user_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6ImlWWVVxNWREMWwvVXQ2RWdlTFBwbmc9PSIsInZhbHVlIjoidHFHL3RsUG5RMG80ZkhiR2R6Y05vQ3NPWU53Zm42RVRRNUFVR1Z5YXZLZi8xb2VERCtERm5ocDN5NzkxbU1scHllKzNHUWdYWTN6Q01XUklJOUFvUWlmOU1nTFo0cFZlRUtxaTd5QjR2cURWVGFQTlBIMWdwVitJOGJ2bnlxSkc2bVR3WkZHUGpLT2hRZTFhblVNZDRSSGZkTHVHRlAyZG5OWE9lS29Ga0tVc0Uva2x0NUo3R2lVcHZmbUhMTUhIdFVnc2lnWDJKNnBkajJiNEdyd3dqWVU2Zk8rYnN5L24vUWZvRXhLR2pEVT0iLCJtYWMiOiI0YjVhMDc5MTc5NzcxOWZmNTAzN2M4Yzg5ZjdkNjQ3YjU0OTJmYzcxNDc5ZTM4ZDQzOWMyZjk4MDlhZDBkMWMwIiwidGFnIjoiIn0%3D; __ssid=52540da27f22ac6289f4825a26393c0; s_domains_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Muc2FsbGEuc2EiLCJpYXQiOjE3MjM5MTI2NDMsImV4cCI6MTcyMzkzNDI0MywibmJmIjoxNzIzOTEyNjQzLCJqdGkiOiJVQ1VXVTNLNkYzVjRuTVBWIiwic3ViIjozNDk4ODIwLCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3Iiwic291cmNlIjoiYXBpLWRhc2hib2FyZCIsInJ0aSI6MH0.hdwTS0DxEzjoYGctHdv87q6LZZ9uWHkQOytgNsUIrGI; __cflb=0H28vmGf6jn2q14MzbvXWy5yxFpAuDUb87HGkoKvkGk; _gid=GA1.2.374584549.1724086750; homepage.run-once=1; _ga=GA1.1.92343697.1722584575; _hjSessionUser_3004400=eyJpZCI6ImM1ZDg1ZjdmLWFjY2ItNTQzOC1iNmUzLTgyZDg5MjM2ODQxNSIsImNyZWF0ZWQiOjE3MjQwOTQ0MjgwMzAsImV4aXN0aW5nIjpmYWxzZX0=; utm_source=eyJpdiI6Im53ZFNXT2tNMG9aR3RUekI3YngwTHc9PSIsInZhbHVlIjoiK01jUHZPR2MvUko2WHFJa2xTTVhadExEbTJZY0NBbFFvT24yQkRoWFgxQzNMd1hFWkN6UVl3S3d6WXZBbTBrSCIsIm1hYyI6IjYxZDk4ZWQzZDZjNmJhM2VmNjRmOWMwOWY0MWIxM2Y0YzM3ZTU2NDIwYjFlYjZhMDg0ZGMwNWMyZjhkZTcyNjUiLCJ0YWciOiIifQ%3D%3D; utm_campaign=eyJpdiI6IlAwVncxVEYrRjByamREbVF3ZlYxRWc9PSIsInZhbHVlIjoiNko3ZUprRzNuTGsyTC9URTB3TC9wVXJJTmxmL0N6MG0yZlVpZTVkNlZaVXFIUjVuUW5hTGk2T1dLV3RwM095dCIsIm1hYyI6ImY2YTE1NDE5NWI3ZTZiZmQ0ZjFmM2EwYWM2NjRhN2E3YTI5NmQ4M2Y5YTE2M2Y1Y2Y1MDQwZmU4MDIxZTUyNzQiLCJ0YWciOiIifQ%3D%3D; utm_medium=eyJpdiI6IlVYSHE3SHRGVjMvYVNWeHlyWWo0SXc9PSIsInZhbHVlIjoiOXpqRG02Zi8yM2NqWWtaYm9abkIrWFgvYW93TmdoN0M3VjZUN2ZRWmVjQi9TSFFsUzhrcXRxSUNMMTFkQXVxNXlvK3lJeGFLa0tndXk5VGxGWmNaQVE9PSIsIm1hYyI6ImY4NDkwYjc2MWYxMWE0NDcwODdjNjkyZjgxMTJjYTdjNzU5ODk4MDExNWUwMzdlOWQ5MTM0MTljZDdmYTNiNjMiLCJ0YWciOiIifQ%3D%3D; utm_referer=eyJpdiI6IllTWURUMXNFOUpYMXh2enE5MS9WVVE9PSIsInZhbHVlIjoiNkFHa3NhbXYzSVFEZGJCNWQrUVlCUEp3K3B2Z3NUZXZwNEQ1MVh1UUpnTnJJazdRSWFndis2Q3hMUzQ1a1RkRXVrSFE5a0NmbDFUc1ovakxqYVZoUlE9PSIsIm1hYyI6ImQzYjYyOWY1ZTU0NmNkN2RjNjFhMGQ3YTFjNzhmMDdlMzljMTU1ZWY3ZjY3OTA0ZTZlM2RiMDUzMWEzYTlkNWUiLCJ0YWciOiIifQ%3D%3D; _ga_ZY5GVCRQKE=GS1.1.1724094428.1.1.1724094537.0.0.0; cf_clearance=ERHV9HvxDXJFahoLChd7.RjRVV0.F_HuoItfGoz0evg-1724156840-1.2.1.1-SMxszxE9SZfuI4olJReJSpbwj8cFm5zmb4MGyXd59vJwd43SY4vHlx6C74r2o2_lCuTBKRWMCxTYxxdXqdR6GIrSspG6pybPnTS14rSxysEYKEmHVqVcg5zp9nTacAo97lt2rfDPupnlC1PwoTm70Vk7801OKLDLg6_msGDLIy82eikC0O2MlXle0Sv7pzC4SQa4p.jJ.CUy7im3ruakb810Zgc9aBNUT2Y2wP0vDAcDyairLtIHcs8Gzwf1N660WPnD9LI8lsiU6ozlg9j3NU7ue6Q_H3t.jNAZ8mEvPeg4wgQ1VMj7_PF8qNqmLFb9VPctCAE5LIBwKDDXBR9Q_bB6yep263AkR8V0njRJM_uQjtRjVJs3bPwZOYvDQLZg_.jc9atqhOrcCEBuPxO_jjEQXpUl03q7oxUgTl7Ipz6FemBaZPYK2p7qdIw4y875; _hjSession_911455=eyJpZCI6ImFjOTQ4MTU1LTllZWItNDA2OS1hMjg3LWVkNzIzOTIwOWZlMyIsImMiOjE3MjQxNTY4MzkzMDksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _plantrack=%257B%2522id%2522%253A1413280%252C%2522website%2522%253A%2522https%253A%252F%252Fsalla.sa%252Ftestmark%2522%252C%2522logo%2522%253A%2522https%253A%252F%252Fcdn.assets.salla.network%252Fprod%252Fadmin%252Fcp%252Fassets%252Fimages%252Fplaceholder.png%2522%252C%2522about%2522%253A%2522%25D9%2585%25D8%25AA%25D8%25AC%25D8%25B1%2520%25D9%2585%25D8%25AA%25D8%25AE%25D8%25B5%25D8%25B5%2520%25D9%2581%25D9%258A%2520%25D8%25A7%25D9%2584%25D8%25AA%25D8%25B7%25D8%25A8%25D9%258A%25D9%2582%25D8%25A7%25D8%25AA%2520%25D8%25A7%25D9%2584%25D8%25AD%25D8%25B5%25D8%25B1%25D9%258A%25D8%25A9%2520%25D8%25A7%25D9%2584%25D9%2585%25D9%2581%25D9%258A%25D8%25AF%25D8%25A9%2520%25D9%2584%25D9%2583%25D9%2584%2520%25D8%25AC%25D9%258A%25D9%2585%25D8%25B1%25D8%25B2%2520%25D9%2588%25D8%25B5%25D8%25A7%25D8%25AD%25D8%25A8%2520pc%2520%25D9%2588%2520%25D8%25A7%25D9%2584%25D9%2585%25D9%2587%25D8%25AA%25D9%2585%25D9%258A%25D9%2586%2520%25D9%2581%25D9%258A%2520%25D8%25A7%25D9%2584%2520smart%2520home%2522%252C%2522created_at%2522%253A1696482570%252C%2522created_at_in_days%2522%253A319%252C%2522plan%2522%253A%2522plus%2522%252C%2522name%2522%253A%2522testmark%2522%252C%2522created%2522%253A%25222023-10-05T08%253A09%253A30%2522%252C%2522entity%2522%253A%2522person%2522%252C%2522sender_sms_name%2522%253Anull%252C%2522sms_credit%2522%253A0%252C%2522currency%2522%253A%2522SAR%2522%252C%2522store_status%2522%253A%2522idle%2522%252C%2522plan_name%2522%253A%2522plus%2522%252C%2522gender%2522%253Anull%252C%2522social_twitter%2522%253A%2522%2522%252C%2522social_facebook%2522%253A%2522%2522%252C%2522social_maroof%2522%253Anull%252C%2522social_youtube%2522%253A%2522%2522%252C%2522social_whatsapp%2522%253A%2522%2522%252C%2522has_domain%2522%253Afalse%252C%2522has_team%2522%253A0%252C%2522theme_name%2522%253A%25221298199463%2522%252C%2522epayment%2522%253Atrue%252C%2522has_app%2522%253Afalse%252C%2522email%2522%253A%2522dutymastr%2540outlook.com%2522%257D; XSRF-TOKEN=eyJpdiI6InRsK3ZhNk9hR3lRdWJNcDYwYlBHd2c9PSIsInZhbHVlIjoib2p0NGtuTmVRUGpDNVBCREVrUktBUllvK3B6bkNLMzcxRlZGdkFPelpjNURublRCOXFDMjkxV3F6Z2krZnQ3WW56K1hmanlqNDMrK3dEczV2elB1b3lDbFFXdG5wcVNzcVo0cngyeUQ1V0k2c21tdlNlU0Fxbm9HR1laWVVFcDkiLCJtYWMiOiIxNjVlNWY3MGYxZTAwMzAyNjE4N2I3NzgyMWY4MzRkOWQ1OGM2OGMwODE4YmU1NGI3YzhhNmIzMzA2YzM3MGY2IiwidGFnIjoiIn0%3D; _ga_BFVTJX0CL9=GS1.1.1724156839.28.1.1724157941.57.0.0; intercom-session-tsadiujc=REV4MXpCam9IVUVVVndmVnZJcC9STWxJellZVG5leDhINVhyN1R4L0NwZitGRXA3c3JQYk1FRC9wMWtSWVpnRi0tQnN5QkIrSWdaNHRkTURkSi9WQ0g2dz09--fc4097b545619be030c5c6e8d3d738c36360046d',
   'priority': 'u=0, i' ,
   'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
   'sec-ch-ua-mobile':'?0',
   'sec-ch-ua-platform': "Windows",
   'sec-fetch-dest': 'document' ,
   'sec-fetch-mode': 'navigate' ,
   'sec-fetch-site': 'same-origin' ,
   'sec-fetch-user': '?1' ,
   'upgrade-insecure-requests': '1' ,
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}
url = 'https://s.salla.sa/'

req = requests.get(url=url,headers=header)
x = req.text
xx = x.find('<a href="https://s.salla.sa/orders/')
r = x[xx+9:xx+100]
end = r.find('"')
od = x[xx+9:xx+9+end]

op = open('data.csv','r')
u = True
row = op.readlines()
seriel = row[0].split(',')[0].strip()
op.close()
op = open('data.csv','w')
g = row[1:-1]
for i in g:
    op.write(i)
op.close()


req2 = requests.get(od,headers=header)
r2 = req2.text
st = r2.find('order_id = "')
new = r2[st+12:st+40]
end2 = new.find('"')
order_id = new[0:end2]
print(order_id)
url1 = 'https://s.salla.sa/orders/order/status'
data = {
    "_token":"zhc8FdUWHVQ5xWSEjGqOVlztSrcnQTQE0bzndQWD",
    "order_id":order_id,
    "for_change_order_status":"1",
    "order_status":"219467593",
    "note":f'seriel key: {seriel}',
    "options[send_status_sms]":"on",
    "branch_id":"1547995",
    "options[restore_loyalty_buy_from_store_points]":"false",
    "options[refund_loyalty_prize_points]":"false"
}
req2 = requests.post(url=url1,data=data,headers=header)
