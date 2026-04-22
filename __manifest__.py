{
    "name": "Purchase State Change Registry",
    "version": "18.0.1.0.0",
    "summary": "Registro de cambios de estado para compras",
    "description": "Hereda purchase.order para registrar cambios en state.",
    "author": "Prueba Tecnica",
    "license": "LGPL-3",
    "category": "Purchases",
    "depends": [
        "purchase",
        "state_change_registry",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/mail_template_data.xml",
        "views/purchase_order_views.xml",
        "views/state_change_registry_views.xml",
        "wizard/state_change_registry_report_wizard_views.xml",
        "views/menus.xml",
        "reports/purchase_order_state_change_registry_report_inherit.xml",
    ],
    "installable": True,
    "application": False,
}
