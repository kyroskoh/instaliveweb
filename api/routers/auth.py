from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import timedelta
from api.models import LoginRequest, LoginResponse, UserInfo
from core.security import create_access_token, verify_token
from core.config import settings
from services.instagram import InstagramService

router = APIRouter()
security = HTTPBearer()


@router.post("/login", response_model=LoginResponse)
async def login(login_data: LoginRequest):
    try:
        # Verify Instagram credentials
        ig_service = InstagramService(login_data.username, login_data.password)
        login_success = await ig_service.login()

        if not login_success:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Instagram credentials"
            )

        # Create JWT token
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": login_data.username}, expires_delta=access_token_expires
        )

        return LoginResponse(access_token=access_token, token_type="bearer")

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Login failed: {str(e)}"
        )


@router.get("/me", response_model=UserInfo)
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    username = verify_token(credentials.credentials)
    return UserInfo(username=username, is_authenticated=True)


@router.post("/logout")
async def logout():
    return {"message": "Successfully logged out"}