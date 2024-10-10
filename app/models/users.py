from app.database import Base
from sqlalchemy import Column, String, Enum as SQLAEnum, UUID
from pydantic import BaseModel, Field
from enum import Enum
import uuid

# Define user roles using Enum
class UserRole(str, Enum):
    super_admin = "super_admin"
    seller = "seller"
    buyer = "buyer"
    
# Define source types for user creation
class UserSource(str, Enum):
    email = "email"
    google = "google"
    apple = "apple"

# SQLAlchemy User model
class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username = Column(String(30), nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    
    # Use SQLAlchemy Enum type for role and source
    role = Column(SQLAEnum(UserRole), nullable=True)  
    password = Column(String, nullable=False)
    source = Column(SQLAEnum(UserSource), nullable=False)  

# Pydantic User model
class CreateUserRequest(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier for the user")
    username: str = Field(..., max_length=30, description="Username for the user")
    email: str = Field(..., description="User's email")
    role: UserRole = Field(..., description="Role of the user in the system")
    password: str = Field(..., min_length=8, description="Password for the user")
    source: UserSource = Field(..., description="Source of the user registration")
