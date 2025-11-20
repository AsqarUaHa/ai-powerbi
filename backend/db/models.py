from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=True)
    full_name = Column(String(255), nullable=True)
    role = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    queries = relationship("Query", back_populates="user")
    insights = relationship("Insight", back_populates="user")
    scheduled_reports = relationship("ScheduledReport", back_populates="user")


class Dashboard(Base):
    __tablename__ = "dashboards"

    id = Column(Integer, primary_key=True, index=True)
    powerbi_id = Column(String(255), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    category = Column(String(100), nullable=True)
    description = Column(Text, nullable=True)
    page_count = Column(Integer, nullable=True)
    last_sync = Column(DateTime, nullable=True)

    queries = relationship("Query", back_populates="dashboard")
    scheduled_reports = relationship("ScheduledReport", back_populates="dashboard")


class Query(Base):
    __tablename__ = "queries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    dashboard_id = Column(Integer, ForeignKey("dashboards.id"), nullable=True)
    query_text = Column(Text, nullable=False)
    query_type = Column(String(50), nullable=False)  # 'question', 'free_form', 'image'
    response = Column(Text, nullable=True)
    tokens_used = Column(Integer, nullable=True)
    execution_time = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="queries")
    dashboard = relationship("Dashboard", back_populates="queries")
    insights = relationship("Insight", back_populates="query")


class Insight(Base):
    __tablename__ = "insights"

    id = Column(Integer, primary_key=True, index=True)
    query_id = Column(Integer, ForeignKey("queries.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    tags = Column(JSONB, nullable=True)  # список тегов, храним как JSON-массив строк
    is_favorite = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    query = relationship("Query", back_populates="insights")
    user = relationship("User", back_populates="insights")


class ScheduledReport(Base):
    __tablename__ = "scheduled_reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    dashboard_id = Column(Integer, ForeignKey("dashboards.id"), nullable=False)
    schedule_cron = Column(String(100), nullable=False)
    report_config = Column(JSONB, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    next_run = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="scheduled_reports")
    dashboard = relationship("Dashboard", back_populates="scheduled_reports")
