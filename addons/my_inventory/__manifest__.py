# noinspection PyStatementEffect
{
    'name': "My Inventory",
    'summary': "Manage all your stock and logistics",
    'sequence': 1,
    'description': "This is an inventory module, here you can manage your stock and logistics.",
    'author': "Aniket",
    'category': 'MyModules',
    'version': '1.0',
    'depends': [
        'base',
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/actions.xml',
        'views/menu-items.xml',
        'views/views.xml',
    ],
    "application": True,
    "installable": True,
}
