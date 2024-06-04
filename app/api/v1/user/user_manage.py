from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core import security
from app.core.config import settings


router = APIRouter()

@router.post("/login", response_model=schemas.Token)
def login(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests

    Args:
        db (Session): The database session
        form_data (OAuth2PasswordRequestForm): The form data containing the username and password

    Returns:
        dict: A dictionary containing the access token and token type
    """
    # Authenticate the user with the given username and password
    user = crud.user.authenticate(
        db, username=form_data.username, password=form_data.password
    )
    # If the user does not exist, raise an HTTPException
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")
    # If the user is inactive, raise an HTTPException
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    
    # Set the access token expiration time
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    # Create and return the access token
    return {
        "access_token": security.create_access_token(
            user.username, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/login/test-token", response_model=schemas.User)
def test_token(current_user: models.User = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    return current_user

@router.post("/register", response_model=schemas.Msg)
def register(
    register_user: schemas.UserCreate, 
    db: Session = Depends(deps.get_db)
):
    """
    Register a new user.

    Args:
        register_user (schemas.UserCreate): User registration data.
        db (Session, optional): Database session. Defaults to Depends(deps.get_db).

    Returns:
        dict: Response message.
    """

    # Check if user already exists
    user = crud.user.get_by_username(db, username=register_user.username)
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The user already exists")
    
    try:
        # Create user in the database
        user = crud.user.create(db, obj_in=register_user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # Return response message
    return {"msg": "User created", "code": "200"}

    

# @router.post("/password-recovery/{email}", response_model=schemas.Msg)
# def recover_password(email: str, db: Session = Depends(deps.get_db)) -> Any:
#     """
#     Password Recovery
#     """
#     user = crud.user.get_by_email(db, email=email)

#     if not user:
#         raise HTTPException(
#             status_code=404,
#             detail="The user with this username does not exist in the system.",
#         )
#     password_reset_token = generate_password_reset_token(email=email)
#     send_reset_password_email(
#         email_to=user.email, email=email, token=password_reset_token
#     )
#     return {"msg": "Password recovery email sent"}


@router.post("/reset-password", response_model=schemas.Msg)
def reset_password(
    new_password: str,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user)
) -> schemas.Msg:
    """
    Reset password
    """
    
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    
    try:
        # Create user in the database
        crud.user.update(db, db_obj=current_user, obj_in={"password": new_password})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    return {"msg": "Password updated successfully", "code": "200"}
