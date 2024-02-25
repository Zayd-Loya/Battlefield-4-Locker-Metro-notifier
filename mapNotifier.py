from bs4 import BeautifulSoup
import requests
from plyer import notification
import time


def server_list():
    with open('servers.txt', 'r') as file:
        urls = file.read().splitlines()

    return urls


def map_checker(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        serverName = url.split('/')[-2].split('-')[0]
        mapName = soup.find(id='server-page-gamemode').find('strong').text.lower().strip()
        playerCount = int(soup.find(id='server-page-info').find('h5').text.strip()[:2:].strip())

        if mapName == 'operation locker' and playerCount >= 32:
            notification.notify(
                title='Locker Alert',
                message=f'Operation Locker is currently being played on {serverName} with {playerCount} players.',
                app_name='Map Notifier',
                app_icon='mp_prison.ico'
            )

        if mapName == 'operation metro 2014' and playerCount >= 32:
            notification.notify(
                title='Metro Alert',
                message=f'Operation Metro is currently being played on {serverName} with {playerCount} players.',
                app_name='Map Notifier',
                app_icon='xp0_metro.ico'
            )

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    while True:
        for server in server_list():
            map_checker(server)
        time.sleep(300)
