from fastapi import FastAPI, File, UploadFile, Path, Response
from fastapi.responses import HTMLResponse
import io

from ipfs_api import upload_to_ipfs, get_from_ipfs_by_hash


app = FastAPI()


# @app.post("/files/")
# async def create_files(
#     files: list[bytes] = File(..., description="Multiple files as bytes")
# ):
#     return {"hashes": [upload_to_ipfs(file.filename, file) for file in files]}



@app.post("/uploadfile/")
async def create_upload_files(
    file: UploadFile = File(..., description="File to Upload")
):
    return {"hash": upload_to_ipfs(file.filename, file.file)}


@app.get("/getfile/{hash}")
async def get_file_by_hash(
        hash: str = Path(..., title="Item hash, as in IPFS"),
):
    file_content = get_from_ipfs_by_hash(hash)
    return Response(content=file_content, media_type="image/png")


@app.get("/")
async def main():
    content = """
        <body>
        <!-- <form action="/files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form> -->
        <form action="/uploadfile/" enctype="multipart/form-data" method="post">
        <input name="file" type="file">
        <input type="submit">
        </form>
        </body>
    """
    return HTMLResponse(content=content)

# @app.get("/show/{hash}")
# async def main(
#         hash: str = Path(..., title="Item hash, as in IPFS"),
# ):
#     content = """
#         <body>
#         <form action="/uploadfile/" enctype="multipart/form-data" method="post">
#         <input name="file" type="file">
#         <input type="submit">
#         </form>
#         </body>
#     """
#     return HTMLResponse(content=content)
