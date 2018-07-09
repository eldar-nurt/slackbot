from bs4 import BeautifulSoup
import requests
import random
import re

urls = ['http://www.monkeyuser.com/toc/',
        'https://habr.com/',
        'https://pda.anekdot.ru/anekdots/random',
        'https://bash.im/index/{}',
        'https://tech.onliner.by/']


def parse_monkey_user():
    url = urls[0]
    links = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    memes = soup.find_all(class_="small-image")
    for meme in memes:
        links.append('http://www.monkeyuser.com' + meme.attrs["data-src"])

    with open('src/mems.txt', 'w', encoding='utf-8') as result_file:
        for item in links:
            result_file.write('%s\n' % item)


def give_back_mem():
    list_mem = []
    with open('src/mems.txt', 'r') as mems:
        for line in mems:
            list_mem.append(line)
    result = list_mem[random.randint(0, len(list_mem)-1)]
    return result


def parse_popular_habr_posts():
    url = urls[1]
    result = 'Top posts on habr.com: \n'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    posts = soup.find_all(class_="post__title_link")
    for post in posts:
        result = result + (str(posts.index(post)+1) + '. ' + post.text + ':\n - ' + post.attrs['href'] + '\n')
    return result


def parse_random_anekdot():
    url = urls[2]
    result = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    anekdots = soup.find_all(class_='topicbox')
    for item in anekdots:
        item_index = item
        if anekdots.index(item_index) == 5:
            break
        item = str(item).replace('<p class="topicbox">', '')
        item = item.replace('</p>', '')
        item = item.replace('<br/>', ' ')
        result.append(item)
        if anekdots.index(item_index) == 5:
            break
    return result


def parse_random_bash_cit():
    url = urls[3].format(str(random.randint(1, 1380)))
    result = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    citats = soup.find_all(class_='text')
    for item in citats:
        item = str(item).replace('<div class="text">', '')
        item = item.replace('</div>', '')
        item = item.replace('<br/>', '\n')
        result.append(item)
    return result[random.randint(0, len(result)-1)]


def parse_popular_tech_onliner():
    url = urls[4]
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    test = soup.find_all(class_="news-tiles__subtitle")
    for elem in test:
        print(re.sub(r'\s+', ' ', elem.text))
    print(test)


# def main():
#     print(parse_random_anekdot())
#
#
# if __name__ == '__main__':
#     main()
