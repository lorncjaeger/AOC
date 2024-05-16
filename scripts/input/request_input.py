import requests
import sys
import os

YEAR = sys.argv[1]
DAY = sys.argv[2]
SESSION_COOKIE = '53616c7465645f5fc7a6a1d12384bb89dfb6645b1242a9b06b1e0b62145e4993e63ba3d9506846e7da2d48441488131097848fbdf696ce3b4cf14a9d450e1b75'


def get_aoc_input(year, day, session_cookie):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    cookies = {'session': session_cookie}
    response = requests.get(url, cookies=cookies)

    if response.status_code == 200:
        return response.text.strip()
    else:
        response.raise_for_status()


if __name__ == "__main__":
    try:
        aoc_input = get_aoc_input(YEAR, DAY, SESSION_COOKIE)
        print(aoc_input)
    except Exception as e:
        print(f"An error occurred: {e}")
