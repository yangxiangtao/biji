

def fry_egg():
    print('打开天然气')
    try:
        count=int(input('请输入鸡蛋个数：'))
        print('完成煎鸡蛋，共煎了%d个蛋'%count)
    finally:
        print('关闭天然气')

try:
    fry_egg()
except ValueError:
    print('煎蛋过程出错！')