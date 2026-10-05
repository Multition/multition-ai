from datetime import UTC, datetime
from typing import Annotated

from fastapi import Depends, FastAPI

from multition_ai import __version__
from multition_ai.config import Settings, get_settings

app = FastAPI(
    title="Multition AI Service",
    version=__version__,
    description="Technical scaffold for future Multition AI capabilities.",
)

@app.get("/health")
def health(settings: Annotated[Settings, Depends(get_settings)]) -> dict[str, str]:
    return {
        "status": "ok",
        "service": "multition-ai",
        "version": __version__,
        "environment": settings.app_env,
        "timestamp": datetime.now(UTC).isoformat(),
    }
