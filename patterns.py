from datetime import datetime
import random

x = random.choice(["en", "et", "es"])

match x:
    case "en":
        print("Hello!")
    case "et":
        print("Tere!")
    case "es":
        print("¡Hola!")
    case _:
        print("Yo")

language_codes = ["en", "en_GB", "en_US", "et_EE", "Outer_Space"]
languages = {"en": "English", "et": "Eesti"}
countries = {"GB": "U.K.", "US": "U.S.", "EE": "Estonia"}

language_code = random.choice(language_codes)

match language_code.split("_"):
    case [lang]:
        print(f"{languages[lang]}, international")
    case [lang, country] if country in countries:
        print(f"{languages[lang]}, {countries[country]}")
    case _:
        print("Probably still English. Or perhaps Klingon?")

formats = {
    "en_US": {"time": "%I:%M%p", "date": "%Y/%m/%d"},
    "et_EE": {"time": "%H:%M", "date": "%d.%m.%Y"},
    "Outer_Space": {
        "time": "Seconds since the Big Bang",
        "date": "Depends on the planet, apparently",
    },
}

match formats.get(language_code):
    case {"time": "Seconds since the Big Bang"}:
        print("Just acknowledge the futility of existence.")
    case {"time": timefmt, "date": datefmt}:
        now = datetime.now()
        print(f"Today is {now.strftime(datefmt)}, and it's {now.strftime(timefmt)} now.")
    case _:
        print(datetime.now().isoformat())
