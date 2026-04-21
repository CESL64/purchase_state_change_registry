from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def write(self, vals):
        track_state = "state" in vals
        previous_states = {order.id: order.state for order in self} if track_state else {}

        res = super().write(vals)
        if not track_state:
            return res

        registry_model = self.env["state.change.registry"]

        for order in self:
            if order.partner_id.not_registry_change:
                continue

            previous_state = previous_states.get(order.id)
            new_state = order.state
            if previous_state == new_state:
                continue

            change_dt = fields.Datetime.now()
            change_dt_text = fields.Datetime.to_string(change_dt)
            order.message_post(
                body=f"Registro de estado actualizado en {change_dt_text}",
            )

            taxes = order.order_line.mapped("taxes_id").mapped("name")
            registry_model.create(
                {
                    "name": order.name or order.partner_ref or str(order.id),
                    "document_type": "purchase",
                    "amount": order.amount_total,
                    "line_count": len(order.order_line),
                    "tax_summary": ", ".join(sorted(set(taxes))),
                    "company_id": order.company_id.id,
                    "previous_state": previous_state,
                    "new_state": new_state,
                    "change_date": change_dt,
                    "user_id": self.env.user.id,
                }
            )

        return res
