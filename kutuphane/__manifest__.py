{
    'name': "Kütüphane",

    'summary': "Kitap ve ödünç takibi",

    'description': """
Kütüphanedeki kitapları ve ödünç verme işlemlerini takip eden alıştırma modülü.
    """,

    'author': "Burak Bayraktar",
    'website': "https://github.com/Burak-Bayraktar34",

    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    'depends': ['base'],

    'data': [
        'security/ir.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}

