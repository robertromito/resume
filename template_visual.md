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

```{=latex}
{\centering
```
## Recent Experience
```{=latex}
\par}
```
{% for job in experience %}
{% if job["recency"] in ["most_recent", "recent"] %}
```{=latex}
{\centering
```
### {{ job.company }} [ {{ job.years }} ]
```{=latex}
\par}
```
```{=latex}
\begin{minipage}[t]{0.48\textwidth}
```
```{=latex}
{\centering
```
### Roles
```{=latex}
\par}
```
{% for role in job.roles %}
#### {{ role.title }}
{% for highlight in role.highlights %}
* {{ highlight }}
{% endfor %}
{% endfor %}

```{=latex}
\end{minipage}
\begin{minipage}[t]{0.48\textwidth}
```
```{=latex}
{\centering
```
### Notable Accomplishments
```{=latex}
\par}
```
{% for a in job["accomplishments"] %}
* {{ a }}
{% endfor %}
```{=latex}
{\centering
```
### Key Technical Skills
```{=latex}
\par}
```
{% for skill in job["key_skills"] %}
* {{ skill }}
{% endfor %}
```{=latex}
\end{minipage}
\medskip
```
{% endif %}
{% endfor %}

---

```{=latex}
{\centering
```
## Education
{% set e = education[0] %}
### {{ e.degree }} [ {{ e.years }} ]
{{ e.school }}, {{ e.location }}
```{=latex}
\par}
```

\break

## Technical Skills

My skills
