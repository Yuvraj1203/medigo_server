
from enum import Enum

class MedicineType(str, Enum):
    TABLET = "tablet"
    SYRUP = "syrup"
    INJECTION = "injection"
    CAPSULE = "capsule"
    DROPS = "drops"
    OINTMENT = "ointment"
    POWDER = "powder"
