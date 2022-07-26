from typing import Optional

import nvdlib

import fastapi
from fastapi import Depends


from models.location import Location

router = fastapi.APIRouter()


@router.get('/api/cve/{cve}')
def ceevdetails(cvs: str):

    cvenumber = cvs
    r = nvdlib.getCVE(cvenumber)
    v3severity = r.v3severity
    v3score = str(r.v3score)
    cvedescription = r.cve.description.description_data[0].value
    return cvenumber + "  " + "v3severity:" + v3severity + " " + "v3score:"+v3score + cvedescription

    return v3score


@router.get('/api/weather/{city}')
def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    # return f"{loc.city} in {units}"
    return f"{loc.city}, {loc.state}. {loc.country} in {units}"

