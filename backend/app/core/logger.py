import logging
import logging.config
import os

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'json': {
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'timestamp': True,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'json',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'amchi_payment_gateway.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 3,
            'formatter': 'json',
        },
    },
    'loggers': {
        'amchi': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

if __name__ == '__main__':
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger('amchi')
    logger.info('Logging is configured!')
