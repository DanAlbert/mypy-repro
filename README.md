# Mypy crash repro case

This project is a minimal repro case for a mypy crash. The project is clearly
wrong because it is referring to types that have been deleted, but those are a
result of minimizing the repro case; when the project is fully functioning the
crash is still present.

The core of the issue might be that an automatic import done by an IDE caused
game.theater.frontline to import game.theater.missiontarget.MissionTarget from
game.theater.controlpoint instead of the module that defines it. That's the one
piece of the original project that does seem outright incorrect, and importing
the type from the correct module does fix the crash. In any case, mypy should
not crash.

However, removing _any_ line from this repro case will cause mypy to not crash,
so it seems to be more complicated than that.
