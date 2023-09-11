import requests
import sys


PROTOCOL = "http"


def main():
    if len(sys.argv) != 2:
        sys.exit("You must provide one argument, the site you want to visit")

    origin_url = sys.argv[1]
    if "://" not in origin_url:
        origin_url = PROTOCOL + "://" + origin_url

    url = origin_url

    while True:
        response = requests.get(url)
        break

if __name__ == "__main__":
    main()