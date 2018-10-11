# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('blockchain', 'index'), []),
    (T('Create Study'), False, URL('blockchain', 'create_study'), []),
    (T('View Blockchain'), False, "#", [
        (T('Process'), False, URL('blockchain', 'view',args="blockchain_path_process"), []),
        (T('Presentation'), False, URL('blockchain', 'view',args="blockchain_path_presentation"), []),
        (T('Data'), False, URL('blockchain', 'view',args="blockchain_path_data"), [])
        ])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

