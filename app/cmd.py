import asyncio
import signal
import typing as t
from functools import wraps

import click
from loguru import logger

from app.services.service import application_dependencies, beth_service

T = t.TypeVar("T")
P = t.ParamSpec("P")


def coro(f: t.Callable[P, T]) -> t.Callable[P, T]:
    @wraps(f)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        logger.info("run_cmd", command=f.__name__)
        return asyncio.new_event_loop().run_until_complete(
            t.cast(t.Coroutine[t.Any, t.Any, T], f(*args, **kwargs))
        )

    return wrapper


@click.group()
def cli() -> None:
    ...


def handle_exit_signal(_sig, _frame) -> t.NoReturn:
    raise SystemExit


@click.command()
@coro
async def run_parser() -> None:
    async with application_dependencies():
        await beth_service.process()


cli.add_command(run_parser)
signal.signal(signal.SIGINT, handle_exit_signal)
signal.signal(signal.SIGTERM, handle_exit_signal)

if __name__ == "__main__":
    cli()
