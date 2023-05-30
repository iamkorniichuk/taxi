DEFAULT_GROUPS = [
    {
        'pk': 1,
        'name': 'customer',
        'permissions': [
            'add_order',
            'add_report'
        ],
        'home_url': 'orders:create'
    },
    {
        'pk': 2,
        'name': 'driver',
        'permissions': [
            'view_order',
            'accept_order'
        ],
        'home_url': 'orders:accept'
    },
    {
        'pk': 3,
        'name': 'manager',
        'permissions': [
            'view_order',
            'view_trip',
            'view_report',
            'add_car',
            'view_car',
            'change_car'
        ],
        'home_url': 'reports:accept'
    },
    {
        'pk': 4,
        'name': 'director',
        'permissions': [

        ]
    }
]
