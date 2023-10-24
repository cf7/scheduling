from typing import List
from entities.create.Schedule.CreateSchedule import CreateSchedule
from entities.update.Schedule.UpdateSchedule import UpdateSchedule
from entities.models.Schedule.Schedule import Schedule
from persistence.SchedulesRepository.command import ScheduleCommand
from persistence.SchedulesRepository.query import ScheduleQuery

"""
Domain Driven Design with Repository Pattern

Repository layer is usually considered closer
to the Domain (i.e. domain being the business logic / concepts / entities)
Respoitories implement DAO's, but no the other way around

Repositories are classes or components that encapsulate the logic 
required to access data sources.

So Repository layer can also combine data from DAO layer to make
more complex data entities (known as "Aggregates") from simpler/faster queries


Quick Note on Aggregates:
- aggregates are collections of 1 or more entities
- they are meant to be queried or mutated together as a whole
- this collection is defined by a consistency boundary (transaction boundary)
- this ensures transactions operate on the collection of entities
as a whole so state consistency is maintained amongst the entities
- each aggregate has a root entity (called the "Aggregate Root"), which is
usually a parent entity that contains the other entities in the collection


DAO layer is usually considered closer
to the data persistence layer (DB)
(it doesn't necessarily have to be 1-to-1 per table,
especially since you'd want to be able to swap out
DB access layers as well)

Repository layer lives within the Persistance layer

Persistence layer is responsible for handling interaction between
the api and the data storage system.

Persistance layer
    --> Repositories
        --> DAO / ORM
"""


class SchedulesRepository:
    def __init__(self):
        ...

    # provide and use DB connection here

    # build aggregates here

    @staticmethod
    def get_schedules(schedule_ids: List[int]) -> List[Schedule]:
        # mock schedule entity
        return ScheduleQuery.get_schedules(schedule_ids)

    @staticmethod
    def create_schedules(create_schedules: List[CreateSchedule]) -> List[Schedule]:
        return ScheduleCommand.create_schedules(create_schedules)

    @staticmethod
    def update_schedule(update_schedule: UpdateSchedule) -> Schedule:
        return None

    # Schedule(
    #         id=1,
    #         name="Updated Schedule",
    #         timezone="America/Los_Angeles",
    #         url="https://example.com/schedule?id=1",
    #     )


"""
Design Decision:

Building Complex Entities from the Data

a) use SQL and DB to optimize searching
pros:
- more performant since it leverages DB's built-in optimization
- reduces data transfer (only returns data that is needed, less data over the network)
cons:
- tight coupling with DB implementation
- complicated SQL difficult to maintain and make changes to


b) have Repository layer build complex entities from
the data returned from more numerous, simpler queries
pros:
- decouples DAO layer from DB implementation
- modularity makes it easier to maintain and change later
- easier to unit test
cons:
- less performant (but not by much if data is lean)
- need to retrieve more data than is necessary

For now, going with Option B because being able to swap out
Database software is more important than performance, especially
since the data requirements for this app are going to be very lean.
"""

"""
Design Decision
- using CQRS Pattern (Command-Query Responsibility Separation) to structure
the DAO layer so that if I want to leverage the Repository layer to handle Aggregates,
I can do so -- while leaving open the possibility of bypassing the Repository layer
(in case I don't need aggregates) so that I can still grab Data directly from the DB

Example:

- my command paths in the API make mutations to data in the DB, but those mutations
need to be performed on a collection of entities (an aggregate) together to ensure consistency
- my query paths, however, merely read from the DB, so they don't need to perform operations
on collections of entities, they only need to pull data directly as-is -- so they call
pull straight from the DB using the DAO layer in that case
"""


"""
Unit of Work pattern
- design pattern used for managing database transactions
and changes to entities within the DAO layer
- this layer ensures that actions done with the Database
are done as transactions, and that the operations happen in order
even when multiple different repositories are trying to connect
to the Database

"""


"""

Design Decision: use Clean Architecture
- replaces service layer with a Use Cases layer
- allows you to define the repository layer inside the domain layer
- which provides affordance of constraining domains to only be used
by Use Case logic (business logic) in very specific ways (and disallowing all others)
- basically you don't have to initialize an entire repository and all its methods
- you can just implement/include the repository methods that the Use Case needs
- downside is you duplicate code (repository methods) across Use Cases, although
there are some clever ways to mitigate this
"""
