from fastapi import APIRouter, Body, HTTPException, status
from models.event import Event
from typing import List

event_router = APIRouter(
    tags=['Event']
)

#our test local datastorage
events = []


#here are the routes that we use to retrieve event
@event_router.get('/', response_model=List[Event])
async def retrieve_all_event()->List[Event]:
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int)->Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Event with suplied id was not found")


#here are routes to create an event
@event_router.post("/new_event")
async def create_event(body: Event=Body(...))->dict:
    events.append(body)
    return{
        "message":"Event created successfully"
    }
#routes to delete an event
@event_router.delete("/{id}")
async def delete_event(id:int)->dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {
                "message": "Event deleted successfully"
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="event with suplied id was not found to be deleted")

@event_router.delete("/")
async def delete_all_events()-> dict:
    events.clear()
    return {
        "message":"Events deleted successfully"
    } 