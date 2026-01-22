from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# =========================
# MODELO DE DADOS
# =========================
class LoginRequest(BaseModel):
    login: str
    password: str


class LoginResponse(BaseModel):
    message: str


# =========================
# CREDENCIAIS TEMPORÁRIAS
# (APENAS PARA USO LOCAL)
# =========================
VALID_LOGIN = "admin"
VALID_PASSWORD = "admin123"


# =========================
# ENDPOINT DE LOGIN
# =========================
@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    if data.login != VALID_LOGIN or data.password != VALID_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login ou senha inválidos"
        )

    return {
        "message": "Login realizado com sucesso"
    }