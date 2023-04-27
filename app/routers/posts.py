from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import func


from .. import models, schemas,oauth2
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/", response_model=List[schemas.PostOut])
def get_post(db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional [str]=""):
    #mycursor.execute("SELECT * FROM post")
    ##if not result:
    #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Posts found.")
    #return {"data": result}
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts
   



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(title_content: schemas.PostCreate, db: Session = Depends(get_db),
                 user_id: int = Depends(oauth2.get_current_user)):
    #sql = """INSERT INTO post (title, content, publish) VALUES (%s, %s, %);"""
    #mycursor.execute(sql, (title_content.title, title_content.content, title_content.publisher))
    #mydb.commit()
    #return {"message": "New Post Inserted sucessfully"}

    new_post = models.Post(owner_id=user_id.id, **title_content.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    id = id
    #mycursor.execute(f"SELECT * FROM post WHERE id={id}")
    #post = mycursor.fetchone()
    
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found.")

    return post
   

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, post: schemas.Post, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    id = id
    #sql = "UPDATE post SET title = %s, content = %s WHERE id = %s"
    #val = (post.title, post.content, str(id))
    #mycursor.execute(sql, val)
    #mydb.commit()
    #mycursor.execute(f"SELECT * FROM post WHERE id = {id}")
    #obj = mycursor.fetchone()
    #return obj
    posts_query = db.query(models.Post).filter(models.Post.id == id)
    posts = posts_query.first()
    if posts == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found.")
    if posts.owner_id != user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform the requested action.")
    posts_query.update(post.dict())
    db.commit()
    return posts

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    #sql = f"DELETE FROM post WHERE id={id}"
    #mycursor.execute(sql)
    #mydb.commit()
    #print(mycursor.rowcount, "record(s) deleted")
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found.")
    if post.owner_id != user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform the requested action.")
    post_query.delete()
    db.commit()