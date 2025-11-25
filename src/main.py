# src/main.py
from fastapi import FastAPI, Response, Depends

from src.core.config import Settings, get_settings
from src.core.exception import register_exception_handlers
from src.lifespan import lifespan

app = FastAPI(
    app_name=Settings.app_name,
    version="0.1.1",
    description="FastAPI 练习项目实战",
    lifespan=lifespan)

register_exception_handlers(app)


# 路由引入
@app.get("/")
def read_root(
        # 使用 FastAPI 的依赖注入系统来获取配置实例
        # 使用 get_settings 函数进行依赖注入
        settings: Settings = Depends(get_settings),
):
    """
    一个示例端点，演示如何访问配置。
    """
    return {
        "message": f"Hello from the {settings.app_name}!",
        # 演示如何使用在模型中动态计算的属性
        "database_url": settings.database_url,
        "jwt_secret": settings.jwt_secret,
    }


@app.get("/health")
async def health_check(response: Response):
    response.status_code = 200
    return {"status": "ok 👍 "}
