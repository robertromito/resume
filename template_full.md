---
geometry:
  - top=0.5in
  - bottom=0.5in
  - left=0.5in
  - right=0.5in
---

```{=latex}
{\centering
```
# Resume of {{ name }}
{{ location }} | {{ email }} | {{ linkedin }}
```{=latex}
\par}
```

{{ opening_statement }}

---

## Employment History

{% for job in experience %}

### {{ job.company }} [ {{ job.years }} ]

{% for role in job.roles %}

#### {{ role.title }}

{% for highlight in role.highlights %}

* {{ highlight }}

{% endfor %}
{% endfor %}
{% endfor %}

---

## Education
{% for e in education %}

* {{ e.degree }} [ {{ e.years }} ], {{ e.school }}, {{ e.location }}

{% endfor %}

---

## Technical Skills
