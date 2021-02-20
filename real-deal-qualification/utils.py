import time
import logging

logger = logging.getLogger()

def timer(func):
    def wrapper(*arg, **kw):
        '''source: http://www.daniweb.com/code/snippet368.html'''
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        logger.info(f'Time ({func.__name__}): {t2 - t1}')
        return res
    return wrapper
