import requests
import email
headers_first = {"Host":"horde.metu.edu.tr","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
                                        "Accept-Encoding":"gzip, deflate",
                                        "Accept-Language":"tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
                                        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                                        "Upgrade-Insecure-Requests":"1",
                                        "Sec-Fetch-Dest":"document",
                                        "Sec-Fetch-Mode":"navigate",
                                        "Sec-Fetch-Site":"same-origin",
                                        "Sec-Fetch-User":"?1",
                                        "Te":"trailers",
                                        "Connection":"close"}
data_dict_real = {"app":"", "login_post":"1", "url":"", "anchor_string":"", "horde_user":"e123456",#Write your username into horde_user part as e123456
                     "horde_pass":"pass", "horde_select_view":"auto", "new_lang":"tr_TR"}#Write your password to horde_pass

first_request = requests.get("https://horde.metu.edu.tr/login.php", headers=headers_first)
headers_second = {"Host":"horde.metu.edu.tr",
                  "Cookie":f"Horde={first_request.cookies.values()[0]}; horde_secret_key={first_request.cookies.values()[1]}",
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
                                        "Content-Type":"application/x-www-form-urlencoded",
                                        "Accept-Encoding":"gzip, deflate",
                                        "Accept-Language":"tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
                                        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                                        "Origin":"https://horde.metu.edu.tr",
                                        "Referer":"https://horde.metu.edu.tr/login.php",
                                        "Upgrade-Insecure-Requests":"1",
                                        "Sec-Fetch-Dest":"document",
                                        "Sec-Fetch-Mode":"navigate",
                                        "Sec-Fetch-Site":"same-origin",
                                        "Sec-Fetch-User":"?1",
                                        "Te":"trailers",
                                        "Connection":"close"}
#print(first_request.cookies.values())

second_request = requests.post("https://horde.metu.edu.tr/login.php", data=data_dict_real, headers=headers_second)

#print(second_request.cookies.values())

updated_cookies = {"Host":"horde.metu.edu.tr",
                  "Cookie":f"Horde={second_request.cookies.values()[0]}; horde_secret_key={first_request.cookies.values()[1]}",
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
                                        "Accept-Encoding":"gzip, deflate",
                                        "Accept-Language":"tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
                                        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                                        "Upgrade-Insecure-Requests":"1",
                                        "Sec-Fetch-Dest":"document",
                                        "Sec-Fetch-Mode":"navigate",
                                        "Sec-Fetch-Site":"same-origin",
                                        "Sec-Fetch-User":"?1",
                                        "Te":"trailers",
                                        "Connection":"close"}
third_request = requests.get("https://horde.metu.edu.tr/imp/dynamic.php?page=mailbox", headers=updated_cookies)
view = third_request.content.decode("utf-8")[25990:26090].split(",")[0].split(":")[1]

#print(str(third_request.content).find("token"))
#10090 is the index of "t" which is the initial letter of token
#We need to get the token from the response of http request in order to use it in the post request to AJAX.
token = str(third_request.content)[10096:10119]
final_headers = {"Host":"horde.metu.edu.tr",
                  "Cookie":f"Horde={second_request.cookies.values()[0]}; horde_secret_key={first_request.cookies.values()[1]}",
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
                                        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                                        "Accept-Encoding":"gzip, deflate",
                                        "Accept-Language":"tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
                                        "X-Requested-With":"XMLHttpRequest",
                                        "X-Prototype-Version":"1.7.3",
                                        "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
                                        "Origin":"https://horde.metu.edu.tr",
                                        "Referer":"https://horde.metu.edu.tr/imp/dynamic.php?page=mailbox",
                                        "Upgrade-Insecure-Requests":"1",
                                        "Sec-Fetch-Dest":"empty",
                                        "Sec-Fetch-Mode":"cors",
                                        "Sec-Fetch-Site":"same-origin",
                                        "Te":"trailers",
                                        "Connection":"close"}
final_data = {"viewport":f"%7B%22view%22%3A%22{view}%22%2C%22initial%22%3A1%2C%22after%22%3A66%2C%22before%22%3A44%2C%22slice%22%3A%221%3A111%22%7D",
              "view":f"{view}", "token":f"{token}"}
final_request = requests.post("https://horde.metu.edu.tr/services/ajax.php/imp/dynamicInit", headers=final_headers, data=final_data)

cacheIDindex = final_request.content.decode("utf-8").find("cacheid")
cacheID = final_request.content.decode("utf-8")[cacheIDindex:cacheIDindex+70].split(",")[0].split(":")[1]
#print(cacheID)


showMessageHeader = {"Host": "horde.metu.edu.tr",
                      "Cookie":f"Horde={second_request.cookies.values()[0]}; horde_secret_key={first_request.cookies.values()[1]}",
                      "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
                                        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                                        "Accept-Encoding":"gzip, deflate",
                                        "Accept-Language":"tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
                                        "X-Requested-With":"XMLHttpRequest",
                                        "X-Prototype-Version":"1.7.3",
                                        "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
                                        "Origin":"https://horde.metu.edu.tr",
                                        "Referer":"https://horde.metu.edu.tr/imp/dynamic.php?page=mailbox",
                                        "Upgrade-Insecure-Requests":"1",
                                        "Sec-Fetch-Dest":"empty",
                                        "Sec-Fetch-Mode":"cors",
                                        "Sec-Fetch-Site":"same-origin",
                                        "Te":"trailers",
                                        "Connection":"close"}


#VTM4MjEsVjE1OTg2MDg4MzQsSDMxNw%3D%3D%7C3%7C1%7C1%7CD91

totalMsgNumber = int(final_request.content.decode("utf-8").split(",")[4].split(":")[1])+20
for x in range(15):
  showMessageData = {"viewport":f"%7B%22view%22%3A%22{view}%22%2C%22cacheid%22%3A%22{cacheID}%22%2C%22slice%22%3A%221%3A111%22%2C%22cache%22%3A%22{totalMsgNumber-110}%3A{totalMsgNumber}%22%7D",
                    "view":f"{view}", "token":f"{token}","preview":"1","buid":f"{totalMsgNumber-x}"}
  showMessageResponse = requests.post("https://horde.metu.edu.tr/services/ajax.php/imp/showMessage",headers=showMessageHeader,data=showMessageData)
  messageStr = showMessageResponse.content.decode("utf-8")
  message = email.message_from_string(messageStr)
  msgKeys = message.raw_items()
  tempMsg = next(msgKeys)[1]
  startIndex = tempMsg.find("subject")-1
  subject = tempMsg[startIndex:startIndex+300].split(":")[1]
  finalIndex = subject.rfind(",")
  print(f"Subject --> {subject[:finalIndex]}")