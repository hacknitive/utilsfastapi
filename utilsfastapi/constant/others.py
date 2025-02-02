from enum import Enum

class EnumOrderBy(str, Enum):
    A = "A"
    D = "D"

class EnumRole(str, Enum):
    PUBLIC = "PUBLIC"
    USER = "USER"
    ADMIN = "ADMIN"


class EnumPermission(Enum):
    ADMIN = (EnumRole.ADMIN, )
    PUBLIC = (EnumRole.PUBLIC, )
    USER = (EnumRole.USER, )
    ADMIN_USER = (EnumRole.ADMIN, EnumRole.USER,)
    ADMIN_PUBLIC_USER = (EnumRole.ADMIN, EnumRole.PUBLIC, EnumRole.USER,)

class EnumDatetimeDuration(str, Enum):
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"
    

RESPONSE_FOR_PUBLIC = {
    "pid": None,
    "role": EnumRole.PUBLIC,
}