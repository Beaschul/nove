from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name : str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)

    def show(self) -> None:
        status = "Operational" if self.is_operational else "Offline"
        print(
            "Valid station created:\n"
            f"ID: {self.station_id}\n"
            f"Name: {self.name}\n"
            f"Crew: {self.crew_size} people\n"
            f"Power: {self.power_level}%\n"
            f"Oxygen: {self.oxygen_level}%\n"
            f"Status: {status}\n"
            f"{f'Notes: {self.notes}' if self.notes else ''}"
        )

def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        space = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="1998-03-23T06:35:00",
            is_operational=True,
            )
        space.show()
    except ValidationError as e:
        print(f"Unexpected validation error:\n{e.errors()[0]['msg']}")

    print("========================================")
    
    try:
        invalid_space = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="1998-03-23T06:35:00",
            is_operational=True,
            )
        invalid_space.show()
    except ValidationError as e:
            print(f"Expected validation error:\n{e.errors()[0]['msg']}")

if __name__ == "__main__":
    main()
