#!/usr/bin/env python

import yaml
from jinja2 import Template

data = {}

for data_file in ["profile", "experience", "skills"]:
    with open(f"data_{data_file}.yml", encoding="utf-8") as f:
      data.update(yaml.safe_load(f) or {})

for version in ["full", "visual"]:
  with open(f"template_{version}.md", encoding="utf-8") as f:
    template = Template(f.read())
  with open(f"dist/resume_{version}.md", "w", encoding="utf-8") as f:
    f.write(template.render(**data))
