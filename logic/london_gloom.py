def evaluate_vibe(weather: str, tea_status: str, pocket_money_pounds: float) -> str:
    """Ocenia poziom edgy klimatu w skali brytyjskiej depresji pogodowej."""
    weather = weather.lower().strip()
    tea_status = tea_status.lower().strip()

    if "rain" in weather and tea_status == "none":
        return (
            "Mroczna otchłań. Pada deszcz, a w szafce nie ma nawet jednej "
            "torebki PG Tips. Słuchasz The Smiths i patrzysz w ścianę."
        )

    if pocket_money_pounds < 1.50:
        return (
            "Kompletny upadek. Nie stać Cię nawet na najtańszą paczkę chipsów "
            "o smaku octu (Salt & Vinegar) z Tesco. Absolute shambles."
        )

    if "sun" in weather:
        return (
            "Słońce w Anglii? Obrzydliwe. To psuje cały gotycki klimat. " "Schowaj się do piwnicy."
        )

    return (
        "Typowy, nudny, szary dzień w Londynie. Narzekasz na rząd, "
        "metro spóźnia się o 40 minut. Jest stabilnie."
    )
