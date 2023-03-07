from datetime import date

from pydantic import BaseModel


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


class CreateBookingResponseSchema(BaseModel):
    """Schema create booking response."""

    bookingid: int
    booking: BaseModel
