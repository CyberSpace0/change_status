import requests

header = {
   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' ,
   'accept-language': 'ar,en-US;q=0.9,en;q=0.8' ,
   'cookie': '_gcl_au=1.1.1590758377.1722584574; _hjSessionUser_911455=eyJpZCI6ImEyMWFiMGYyLTkzYjktNWIyYS04MmRiLTI1Yjc3YzdiMWVjYSIsImNyZWF0ZWQiOjE3MjI1ODQ1NzU5NTYsImV4aXN0aW5nIjp0cnVlfQ==; intercom-device-id-tsadiujc=5fd57dc5-a113-478e-8b09-c7cce2c0c624; __ssid=52540da27f22ac6289f4825a26393c0; _ga=GA1.1.92343697.1722584575; _hjSessionUser_3004400=eyJpZCI6ImM1ZDg1ZjdmLWFjY2ItNTQzOC1iNmUzLTgyZDg5MjM2ODQxNSIsImNyZWF0ZWQiOjE3MjQwOTQ0MjgwMzAsImV4aXN0aW5nIjpmYWxzZX0=; utm_source=eyJpdiI6Im53ZFNXT2tNMG9aR3RUekI3YngwTHc9PSIsInZhbHVlIjoiK01jUHZPR2MvUko2WHFJa2xTTVhadExEbTJZY0NBbFFvT24yQkRoWFgxQzNMd1hFWkN6UVl3S3d6WXZBbTBrSCIsIm1hYyI6IjYxZDk4ZWQzZDZjNmJhM2VmNjRmOWMwOWY0MWIxM2Y0YzM3ZTU2NDIwYjFlYjZhMDg0ZGMwNWMyZjhkZTcyNjUiLCJ0YWciOiIifQ%3D%3D; utm_campaign=eyJpdiI6IlAwVncxVEYrRjByamREbVF3ZlYxRWc9PSIsInZhbHVlIjoiNko3ZUprRzNuTGsyTC9URTB3TC9wVXJJTmxmL0N6MG0yZlVpZTVkNlZaVXFIUjVuUW5hTGk2T1dLV3RwM095dCIsIm1hYyI6ImY2YTE1NDE5NWI3ZTZiZmQ0ZjFmM2EwYWM2NjRhN2E3YTI5NmQ4M2Y5YTE2M2Y1Y2Y1MDQwZmU4MDIxZTUyNzQiLCJ0YWciOiIifQ%3D%3D; utm_medium=eyJpdiI6IlVYSHE3SHRGVjMvYVNWeHlyWWo0SXc9PSIsInZhbHVlIjoiOXpqRG02Zi8yM2NqWWtaYm9abkIrWFgvYW93TmdoN0M3VjZUN2ZRWmVjQi9TSFFsUzhrcXRxSUNMMTFkQXVxNXlvK3lJeGFLa0tndXk5VGxGWmNaQVE9PSIsIm1hYyI6ImY4NDkwYjc2MWYxMWE0NDcwODdjNjkyZjgxMTJjYTdjNzU5ODk4MDExNWUwMzdlOWQ5MTM0MTljZDdmYTNiNjMiLCJ0YWciOiIifQ%3D%3D; utm_referer=eyJpdiI6IllTWURUMXNFOUpYMXh2enE5MS9WVVE9PSIsInZhbHVlIjoiNkFHa3NhbXYzSVFEZGJCNWQrUVlCUEp3K3B2Z3NUZXZwNEQ1MVh1UUpnTnJJazdRSWFndis2Q3hMUzQ1a1RkRXVrSFE5a0NmbDFUc1ovakxqYVZoUlE9PSIsIm1hYyI6ImQzYjYyOWY1ZTU0NmNkN2RjNjFhMGQ3YTFjNzhmMDdlMzljMTU1ZWY3ZjY3OTA0ZTZlM2RiMDUzMWEzYTlkNWUiLCJ0YWciOiIifQ%3D%3D; _ga_ZY5GVCRQKE=GS1.1.1724094428.1.1.1724094537.0.0.0; __cflb=02DiuHSSY6uJRHtqYzYdDzcTiErkrZF9umJGr1R3BMHWt; homepage.run-once=1; cf_clearance=tJUWxdAQsKDS2FwkSEiA1PPve6JOw39w3pD4YLFg6TQ-1724177891-1.2.1.1-.gnrLX058HXiSZhR7VZNURK7zU.U2w7V5_O0Zhzr4WprqRrBX2pP3lEwGDw2_8vJWcAcZxltnVlE_uOAMUYidrjlSUPKmTYJ_6wk.OCkkjE0iMJnlnhteeuNV5EbOa0TkBCTolEMq.pTDTwObcoF39rSnfmvsHmrhmAfc2ldDiHhVmfEEWNxxjLpGwu7Ztlw65U6QNWM4pGr4EFZ98oHKy4nw6ayhtXk3ebJ8CSe_3tRxrj.ADdNGE7YN5HlEJ2toyfyb73tr5UZrKmwN2yrcTV3uFFbcB.4hA4YOHAhHOD5hFrx.f_tdVuVxu_llQivECF6sR6L2G6u.Fhm6Ur_PSj2xnTRfyBrkfimfzWAof4NXHQOfUi_Gn457tbXRSVhGsTseSD3HMh9mDkPFoFKmLr0iwnFX0ATIyCYSb92ui5UNzxcCDRRxyj58fdollO8; _plantrack=%257B%2522id%2522%253A1413280%252C%2522website%2522%253A%2522https%253A%252F%252Fsalla.sa%252Ftestmark%2522%252C%2522logo%2522%253A%2522https%253A%252F%252Fcdn.salla.sa%252FRAAwRv%252FO2zNzKSGLKF3a96dE3yKgmkzOMSjpPhR4DGnDals.jpg%2522%252C%2522about%2522%253A%2522%25D9%2585%25D8%25AA%25D8%25AC%25D8%25B1%2520%25D9%2585%25D8%25AA%25D8%25AE%25D8%25B5%25D8%25B5%2520%25D9%2581%25D9%258A%2520%25D8%25A7%25D9%2584%25D8%25AA%25D8%25B7%25D8%25A8%25D9%258A%25D9%2582%25D8%25A7%25D8%25AA%2520%25D8%25A7%25D9%2584%25D8%25AD%25D8%25B5%25D8%25B1%25D9%258A%25D8%25A9%2520%25D8%25A7%25D9%2584%25D9%2585%25D9%2581%25D9%258A%25D8%25AF%25D8%25A9%2520%25D9%2584%25D9%2583%25D9%2584%2520%25D8%25AC%25D9%258A%25D9%2585%25D8%25B1%25D8%25B2%2520%25D9%2588%25D8%25B5%25D8%25A7%25D8%25AD%25D8%25A8%2520pc%2520%25D9%2588%2520%25D8%25A7%25D9%2584%25D9%2585%25D9%2587%25D8%25AA%25D9%2585%25D9%258A%25D9%2586%2520%25D9%2581%25D9%258A%2520%25D8%25A7%25D9%2584%2520smart%2520home%2522%252C%2522created_at%2522%253A1696482570%252C%2522created_at_in_days%2522%253A320%252C%2522plan%2522%253A%2522plus%2522%252C%2522name%2522%253A%2522smart%2520pc%2522%252C%2522created%2522%253A%25222023-10-05T08%253A09%253A30%2522%252C%2522entity%2522%253A%2522person%2522%252C%2522sender_sms_name%2522%253Anull%252C%2522sms_credit%2522%253A0%252C%2522currency%2522%253A%2522SAR%2522%252C%2522store_status%2522%253A%2522active%2522%252C%2522plan_name%2522%253A%2522plus%2522%252C%2522gender%2522%253Anull%252C%2522social_twitter%2522%253A%2522%2522%252C%2522social_facebook%2522%253A%2522%2522%252C%2522social_maroof%2522%253Anull%252C%2522social_youtube%2522%253A%2522%2522%252C%2522social_whatsapp%2522%253A%2522%252B966542466332%2522%252C%2522has_domain%2522%253Afalse%252C%2522has_team%2522%253A0%252C%2522theme_name%2522%253A%25221298199463%2522%252C%2522epayment%2522%253Atrue%252C%2522has_app%2522%253Afalse%252C%2522email%2522%253A%2522dutymastr%2540outlook.com%2522%257D; _hjSession_911455=eyJpZCI6IjcyMGJhYmY0LTVmY2YtNDJjOS1iY2IwLTdjMGQzZTRkODczZCIsImMiOjE3MjQxNzc4ODk3NjgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _hjHasCachedUserAttributes=true; s_domains_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Muc2FsbGEuc2EvbG9naW4iLCJpYXQiOjE3MjQxNzk5NzgsImV4cCI6MTcyNDIwMTU3OCwibmJmIjoxNzI0MTc5OTc4LCJqdGkiOiJaQWxUT2RjVTZycGJINGxtIiwic3ViIjozNDk4ODIwLCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3Iiwic291cmNlIjoiYXBpLWRhc2hib2FyZCIsInJ0aSI6MH0.lTTguVKB3Ot8_SOj2ZsHOXUV1Fx8VYr_M0TYOpA-miE; __saaid=drAdnGnCMbBVmOpufLNBYuyCxxQmR47c909YwiTD; remember_user_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IlYvOVRISmNURDNKK21WbXl5K1A4RXc9PSIsInZhbHVlIjoiV1FGY2dudmRjUm9DanI1cjBEbElUN1d6bnYveXZwS2NZSXk0c2c2TGV0Yk5OOExUcG54ODRaNnhRZzFQUTg3UCtZSkNKRkEvZWZrZzF1cWtLL0R0RkVobFQxV240a0xDR0ZSSGlMeFo5SkNHR2VZZXMzTXMxdEdPZzAvZDJjRW1rdVhnZ0xZSytEb0xxajBzNVFOM0gxejc0elpwUlNSdEJKTkp0bVA0enluWnNRcVd4eTMzNDVESk83WXVEUTlnTUtGcFlFZzlUU2hDVDE2SklRNlBwWHdnWVdGMzZXK1VYUEFrcUJxOXJaaz0iLCJtYWMiOiI3YjM5ZGYyZjkzODM1Nzk1NDUyMjU5NTFjY2U1ZWJmYzQwNWFmZTQyNTAyYjYzNWFkNzk4ODVmNjhmNmNmM2MyIiwidGFnIjoiIn0%3D; intercom-session-tsadiujc=aXNTMm91bmtUUWdIeDMrWEZ6eXBvbUlXbjZSMkdDMWhVUDNzUEFBRlNmMXNucXVwV1NxN3p3a2ZhUkxFb3BVdy0tRlMxNzJmRTV1end0bUJzblNPNE5iZz09--55aace8cfe94c5f10cfff4a875632dad7cf2ac06; _ga_BFVTJX0CL9=GS1.1.1724177886.30.1.1724180017.60.0.0; XSRF-TOKEN=eyJpdiI6IlJ5NG9oS0cyTnVzaGFUd2JrelZGTFE9PSIsInZhbHVlIjoiQjVrMFBRKy9ZalA0K0lDUE5WOWIwbUw4RTJ3aHhQanJpcTN4WU9lK3M2Q2xVSTcwbExEZGVsNVdyOS82U2NLWUtJUjEyTVBaalF2YVFOVVo5VFRWUWpOcVBqcGlyM0RrTnlzcWg0NDBJM0hLaXJyd2FGOEx0Z3JpeGVJU1FNczAiLCJtYWMiOiJlYTlmOGNkZGNkYTk3MmZjNzZjY2U0ZTc5Y2I3OTg1NTIzN2FhMzU4MWU5Zjk3MTBiZGI4YmIyM2FmYzJiMzBkIiwidGFnIjoiIn0%3D',
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
