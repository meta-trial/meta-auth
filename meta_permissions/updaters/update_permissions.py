from edc_permissions.permissions_updater import PermissionsUpdater
from edc_permissions.utils import (
    create_edc_dashboard_permissions,
    create_edc_navbar_permissions,
)

from ..group_names import RANDO, AE_REVIEW, SCREENING
from .ae_review import update_ae_review_group_permissions
from .auditor import extra_auditor_group_permissions
from .clinic import extra_clinic_group_permissions
from .lab import extra_lab_group_permissions, extra_lab_view_group_permissions
from .pii_models import extra_pii_models
from .rando import update_rando_group_permissions
from .screening import update_screening_group_permissions

extra_updaters = [
    extra_auditor_group_permissions,
    extra_clinic_group_permissions,
    extra_lab_group_permissions,
    extra_lab_view_group_permissions,
    update_rando_group_permissions,
    update_ae_review_group_permissions,
    update_screening_group_permissions,
]


def update_permissions():

    create_edc_dashboard_permissions(
        extra_codename_tpls=[
            ("edc_dashboard.view_ae_listboard", "Can view AE Listboard"),
            ("edc_dashboard.view_screening_listboard", "Can view Screening Listboard"),
            ("edc_dashboard.view_subject_listboard", "Can view Subject Listboard"),
        ]
    )
    create_edc_navbar_permissions(
        extra_codename_tpls=[
            ("edc_navbar.nav_ae_section", "Can access AE section"),
            ("edc_navbar.nav_subject_section", "Can access subject section"),
            ("edc_navbar.nav_screening_section", "Can access screening section"),
        ]
    )

    PermissionsUpdater(
        extra_pii_models=extra_pii_models,
        extra_updaters=extra_updaters,
        extra_group_names=[AE_REVIEW, RANDO, SCREENING],
    )
