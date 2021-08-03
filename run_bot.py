import os, django
from threading import Thread
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CrmProject.settings')
django.setup()

from crm.bot import *
from manage import main


def run_polling(*args):
    client.polling(none_stop, interval)


if __name__ == '__main__':
    interval = 0
    none_stop = True
    t = Thread(target=run_polling(), args=(none_stop, interval))
    t.start()
    main()