"""Register only the upstream PPM ays_30+ scheduler, without other PPM hooks."""

import logging

import comfy.samplers

from .upstream_schedulers import CUSTOM_HANDLERS


def register_scheduler():
    name = "ays_30+"
    if name not in comfy.samplers.SCHEDULER_HANDLERS:
        comfy.samplers.SCHEDULER_HANDLERS[name] = CUSTOM_HANDLERS[name]
    # Extend in place: existing KSampler / Efficiency Nodes references stay valid.
    for names in (comfy.samplers.SCHEDULER_NAMES, comfy.samplers.KSampler.SCHEDULERS):
        if name not in names:
            names.append(name)
    logging.info("[AYS30+] Registered ays_30+ (ComfyUI-ppm, 99165b6eb6e1)")


register_scheduler()

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
