def celcius_to_fahrenheit(suhu_celcius):
    """Fungsi konversi suhu Celcius ke Fahrenheit
    Argument:
        suhu_celcius (float/int): Suhu dalam celcius yang akan dikonversi
    Return:
        suhu_fahrenheit (float): Hasil konversi berupa suhu dalam Fahrenheit
    """
    suhu_fahrenheit=(9/5*suhu_celcius)+32
    return suhu_fahrenheit

def fahrenheit_to_celcius(suhu_fahrenheit):
    """Fungsi konversi suhu Fahrenheit ke Celcius
    Argument:
        suhu_fahrenheit (float/int): Suhu dalam Fahrenheit yang akan dikonversi
    Return:
        suhu_celcius (float): Hasil konversi berupa suhu dalam Fahrenheit
    """
    suhu_celcius=(suhu_fahrenheit-32)*5/9
    return suhu_celcius