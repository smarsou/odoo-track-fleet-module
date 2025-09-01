
from odoo import models, fields, api

class Truck(models.Model):
    # Definition
    _name = "trackfleet.truck"
    _description = "Truck"
    # Identification
    name = fields.Char("License Plate", required=True)
    driver_id = fields.Many2one("res.partner", string="Driver")
    # Details
    capacity_t = fields.Float("Capacity (t)")
    mileage = fields.Integer("Mileage (km)")
    status = fields.Selection([
        ('available', 'Available'),
        ('in_delivery', 'In Delivery'),
        ('maintenance', 'Maintenance')
    ], string="Status", default="available")
    active = fields.Boolean('Active', default=True)
    # Maintenance
    last_maintenance_date = fields.Date("Last Maintenance Date")
    next_maintenance_date = fields.Date("Next Maintenance Date")
    maintenance_due = fields.Boolean(
        string="Maintenance Due",
        compute="_compute_maintenance_due",
        store=True
    )
    delivery_ids = fields.One2many("trackfleet.delivery", "truck_id", string="Deliveries")

    @api.depends("next_maintenance_date")
    def _compute_maintenance_due(self):
        today = fields.date.today()
        for truck in self:
            if truck.next_maintenance_date:
                truck.maintenance_due = truck.next_maintenance_date <= today
            else:
                truck.maintenance_due = False