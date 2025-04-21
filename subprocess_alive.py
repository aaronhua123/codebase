import random
import time
from multiprocessing import Process, Value


def run(share1):
    while True:
        # print("Hello World!")
        with share1.get_lock():
            share1.value = time.time()
        time.sleep(random.choice((3, 3, 3, 3, 5)))


if __name__ == '__main__':
    data = {}

    for i in range(2):
        share = Value("d", time.time())
        p = Process(target=run, args=(share,), daemon=True)
        p.start()
        data[p.ident] = (p, share)

    while True:
        time.sleep(1)
        # 活跃进程数量
        print("跃进程数量", len([p for ident, (p, share) in data.items() if p.is_alive()]))
        del_list = []
        for ident, (p, share) in data.items():
            # print(ident, share.value)
            with share.get_lock():
                if time.time() - share.value > 4:
                    print(f"进程{ident}心跳丢失，重启中...")
                    del_list.append(p)
                elif not p.is_alive():
                    print(f"进程{ident}进程假死，重启中...")
                    del_list.append(p)

        if del_list:
            print("需要重启进程数量", len(del_list))
            for p in del_list:
                del data[p.ident]
                p.terminate()
                p.join()
                share = Value("d", time.time())
                p = Process(target=run, args=(share,), daemon=True)
                p.start()
                data[p.ident] = (p, share)
            del_list = []
