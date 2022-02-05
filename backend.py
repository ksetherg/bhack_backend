import requests


IPFS_URI = 'http://95.217.3.251:5001/api/v0'


def read_image(path: str) -> bytes:
    """Get image contents from local disk."""
    with open(path, 'rb') as file:
        content = file.read()
    return content


def upload_to_ipfs(name: str, img_content: bytes) -> str:
    """Upload image to IPFS."""
    uri = f'{IPFS_URI}/add'
    files = {
        name: img_content,
    }
    response = requests.post(uri, files=files)
    res = response.json()
    return res['Hash']


def get_from_ipfs_by_hash(hash_id: str) -> bytes:
    """Get image contents from IPFS."""
    uri = f'{IPFS_URI}/cat'
    params = (
        ('arg', hash_id),
    )
    response = requests.post(uri, params=params)
    return response.content


if __name__ == "__main__":
    path = 'logos/uni.png'
    content_local = read_image(path)

    hash_id = upload_to_ipfs(path.replace('/', '-'), content_local)
    content_remote = get_from_ipfs_by_hash(hash_id)

    print('Images match: ', content_local == content_remote)
