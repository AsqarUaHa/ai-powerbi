from typing import Protocol, Any


class AnthropicClient(Protocol):  # pragma: no cover - протокол для type-check
    async def messages_create(self, *args: Any, **kwargs: Any) -> Any: ...


class OpenAIClient(Protocol):  # pragma: no cover
    async def chat_completions_create(self, *args: Any, **kwargs: Any) -> Any: ...
