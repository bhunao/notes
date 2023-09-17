import logging

log = logging.getLogger("notes-api")

log.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('notes_api.log')
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s %(levelname)s %(filename)s.%(funcName)s:%(lineno)s - %(message)s')

# file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

log.addHandler(file_handler)
log.addHandler(console_handler)
