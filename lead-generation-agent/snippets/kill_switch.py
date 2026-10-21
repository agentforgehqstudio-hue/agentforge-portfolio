"""Simplified example written for this showcase (not the production code).

The kill switch: paid calls only happen while LEADGEN_ENABLED is exactly "true".
Anything else ("TRUE", "yes", missing) counts as off, so a typo can never spend money.
"""
import os


def enabled() -> bool:
    return os.environ.get("LEADGEN_ENABLED", "") == "true"


def paid_call(do_call):
    if not enabled():
        raise RuntimeError("Paused: LEADGEN_ENABLED is not 'true'.")
    return do_call()
