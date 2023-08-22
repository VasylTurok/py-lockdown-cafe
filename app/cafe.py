import datetime
from app.errors import (NotVaccinatedError,
                        NotWearingMaskError, OutdatedVaccineError)


class Cafe:

    def __init__(self, name: str) -> None:

        self.name = name

    def visit_cafe(self, visitor: dict) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError

        current_date = datetime.date.today()
        if visitor["vaccine"]["expiration_date"] < current_date:
            raise OutdatedVaccineError

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"