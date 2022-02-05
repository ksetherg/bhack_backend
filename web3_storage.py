import requests
from ipfs_api import read_image


WEB3_STORAGE_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDg3NjFlMzQ3MmQ0NjM2OGIzQ0E4NTdmMWE0ZjI2NjAzOTU4N2VhNDMiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NDQwNzYyNDY5ODcsIm5hbWUiOiJ0ZXN0aW5nX2FwaSJ9.eyXWtVfvqz4wr81Dx2j2WPPhRCLKj5oZo6AzW2dUt3U'
HEADERS = {'Authorization': f'Bearer {WEB3_STORAGE_TOKEN}'}
URI_BASE = 'https://api.web3.storage'


def upload_to_web3_storage(name: str, img_content: bytes) -> str:
    """Upload image to Web3 Storage."""
    uri = f'{URI_BASE}/upload'
    data = {
        name: img_content,
    }
    response = requests.post(uri, headers=HEADERS, data=data)
    res = response.json()
    return res


def get_from_web3_storage_by_cid(cid: str) -> bytes:
    """Get image contents from Web3 Storage."""
    uri = f'{URI_BASE}/car/{cid}'
    response = requests.get(uri, headers=HEADERS)
    return response.content


if __name__ == "__main__":
    path = 'logos/uni.png'
    content_local = read_image(path)

    cid = upload_to_web3_storage(path.replace('/', '-'), content_local)
    content_remote = get_from_web3_storage_by_cid(cid['cid'])

    print('Images match: ', content_local == content_remote)
