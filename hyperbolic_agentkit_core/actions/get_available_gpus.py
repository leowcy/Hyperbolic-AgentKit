import requests
import json
from typing import Optional

from collections.abc import Callable

from pydantic import BaseModel, Field

from hyperbolic_agentkit_core.actions.hyperbolic_action import HyperbolicAction
from hyperbolic_agentkit_core.actions.utils import get_api_key

GET_AVAILABLE_GPUS_PROMPT = """
This tool will get all the available GPUs on the Hyperbolic platform.

It does not take any following inputs

Important notes:
- Authorization key is required for this operation
- The GPU prices are in USD cents per hour
"""


class GetAvailableGpusInput(BaseModel):
  """Input argument schema for getting available GPUs."""


def get_available_gpus() -> str:
  """
  Returns a string representation of the response from the Hyperbolic API.
  Returns:
    A string representing the response from the API.
  """
  # Get API key from environment
  api_key = get_api_key()

  url = "https://api.hyperbolic.xyz/v1/marketplace"
  headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
  }
  data = {"filters": {}}
  response = requests.post(url, headers=headers, json=data)
  return response.json()


class GetAvailableGpusAction(HyperbolicAction):
  """Get available GPUs action."""

  name: str = "get_available_gpus"
  description: str = GET_AVAILABLE_GPUS_PROMPT
  args_schema: type[BaseModel] | None = GetAvailableGpusInput
  func: Callable[..., str] = get_available_gpus
