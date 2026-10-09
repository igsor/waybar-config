#!/usr/bin/python
import csv
import subprocess
from collections.abc import Set as AbstractSet
from typing import Final

_SHELL_ENCODING: Final[str] = "UTF-8"


def main() -> None:
    current_sink = _get_current_sink()
    sinks = sorted(_get_all_sinks())
    assert sinks, "expected at least one sink"
    next_sink = sinks[(sinks.index(current_sink) + 1) % len(sinks)]
    _set_sink(next_sink)


def _get_current_sink() -> str:
    return _run_shell_command("pactl", "get-default-sink").strip()


def _get_all_sinks() -> AbstractSet[str]:
    return frozenset(
        sink["name"]
        for sink in csv.DictReader(
            _run_shell_command("pactl", "list", "short", "sinks").split("\n"),
            fieldnames=("id", "name", "provider", "channels", "state"),
            delimiter="\t",
        )
    )


def _set_sink(sink: str) -> None:
    _run_shell_command("pactl", "set-default-sink", sink)


def _run_shell_command(
    command: str, /, *arguments: str, encoding: str = _SHELL_ENCODING
) -> str:
    return subprocess.run(
        [command, *arguments], check=True, stdout=subprocess.PIPE
    ).stdout.decode(encoding)


if __name__ == "__main__":
    main()
