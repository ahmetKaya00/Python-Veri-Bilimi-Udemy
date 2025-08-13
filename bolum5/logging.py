import logging

logging.basicConfig(
    filename="app.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.ERROR
)

logging.debug("Bu debug mesajıdır.")
logging.info("Program başladı")
logging.warning("Düşük disk alanı!")
logging.critical("Sunucu Çöktü!")

logging.basicConfig(level=logging.ERROR)

try:
    sayi = 10 / 0
except ZeroDivisionError:
    logging.error("Sıfıra bölme hatası!")