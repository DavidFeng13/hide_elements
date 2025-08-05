{
    'name': 'Hide Odoo Elements',
    'version': '1.1',
    'summary': 'Hide copyright and other elements in settings page',
    'description': """
        Hide Elements Module for Odoo Settings Page:
        - Hide copyright information
        - Hide Odoo S.A. related information
        - Hide system notification area
        
        This module automatically hides specific elements on the settings page 
        after installation, no additional configuration needed.
    """,
    'category': 'Technical',
    'author': 'Shanghai JingCheng Information Technology Co., Ltd.',
    'website': 'https://www.erpjc.cn',
    'license': 'OPL-1',
    'depends': ['web'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'hide_elements/static/src/css/hide_elements.css',
        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
    ],
    'price': 0.0,
    # 'currency': 'USD',
    'installable': True,
    'application': False,
    'auto_install': False,
    'support': 'jcerp@aliyun.com',

} 
