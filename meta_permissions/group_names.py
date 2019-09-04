from edc_permissions.constants import (
    ADMINISTRATION,
    EVERYONE,
    CLINIC,
    PII,
    LAB,
    PII_VIEW,
)

RANDO = "RANDO"
AE_REVIEW = "AE_REVIEW"
SCREENING = "SCREENING"

# commonly grouped like this ..
CLINIC_USER_GROUPS = [
    ADMINISTRATION,
    EVERYONE,
    SCREENING,
    CLINIC,
    PII,
    RANDO,
    AE_REVIEW,
]
LAB_USER_GROUPS = [ADMINISTRATION, EVERYONE, LAB, PII_VIEW]
TMG_USER_GROUPS = [ADMINISTRATION, EVERYONE, AE_REVIEW]