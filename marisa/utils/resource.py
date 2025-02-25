"""检查资源完整性"""

import zipfile

import httpx
import aiofiles
from nonebot import logger
from rich.progress import (
    Progress,
    BarColumn,
    TextColumn,
    DownloadColumn,
    TransferSpeedColumn,
)

from ..configs import DATA_DIR


async def check_resource():
    """检查资源"""

    if not DATA_DIR.exists():
        DATA_DIR.mkdir(parents=True, exist_ok=True)

    logger.info("正在检查资源完整性")

    file_count = len([f for f in DATA_DIR.iterdir() if f.is_file()])
    subfolders_count = len([f for f in DATA_DIR.iterdir() if f.is_dir()])

    if (file_count + subfolders_count) < 8:
        logger.info("资源缺失，即刻下载")
        try:
            async with httpx.AsyncClient(timeout=10.0).stream(
                "GET",
                url="https://github.com/MyXiaoNan/resources/raw/main/resources.zip",
                follow_redirects=True,
            ) as response:
                async with aiofiles.open(DATA_DIR / "resources.zip", "wb") as wf:
                    total: int = int(response.headers["Content-Length"])
                    with Progress(
                        TextColumn(DATA_DIR.name),
                        "[progress.percentage]{task.percentage:>3.0f}%",
                        BarColumn(bar_width=None),
                        DownloadColumn(),
                        TransferSpeedColumn(),
                    ) as progress:
                        download_task = progress.add_task("Download", total=total)
                        async for chunk in response.aiter_bytes():
                            await wf.write(chunk)
                            await wf.flush()
                            progress.update(
                                download_task,
                                completed=response.num_bytes_downloaded,
                            )
            zipfile.ZipFile(DATA_DIR / "resources.zip").extractall(DATA_DIR)
            (DATA_DIR / "resources.zip").unlink()
            logger.success("资源下载完成")
        except httpx.ReadTimeout:
            logger.warning("下载超时")
    else:
        logger.info("资源完好，无需下载")
