# pulse-gallery

# 概述

这是一个简单的图片展示页面项目，随机的展示图库中的图片，通过简单的交互标记喜欢或讨厌。

# 技术栈

- react
- typescript
- python

# 功能

- [x] 随机展示一张图片，点击切换
- [ ] 左滑、右滑标记喜爱或讨厌
- [ ] 登录并记录个人喜好

# 如何调试

## 后端

1. 创建python虚拟环境

```bash
python -m venv venv
```

2. 激活虚拟环境

```bash
# Windows
venv\Script\activate

# Linux/maxOS
source venv/bin/activate
```

3. 安装python依赖

```bash
pip install -r requirements.txt
```

4. 运行后端服务

```bash
uvicorn src.backend.main:app --reload
```

api默认端口为

```
http://localhost:8000
```

可以通过浏览器访问下面的地址来检查自动生成的`swagger`文档，辅助api的调试

```
http://localhost:8000/docs
```

## 前端

1. 进入到前端根目录

```bash
cd src/frontend
```

2. 安装依赖

```bash
npm install
```

3. 运行前端服务

```bash
npm run dev
```

默认端口为

```
http://localhost:5173
```
