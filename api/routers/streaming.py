from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from api.models import StreamInfo, StreamResponse, ViewersResponse
from core.security import verify_token
from services.instagram import InstagramService

router = APIRouter()
security = HTTPBearer()


async def get_current_username(credentials: HTTPAuthorizationCredentials = Depends(security)):
    return verify_token(credentials.credentials)


@router.get("/info", response_model=StreamInfo)
async def get_stream_info(username: str = Depends(get_current_username)):
    try:
        ig_service = InstagramService.get_instance(username)
        if not ig_service:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Instagram session not found. Please login again."
            )

        stream_data = await ig_service.get_stream_info()
        return StreamInfo(**stream_data)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get stream info: {str(e)}"
        )


@router.post("/start", response_model=StreamResponse)
async def start_stream(username: str = Depends(get_current_username)):
    try:
        ig_service = InstagramService.get_instance(username)
        if not ig_service:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Instagram session not found. Please login again."
            )

        result = await ig_service.start_broadcast()
        if result["success"]:
            return StreamResponse(
                status="running",
                message="Live stream started successfully!",
                data=result["data"]
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=result["message"]
            )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to start stream: {str(e)}"
        )


@router.post("/stop", response_model=StreamResponse)
async def stop_stream(username: str = Depends(get_current_username)):
    try:
        ig_service = InstagramService.get_instance(username)
        if not ig_service:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Instagram session not found. Please login again."
            )

        result = await ig_service.stop_broadcast()
        if result["success"]:
            return StreamResponse(
                status="stopped",
                message="Live stream stopped successfully!",
                data=result["data"]
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=result["message"]
            )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to stop stream: {str(e)}"
        )


@router.post("/refresh-key", response_model=StreamResponse)
async def refresh_stream_key(username: str = Depends(get_current_username)):
    try:
        ig_service = InstagramService.get_instance(username)
        if not ig_service:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Instagram session not found. Please login again."
            )

        result = await ig_service.create_broadcast()
        if result["success"]:
            return StreamResponse(
                status="refreshed",
                message="Stream key refreshed successfully!",
                data=result["data"]
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=result["message"]
            )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to refresh stream key: {str(e)}"
        )


@router.get("/viewers", response_model=ViewersResponse)
async def get_viewers(username: str = Depends(get_current_username)):
    try:
        ig_service = InstagramService.get_instance(username)
        if not ig_service:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Instagram session not found. Please login again."
            )

        viewers = await ig_service.get_viewers()
        return ViewersResponse(count=len(viewers), viewers=viewers)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get viewers: {str(e)}"
        )