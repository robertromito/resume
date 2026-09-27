# Rob's Resume Renderer

This is the project for managing my resume, which has several forms:

- An ATS friendly version with all of my experience and skills, in PDF and docx format. The layout is simple, comprised of headings and bullets.

- A visually focused version which contains my most recent experience, a grid of my technical skills over time, and a summary of my non technical skills.  This version is rendered as a PDF

- A static html version which is a combination of the visual version and the ATS version, sprinkled with some interactivity

## Resume Components

The resume versions mentioned above are ultimately different combinations and layouts of the following sections:

- A *Recent Experience* section which highlights my most current experience, projects, and accomplishments. It's designed to fit on one page.

- A *Complete Experience* section which contains name, dates, and highlights for all of my jobs and projects.

- A *Technical Skills Timeline* section which is a grid showing my technical skill history over time, across several skill categories. This section will fit on one page and will be relatively dense.

- A **Working with Rob** section which is a narrative about my non-technical contributions. The content is limited to a single page and will contain a decent amount of whitespace

## System Design

My main goal with this system is to eliminate duplication as much as possible while being able to render different resume versions and formats. I accomplish this using the following approaches:

- My personal details, experience, and skill are defined once in yaml data files.
  - I am keeping sqlite open as a future option for the data componenets.

- Markdown is used as much as possible for the different resume components.

- Python and Jinja is used for rendering complete markdown and static html versions.

- Pandoc is used to render pdf, ODT, and docx formats.

For advanced layout, the template_*.md files use raw LaTeX codes that pandoc reads when producing the final output.

## Limits / Exclusions

While this project will handle producing the primary versions of my resume, the following aspects are out of scope (at least for now):

- Cover letters.

- Integration with career sites like LinkedIn and Indeed.
