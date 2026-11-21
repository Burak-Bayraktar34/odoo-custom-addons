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
        'views/kitap_views.xml',
        'views/yazar_views.xml',
        'views/partner_views.xml',
        'views/kutuphane_menus.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}