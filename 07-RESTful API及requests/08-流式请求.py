import json
import requests
if __name__ == '__main__':

    r = requests.get('http://httpbin.org/stream/20', stream=True)

    # for line in r.iter_lines():
    #     '''
    #     当使用 decode_unicode=True 在 Response.iter_lines() 或 Response.iter_content() 中时，
    #     你需要提供一个回退编码方式，以防服务器没有提供默认回退编码，从而导致错误：
    #     '''
    #     # filter out keep-alive new lines
    #     if line:
    #         decoded_line = line.decode('utf-8')
    #         print(json.loads(decoded_line))
    # for content in r.iter_content(chunk_size=1024):
    for content in r.iter_content(chunk_size=104):
        print(content)
