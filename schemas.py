"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import date, time

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Taste of Budapest specific schemas

class Reservation(BaseModel):
    """Reservations collection schema (collection name: "reservation")"""
    name: str = Field(..., min_length=2)
    email: EmailStr
    phone: str = Field(..., min_length=6, max_length=30)
    date: date
    time: str = Field(..., description="Time in HH:MM")
    guests: int = Field(..., ge=1, le=20)
    special_requests: Optional[str] = Field(None, max_length=1000)

class ContactMessage(BaseModel):
    """Contact messages collection schema (collection name: "contactmessage")"""
    name: str = Field(..., min_length=2)
    email: EmailStr
    message: str = Field(..., min_length=5, max_length=2000)
