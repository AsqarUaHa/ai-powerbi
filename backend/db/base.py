from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Импорт моделей, чтобы они регистрировались в metadata
# (не удаляйте этот импорт, даже если IDE помечает как неиспользуемый).
try:  # pragma: no cover - защита от циклических импортов при статическом анализе
    from . import models  # noqa: F401
except Exception:  # pragma: no cover
    pass
