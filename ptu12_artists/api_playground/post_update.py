# post_update newuserhere

import http.client
import json
from pprint import pprint

conn = http.client.HTTPConnection("localhost", 8000)

headers_list = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
#  "Authorization": "Basic bmV3dXNlcmhlcmU6bWFub25hdWphc3Bhc3MxMjM=",
 "Content-Type": "multipart/form-data; boundary=kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A" 
}

payload = "--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"score\"\r\n\r\n3\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\nBandom parasyti su Thunder Client ir newuserhere autherizacija. Pridesiu PUT per Thunder\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A\r\nContent-Disposition: form-data; name=\"song\"\r\n\r\n1\r\n--kljmyvW1ndjXaOEAg4vPm6RBUqO6MC5A--\r\n"

conn.request("PUT", "/6/", payload, headers_list)
response = conn.getresponse()
result_string = response.read()

# pprint(result_string.decode("utf-8"))
result_data = json.loads(result_string)
print(result_data)