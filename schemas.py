import re
from datetime import date


from pydantic import BaseModel, validator


class BookingDates(BaseModel):
    """Schema bookingdates."""

    checkin: date
    checkout: date


class Booking(BaseModel):
    """Schema booking."""

    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str

    @validator('firstname')
    def first_name(cls, v: str) -> str:
        """Валидация firstname."""
        match = re.match(r'^[A-Z]\w*[^\s\d]{0,}', v)
        if match is None:
            raise ValueError('Некорректное имя')
        return v


class CreateBookingResponseSchema(BaseModel):
    """Schema create booking response."""

    bookingid: int
    booking: Booking


class CreateTokenResponseSchema(BaseModel):
    """Schema create token response."""

    token: str
