# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

from odoo.addons.project_agile.controllers import main


class AgileController(main.AgileController):
    def prepare_transition(self, transition):
        data = super(AgileController, self).prepare_transition(transition)
        data['task_type_ids'] = [x['id'] for x in transition.task_type_ids]
        return data
