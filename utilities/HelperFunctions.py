import random
import string


def generate_random_string(size):
    """
    Generates a random string of the specified size.

    :param size: The length of the random string to generate.
    :return: A random string consisting of letters and digits.
    """
    random_text = ''.join(random.choices(
        string.ascii_letters + string.digits, k=size))
    return random_text

def format_date_by_locale(driver, date):
    """
    Formats a date string based on the system's locale settings.

    :param driver: WebDriver instance used to execute JavaScript for retrieving locale.
    :param date: The date string in 'YYYY-MM-DD' format to be formatted.
    :return: A formatted date string according to the locale or a message if the locale is not supported.
    """
    locale_date_format = driver.execute_script("""
        return new Intl.DateTimeFormat().resolvedOptions().locale;
    """)

    date = date.split("-")
    year = date[0]
    month = date[1]
    day = date[2]

    if "en-US" in locale_date_format:
        return f"{month}/{day}/{year}"
    elif "en-GB" in locale_date_format or "fr-FR" in locale_date_format:
        return f"{day}/{month}/{year}"
    elif "zh-CN" in locale_date_format:
        return f"{year}-{month}-{day}"
    else:
        return "Locale-based format could not be determined."
