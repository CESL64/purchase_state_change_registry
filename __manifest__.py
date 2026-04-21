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
        "views/purchase_order_views.xml",
        "views/state_change_registry_views.xml",
    ],
    "installable": True,
    "application": False,
}
