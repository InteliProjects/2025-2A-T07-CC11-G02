from fastapi import APIRouter, HTTPException, Query

from ..repositories.users_repo import (
    UserCreate,
    UserOut,
    UserUpdate,
    create_user,
    delete_user,
    get_user_by_external_id,
    get_user_by_id,
    list_users,
    update_user,
)

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserOut)
def create_user_endpoint(payload: UserCreate):
    try:
        return create_user(payload)
    except Exception as e:
        # Common causes: unique constraint violations
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{user_id}", response_model=UserOut)
def get_user_endpoint(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/by-external/{external_id}", response_model=UserOut)
def get_user_by_external_endpoint(external_id: str):
    user = get_user_by_external_id(external_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=list[UserOut])
def list_users_endpoint(
    limit: int = Query(50, ge=1, le=200), offset: int = Query(0, ge=0)
):
    return list_users(limit=limit, offset=offset)


@router.patch("/{user_id}", response_model=UserOut)
def update_user_endpoint(user_id: int, payload: UserUpdate):
    user = update_user(user_id, payload)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}")
def delete_user_endpoint(user_id: int):
    ok = delete_user(user_id)
    if not ok:
        raise HTTPException(status_code=404, detail="User not found")
    return {"deleted": True}
