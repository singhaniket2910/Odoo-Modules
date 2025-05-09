{
    'name': "First Custom Module",
    'summary': "Dummy Module",
    'description': "This is a basic module, just for learning purpose.",
    'author': "Aniket",
    'website': "https://spyadav.odoo.com/",
    'category': 'No category',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/first_module_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    "application": True,
    "installable": True,
}
