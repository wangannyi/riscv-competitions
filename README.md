# 环境设置

## 安装依赖

```
sudo apt update
sudo apt install -y libopenblas-dev \
python3-dev \
python3-venv \
libcjson-dev libasound2-dev
```

## 创建 python 虚拟环境

```Bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip config set global.extra-index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple
python3 -m venv hwenv
source ~/hwenv/bin/activate
pip install gpiozero pyserial smbus
```