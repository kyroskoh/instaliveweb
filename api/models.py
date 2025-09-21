from pydantic import BaseModel
from typing import Optional, Dict, Any


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str


class UserInfo(BaseModel):
    username: str
    is_authenticated: bool


class StreamInfo(BaseModel):
    status: str
    stream_url: Optional[str] = None
    stream_key: Optional[str] = None
    broadcast_id: Optional[str] = None


class StreamResponse(BaseModel):
    status: str
    message: str
    data: Optional[Dict[str, Any]] = None


class ViewersResponse(BaseModel):
    count: int
    viewers: list = []