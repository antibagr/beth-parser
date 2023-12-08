import datetime as dt
import functools

import pydantic


class BaseModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        validate_assignment=True,
        json_encoders={
            dt.datetime: functools.partial(dt.datetime.strftime, format="%Y-%m-%d %H:%M:%S")
        },
    )
