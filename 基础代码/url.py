import time
i = 0
while True:
    url = 'http://www.toutiao.com/search_content/?offset='+str(i)
    url = url+'&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1'
    print(url)
    i = i + 20
    time.sleep(2)