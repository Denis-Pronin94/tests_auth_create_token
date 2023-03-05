valid_data = [{
    'firstname': 'Jim',
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'J',
    'lastname': 'B',
    'totalprice': 9,
    'depositpaid': False,
    'bookingdates': {
        'checkin': '2016-01-01',
        'checkout': '2022-01-01',
    },
    'additionalneeds': 'B',
},
    {
    'firstname': 'Jimmmmmmmm',
    'lastname': 'Brownnnnnnnnnnnn',
    'totalprice': 99999999999,
    'depositpaid': False,
    'bookingdates': {
        'checkin': '2016-01-01',
        'checkout': '2022-01-01',
    },
    'additionalneeds': 'Breakfasttttttttttt',
},
]

no_parameter_in_data = [{
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 'Brown',
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 'Brown',
    'totalprice': 111,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
},
]

negative_type_in_data = [{
    'firstname': 123,
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 123,
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 'Brown',
    'totalprice': '111',
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': 'True',
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': 'Jim',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': 'Brown',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 123,
},
    {
    'firstname': True,
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': False,
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 'Brown',
    'totalprice': True,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': True,
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': False,
    },
    'additionalneeds': 'Breakfast',
},
    {
    'firstname': 'Jim',
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': True,
},
]

ids_test_positive = [
    'Валидные значения из документации',
    'Валидные значения с короткими значениями',
    'Валидные значения с длинными значениями',
]

ids_for_test_no_parameter = [
    'Нет параметра firstname',
    'Нет параметра lastname',
    'Нет параметра totalprice',
    'Нет параметра depositpaid,',
    'Нет параметра bookingdates',
    'Нет параметра checkin',
    'Нет параметра checkout',
    'Нет параметра additionalneeds',
]

ids_test_wrong_value = [
    'firstname - число',
    'lastname - число',
    'totalprice - строка',
    'depositpaid - строка',
    'checkin - строка',
    'checkout - строка',
    'additional_needs - число',
    'firstname - булевое значение',
    'lastname - булевое значение',
    'totalprice - булевое значение',
    'checkin - булевое значение',
    'checkout - булевое значение',
    'additionalneeds - булевое значение',
]
