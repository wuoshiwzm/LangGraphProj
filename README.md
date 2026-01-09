# LangGraphProj


## 使用 LangGraph 开发的 Agent:
更好的并发性 （底层使用了 FastAPI , 更快的速度与响应）
比肩 NodeJS 和 Go 的高性能 python web 框架

LangGraph 支持短期存储与长期存储



langgraph build: 构建一个可直接部署的 LangGraph 服务器的 Docker 镜像

langgraph dev   启动一个轻量级开发服务器，无需 Docker 安装。此服务器非常适合快速开发和测试。此功能在0.155 及更高版本中可用。

langgraph dockerfile    生成一个 dockerfile, 可用于 LangGraph API 服务器 构建镜像并部署实例。用于进一步定制 dockerfile 或以更自定义的方式部署。

langgraph up    本地 Docker 容器中启动一个 LangGraph API 服务器实例。这要求 Docker 服务器在本地运行。本地开发需要 LangSmith API 密钥


从 new-langgraph-project-python 模板或 new-langgraph-project-js 模板创建一个新应用。
*** 如果未使用 langgraph new 命令时未指定模板，将显示交互式菜单
langgraph new path/to/app --temp new-langgraph-project-python


进入项目目录并生成 demo 项目：
```
D:\projs\test\python\LangGraphProj>langgraph new langraph_demo
```

进入demo目录并安装需要的包
```
D:\projs\test\python\LangGraphProj\langraph_demo>pip install -e .
```