import os
from fastapi.responses import JSONResponse
import requests
from starlette.requests import Request
from starlette.routing import Match

from app.core.config import get_settings
from app.core.schemas.base import BaseResponse


def get_matching_route_path(request: Request) -> str:
    for route in request.app.routes:
        match, child_scope = route.matches(request.scope)
        if match == Match.FULL:
            return route.path
    return request.url.path


def get_path_params(request: Request) -> dict:
    for route in request.app.routes:
        match, child_scope = route.matches(request.scope)
        if match == Match.FULL:
            return child_scope["path_params"]
    return {}


def remove_empty_from_dict(d):
    if type(d) is dict:
        return dict((k, remove_empty_from_dict(v)) for k, v in d.items() if v and remove_empty_from_dict(v))
    elif type(d) is list:
        return [remove_empty_from_dict(v) for v in d if v and remove_empty_from_dict(v)]
    else:
        return d


def base_response_to_json_response(model: BaseResponse):
    try:
        status_code = model.status_code
        content = model.dict()

        return JSONResponse(
            status_code=status_code,
            content=remove_empty_from_dict(content)
        )
    except AttributeError:
        return model


def download_file(url: str, save_path: str, session=None):
    if session is None:
        session = requests.Session()

    try:
        response = session.get(url, stream=True)
        response.raise_for_status()

        filename = os.path.basename(url)
        save_path = os.path.join(save_path, filename)

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

        return save_path

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None
