from fastapi.testclient import TestClient
import torch
import numpy as np
import pytest
import sys
import os
from httpx import AsyncClient
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))+"/backend")

from app.api import *

client = TestClient(app)

## 함수가 test로 시작되어야 함!
@pytest.mark.asyncio
async def test_inference():
    async with AsyncClient(base_url="https://fast-api-backend-nzhkc6v44a-du.a.run.app") as ac:
        with open(os.path.join(os.path.dirname(__file__),"test_img.jpg"), "rb") as x:
            response = await ac.post("/inference",files={'files': x})
            assert response.status_code == 200
            assert type(response.json())==int
            assert 0<=response.json()<5