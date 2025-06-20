def make_car(manufacturer, model, **options):
    dict_car = {
        "manufacturer": manufacturer.title(),
        "model": model.title(),
    }

    for option, value in options.items():
        dict_car[option] = value

    return dict_car


print(make_car("vinfast", "vietnam", color="blue"))
print(make_car("subaru", "outback", color="blue", tow_package=True))
