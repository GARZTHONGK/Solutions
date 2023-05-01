from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract

import plusbus_data as pbd
import plusbus_sql as pbsql


def booked_journey(booking, date_):
    with Session(pbsql.engine) as session:
        records = session.scalars(select(pbd.Bookings).where(pbd.Bookings.id == booking.id).where(extract('day', pbd.Bookings.date) == date_.day).where(extract('month', pbd.Bookings.date) == date_.month).where(extract('year', pbd.Bookings.date) == date_.year))
        capacity = 0
        for record in records:
            capacity += pbsql.get_record(pbd.Bookings, record.customer_id).capacity
        return capacity


def capacity_available(booking, date_):
    booked = booked_journey(booking, date_)
    return booking.max_capacity >= booked


def capacity_remaining(journey_id):
    with Session(pbsql.engine) as session:
        records = session.scalars(select(pbd.Bookings).where(pbd.Bookings.journey_id == journey_id))
        capacity = 0
        for record in records:
            capacity += record.capacity
        return capacity
