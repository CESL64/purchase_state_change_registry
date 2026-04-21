from odoo import fields, models


class StateChangeRegistry(models.Model):
    _inherit = "state.change.registry"

    purchase_id = fields.Many2one(
        comodel_name="purchase.order",
        string="Orden de Compra",
    )
