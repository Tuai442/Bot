import pandas as pd

from Bot.App.Startegie.Strategy.fibonacci import Pattern

USER_CONFIGURATIONS_TEMPLATE = {
    "name": str(),
    "strategy-config": {
        "pattern-properties": {
            "ratio": list(),
            "bounce-margin": int(),

        },
        "bounce-margin": int,
    },
    "buy-risk": float,
    "stop-loss": float,
    "wallet": float,

}