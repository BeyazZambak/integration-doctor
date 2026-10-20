import httpx

URL = "https://httpbin.org/bytes/50000"


def check(url):
    response = httpx.get(url, timeout=10)

    status = response.status_code
    size = len(response.content)
    seconds = response.elapsed.total_seconds()

    print(f"{status} {size} {seconds:.2f}")


check(URL)