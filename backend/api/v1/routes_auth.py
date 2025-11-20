from fastapi import APIRouter

from ...schemas.auth import UserCreate, UserLogin, UserRead, Token

router = APIRouter()


@router.post("/register", response_model=UserRead)
async def register_user(payload: UserCreate) -> UserRead:
    """Регистрация пользователя (пока заглушка без БД и реального хранилища)."""
    return UserRead(id=1, email=payload.email, full_name=payload.full_name, role="user")


@router.post("/login", response_model=Token)
async def login(payload: UserLogin) -> Token:
    """Логин пользователя и выдача access token (заглушка)."""
    return Token(access_token="stub-token")


@router.post("/logout")
async def logout() -> dict:
    """Логаут пользователя (заглушка)."""
    return {"success": True}


@router.get("/me", response_model=UserRead)
async def get_current_user() -> UserRead:
    """Текущий пользователь (заглушка)."""
    return UserRead(id=1, email="demo@example.com", full_name="Demo User", role="admin")
