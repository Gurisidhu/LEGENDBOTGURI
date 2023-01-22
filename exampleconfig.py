from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 18734981
    API_HASH = "0e88a144af021c41897a8e826eaf96aa"
    # the name to display in your alive message
    ALIVE_NAME = "Your value"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "Your value"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    LEGEND_STRING = "1BVtsOIwBu3zwRlimbAdtWkRH9sIkVwzPJBLlwMaSpmNP5DYa0dfLO5qSGn8eSnlPi_ldY-PzjIVLJJef05aeVQkDvDrAdmsAMuk_WYU7bleZtrvJvXAS1eH8Kw0rljqXx2930ZGIkgL87BWWoLQUlN7cdaf5fsDWS7bMyC4PN8tS_cWFCcXp8jd6TpSaj82wl2K5B5rYlv4Hkr08A_pqmjpIVWYzfR3rG6Bbl7PrGzbwvPVfcBmiU5an4drLcWeTFkHuJIBJVCpxB76kystHN-O_G2tJuneA7dHJXQG0YPl5NQ2OuaWZS9xdqjygX0zWCMwVDet4VIaCYMdOJDwLa2xPMurIqRQ="
    # create a new bot in @botfather and fill the following vales with bottoken
    BOT_TOKEN = "5784670818:AAGE0FoC5zpQHeDgXBH6XllEnRv1yfdN1co"
    # command handler
    HANDLER = "."
    # command hanler for sudo
    SUDO_HANDLER = "."
    # External plugins repo
    EXTRA_REPO = "https://github.com/ITS-LEGENDBOT/PLUGINS"
    UPSTREAM_REPO = "pro"
    # Your City's TimeZone
    TZ = "Your value"
