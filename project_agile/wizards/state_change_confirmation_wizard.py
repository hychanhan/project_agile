# -*- coding: utf-8 -*-
# Copyright 2017 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

from odoo import models, fields, api


class StageChangeConfirmationWizard(models.TransientModel):
    _inherit = 'wkf.project.task.confirmation'

    resolution_id = fields.Many2one(
        comodel_name='project.task.resolution',
        string='Resolution',
    )

    @api.multi
    def prepare_values(self):
        values = super(StageChangeConfirmationWizard, self).prepare_values()

        if self.resolution_id:
            values['resolution_id'] = self.resolution_id.id

        return values
