
import logging

#logging.basicConfig(filemode='w')

# создаем регистратор
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
# создаём обработчик логера
handler = logging.FileHandler('out.log')
handler.setLevel(logging.DEBUG)

# строка формата сообщения
strfmt = '[%(asctime)s] [%(name)s] [%(levelname)s] %(filename)s %(funcName)s %(module)s > %(message)s'
# строка формата времени
datefmt = '%Y-%m-%d %H:%M:%S'
# создаем форматтер
formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)
# добавляем форматтер к 'ch'
handler.setFormatter(formatter)
# обработчик добавляется в логгер
log.addHandler(handler)

log.debug('debug message')
log.info('info message')
log.warning('warn message')
log.error('error message')
log.critical('critical message')
