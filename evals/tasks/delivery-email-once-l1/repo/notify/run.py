from infra.kv import KV

from .mailer import Mailer
from .worker import Worker


def main():
    worker = Worker(KV.connect(), Mailer())
    return worker


if __name__ == "__main__":
    main()
