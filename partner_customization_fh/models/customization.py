from odoo import models, fields, api, _


class ResPartnerCustom(models.Model):
    _inherit = 'res.partner'

    id_number = fields.Char(string='ID Number')
    registration_number = fields.Char(string='Registration Number', readonly=True,
                                      default=lambda self: _('/'))
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    date_of_birth = fields.Date(string='Date of Birth')
    PIN_NO = fields.Char(string='KRA PIN')

    @api.model
    def create(self, vals):
        if vals.get('registration_number', '/') == '/':
            vals['registration_number'] = self.env['ir.sequence'].next_by_code('res.partner.registration') or '/'

            # Set the tax_id field value to the generated registration number
            vals['vat'] = vals.get('registration_number', False)
        return super(ResPartnerCustom, self).create(vals)
