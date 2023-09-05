from fastapi import APIRouter,Request, HTTPException, status, Depends
from typing import List
from sqlalchemy.orm import Session
from models.event import Event,EventUpdate
from database.connection import get_session


event_router = APIRouter(tags=['Event'])

@event_router.post("/new")
async def create_event(new_event: Event, session: Session = Depends(get_session))->dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {
        "message":"Event created successfully"
    }

@event_router.get("/", response_model= list[Event])
async def retrieve_all_events(session=Depends(get_session))->List[Event]:
    #statement = select(Event)
    #events = session.exec(statement).all()
    event = session.query(Event).all()
    return event


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session))->Event:
    event = session.get(Event,id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Event with supplied ID does not exit'
    )


@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session = Depends(get_session))->Event:
    event = session.get(Event,id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Event with supplied ID was not found'
    )


@event_router.delete("/delete/{id}")
async def delete_event(id: int, session = Depends(get_session))-> dict:
    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit()
        return{
            "message":"Event deleted sucessfully"
        }
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Event has already been deleted'
    )