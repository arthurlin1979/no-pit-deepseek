"""Idempotently put Arthur's DS4 settings back into maya-ds4.json.

A Maya update or `./maya.sh --setup` rewrites the config and can drop keys it
does not know (see upstream issue #1089), so this is run by reapply.sh.
"""
import json
import time

PATH = "maya-ds4.json"

WANT_ENV = {
    "MAYA_DS4_SLOT_KEEP": "1",
    "MAYA_DS4_SLOT_RAM_GB": "32",
    "MAYA_DS4_SLOT_CAP": "8",
    "MAYA_DS4_PREFIX_KEEP": "4",
    "MAYA_DS4_PREFIX_GB": "8",
    "MAYA_DS4_KEEP_THINKING": "1",
}
WANT_TOP = {"thinking_budget": 2048, "reasoning_effort": "low"}

cfg = json.load(open(PATH))
before = json.dumps({k: cfg.get(k) for k in WANT_TOP} | {"env": cfg.get("env")}, ensure_ascii=False, sort_keys=True)

env = dict(cfg.get("env") or {})
env.update(WANT_ENV)
cfg["env"] = env
cfg.update(WANT_TOP)

# abliteration on by default (the direction file is in "args")
_args = cfg.get("args") or []
if "--ablate-default" in _args:
    _args[_args.index("--ablate-default") + 1] = "on"
else:
    _args += ["--ablate-default", "on"]
cfg["args"] = _args  # ABLATE_DEFAULT

after = json.dumps({k: cfg.get(k) for k in WANT_TOP} | {"env": cfg.get("env")}, ensure_ascii=False, sort_keys=True)
if before != after:
    open(PATH + time.strftime(".bak-%Y%m%d-%H%M"), "w").write(json.dumps(json.load(open(PATH)), ensure_ascii=False, indent=2))
json.dump(cfg, open(PATH, "w"), ensure_ascii=False, indent=2)
print("   config:", after)
