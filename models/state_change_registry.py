from odoo import fields, models
from odoo.exceptions import UserError


class StateChangeRegistry(models.Model):
    _inherit = "state.change.registry"

    purchase_id = fields.Many2one(
        comodel_name="purchase.order",
        string="Orden de Compra",
    )

    def send_state_change_notification(self):
        self.ensure_one()
        result = super().send_state_change_notification()

        if self.document_type != "purchase":
            return result

        if not self.purchase_id:
            raise UserError("Este registro no esta ligado a una orden de compra.")

        partners_to_notify = self.purchase_id.message_partner_ids.filtered("email")
        if not partners_to_notify:
            raise UserError(
                "La orden de compra no tiene seguidores con correo electronico para notificar."
            )

        template = self.env.ref(
            "purchase_state_change_registry.mail_template_purchase_state_change_notification"
        )
        rendered_mail_values = template._generate_template(
            [self.id],
            ("body_html", "subject", "email_from"),
        ).get(self.id, {})

        self.purchase_id.message_post(
            body=rendered_mail_values.get("body_html"),
            subject=rendered_mail_values.get("subject"),
            email_from=(
                rendered_mail_values.get("email_from")
                or self.env.user.email_formatted
                or self.env.company.email
            ),
            partner_ids=partners_to_notify.ids,
            message_type="comment",
            subtype_xmlid="mail.mt_comment",
            email_layout_xmlid="mail.mail_notification_layout_with_responsible_signature",
        )

        self.message_post(
            body=(
                "Se envio notificacion por correo para el cambio de estado "
                f"'{self.previous_state or ''}' -> '{self.new_state or ''}'."
            ),
            subtype_xmlid="mail.mt_note",
        )

        self.mail_sent = True
        return result
