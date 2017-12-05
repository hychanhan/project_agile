# -*- coding: utf-8 -*-
# Copyright 2017 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

{
    "name": "Project Agile Kanban",
    "summary": "This module enables you to manage your projects by using agile kanban methodology",
    "category": "Project",
    "version": "10.0.0.1.0",
    "license": "LGPL-3",
    "author": "Modoolar",
    "website": "https://www.modoolar.com/",

    "depends": [
        "project_agile",
    ],

    "data": [
        "views/project_agile_board_views.xml",
        "views/project_agile_kanban.xml",
    ],

    "demo": [],
    "qweb": [
        "static/src/xml/*.xml",
    ],
    "application": True,
    "post_init_hook": "_post_init_hook",
}