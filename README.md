# BS Monthly Report Maker

-------
## How to use

### I - Toggl:
1. Go to reports
2. Choose period
3. Assert no rounding
4. Export xlsx file
   
### II - Excel file:
1. Upload and open in Google Docs
2. Copy a billed hours column
3. Format it to number
4. *24

### III - Prepare data:
1. Open act_data, create a new item at zero index
2. Determine tasks, put names in act_data[0]
3. Calculate hours for tasks, fill out act_data[0]
   
### IV - Generate docx:
1. Activate venv `source .venv/bin/activate`
2. Run `python main.py`

### V - Bank
1. Go to a bank
2. Copy existing bill
3. Modify the bill using prepared text
4. Download the bill

### Vi - Diadoc
1. Open Diadok
2. Create a new package
3. Upload act and bill
4. Fill out form using prepared data
5. Sign a package

-------
## Installation
1. Clone a repo
2. Create a virtual environment
3. Activate venv: `source .venv/bin/activate`
4. Install dependencies `pip install -r requirements.txt `
5. Create a template file `act_v1.docx` (name can be adjusted in settings) and put it to `templates` folder
6. Put template variables to the template file
7. Add and adjust settings/settings.yaml `$ cp settings/tpl.settings.yaml settings/settings.yaml`

-------
## Template variables
| Name | Description | Example |
| --- | --- | --- |
| contract_num | Номер основного договора | 7Р-10 |
| contract_date | Дата основного договора | «25» сентября 2019 г. |
| sup_num | Номер дополнительного соглашения | 1 |
| sup_date | Дата дополнительного соглашения | «25» сентября 2019 г. |
| city | Населенный пункт | г. Красноярск |
| user_name | Исполнитель | Иванов Иван Иванович |
| user_address | Адрес исполнителя | г. Красноярск, ул. , кв. |
| report_period | Отчетный период текстом | с 1 по 31 января 2021 года |
| act_num | Номер акта | 21 |
| act_date | Дата акта | «1» марта 2021 г. |
| total_sum | Общая сумма цифрами (руб.) | 11 500 р. |
| total_text | Общая сумма текстом | Сто одна тысяча пятьсот рублей 00 копеек |
| hour_rate | Ставка в час (руб.) | 600,00 |
| {%tr for item in items %} | Открывающий тег |  |
| item.index | Номер задачи | 1 |
| item.text | Наименование задачи | Работы по созданию... |
| item.hours | Часы по задаче | 11,4 |
| item.sum | Сумма по задаче | 11 400,00 |
| {%tr endfor %} | Закрывающий тег |  |
