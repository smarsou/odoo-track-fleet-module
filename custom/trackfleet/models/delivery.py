from odoo import models, fields, api

class Delivery(models.Model):
    _name = "trackfleet.delivery"
    _description = "Delivery"

    # Relations
    truck_id = fields.Many2one("trackfleet.truck", string="Assigned Truck", required=True)
    customer_id = fields.Many2one("res.partner", string="Customer", required=True, domain="[('name', '=like', 'DEMO%')]")

    # Details
    planned_date = fields.Datetime("Planned Date", required=True)
    delivery_date = fields.Datetime("Actual Delivery Date")
    status = fields.Selection([
        ("scheduled", "Scheduled"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
        ("canceled", "Canceled"),
    ], string="Status", default="scheduled", group_expand="_expand_groups")

    # Adresse (position géographique du client)
    destination_address = fields.Char("Destination Address", required=True)

    # Quantité transportée
    weight_t = fields.Float("Weight (t)", help="Total weight of goods transported")

    # Notes
    notes = fields.Text("Notes")


    @api.model
    def _expand_groups(self, states, domain):
        return ['scheduled', 'in_progress', 'done', 'canceled']
    
    # Gestion automatique de la référence
    # @api.model
    # def _compute_ref(self):
    #     for record in self:
    #         if record.name == "New":
    #             record.name = self.env["ir.sequence"].next_by_code("trackfleet.delivery") or "New"
