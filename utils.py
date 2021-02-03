import calendar


def get_context(settings, data):
    total_hours, total, table_items = get_task_list(data["items"], settings["hour_rate"])
    context = {
        "contract_num": settings.get("contract_num", ''),
        "contract_date": settings.get("contract_date", ''),

        "sup_num": settings.get("sup_num", ''),
        "sup_date": settings.get("sup_date", ''),

        "city": settings.get("city", ''),
        "user_name": settings.get("user_name", ''),
        "user_address": settings.get("user_address", ''),

        "report_period": get_report_period(data),

        'act_num': data["act_num"],
        'act_date': format_date(data["act_date"]),

        'bill_num': data["bill_num"],
        'bill_date': format_date(data["bill_date"]),

        "total_hours": total_hours,
        "total_sum": format_money(total),
        "total_text": get_sum_as_text(total),

        "hour_rate": format_money(settings["hour_rate"]),

        "items": [
            {
                "index": '1',
                "text": "Item 1",
                "hours": "10,4",
                "sum": "10 400,00",
            },
            {
                "index": '2',
                "text": "Item 2",
                "hours": "11,4",
                "sum": "11 400,00",
            }
        ],

        "output_doc_name": get_document_name(data["act_date"])
    }
    return context


def get_month_name(month_num, genitive=True):
    months_nominative = [
        "январь", "февраль", "март", "апрель", "май", "июнь",
        "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"
    ]
    months_genitive = [
        "января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря"
    ]
    if genitive:
        months = months_genitive
    else:
        months = months_nominative
    return months[month_num - 1]


def get_report_period(data):
    rep_year = data["report_year"]
    rep_month = data["report_month"]
    last_day = calendar.monthrange(rep_year, rep_month)[1]
    return f"с 1 по {last_day} {get_month_name(rep_month)} {rep_year} года"


def format_date(date):
    return f'«{date.day}» {get_month_name(date.month)} {date.year} г.'


def calculate_sum_from_hours(hours, hour_rate):
    return hours * hour_rate


def get_task_list(items, hour_rate):
    table_items = []
    total_hours = 0
    total = 0
    for idx, item in enumerate(items):
        item_sum = calculate_sum_from_hours(item["hours"], hour_rate)
        table_item = {
            "index": idx,
            "text": item["text"],
            "hours": item["hours"],
            "sum": item_sum,
        }
        table_items.append(table_item)
        total_hours = total_hours + item["hours"]
        total = total + item_sum

    return total_hours, total, table_items


def get_sum_as_text(decimal):
    return "Сумма прописью"


def format_money(decimal):
    return "{:,.2f}".format(decimal).replace(',', ' ').replace('.', ',')


def get_document_name(act_date):
    return f'Акт Павлушкин от {act_date} ({get_month_name(act_date.month, genitive=False)})'


def print_output_information(context):
    print(f'Создан документ: "{context["output_doc_name"]}"')
    print("-------------------------------------------------------------------------------------------------------")
    print(f'Счет № {context["bill_num"]} от {context["bill_date"]}      Часов: {context["total_hours"]}')
    print(f"""Работы по Дополнительному соглашению №{context["sup_num"]} от {context["sup_date"]} по разработке сервисов, веб-приложений 
и мобильных приложений для платформ iOS и Android за отчетный период {context["report_period"]}""")
    print("-------------------------------------------------------------------------------------------------------")
    print(f'Акт № {context["act_num"]} от {context["act_date"]}     Сумма: {context["total_sum"]} р.')
    print(f'Основание: ДС №{context["sup_num"]} от {context["sup_date"]} к Договору № {context["contract_num"]} от {context["contract_date"]}')
    print("-------------------------------------------------------------------------------------------------------")
