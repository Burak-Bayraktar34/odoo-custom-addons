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
        'security/ir.access.csv', #burası normald yorum satırlı geliyor ama biz bunu silerek erişim hakkı veriyoruz.
        'views/kitap_views.xml',
        'views/yazar_views.xml',
        'views/kutuphane_menus.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}

