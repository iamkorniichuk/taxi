DEFAULT_GROUPS = [
    {"pk": 1, "name": "customer", "permissions": ["add_order", "add_report"]},
    {"pk": 2, "name": "driver", "permissions": ["view_order", "accept_order"]},
    {
        "pk": 3,
        "name": "manager",
        "permissions": [
            "view_order",
            "view_trip",
            "view_report",
            "answer_report",
            "add_car",
            "view_car",
            "change_car",
        ],
    },
    {"pk": 4, "name": "director", "permissions": []},
]
