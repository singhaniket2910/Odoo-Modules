# noinspection PyStatementEffect
{
    'name': "MyModule",
    'summary': "Just for learning purpose",
    'sequence': 2,
    'description': "This is a basic module, just for learning purpose.",
    'author': "Aniket",
    'category': 'MyModules',
    'version': '1.0',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_views.xml',
    ],
    "application": True,
    "installable": True,
}
