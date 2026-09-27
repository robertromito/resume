# Rob's Resume Renderer System

## Data Files

The following data files will always be managed by hand. Never attempt to change them:

- data_profile.yml holds name, email, links, personal statements, etc

- data_experience.yml holds work experience with the following data structure:
```
experience:
  - company: The company name
    type: (FTE | Contract)
	years: start year - end year
	recency: (most_recent | recent | old)
	roles:
	  - title: The role title
	    highlights:
		  - list of highlights that will use yaml multiline block scalars
    skills:
	  - list of skills that will use yaml multiline block scalars
```

- data_skills.yml holds skill experience detached from employment experience. The data represents skills overtime grouped by categories
```
skills:
  - <year>:
    - languages_frameworks:
	  - list of programming language and programming framework skills. e.x. C#, Java, Spring, React, FastAPI
	- testing:
	  - test automation
	- data:
	  - database platforms
	- infrastructure:
	  - cloud, on-prem, virual
	- tools:
	  - scm, AI, editors, OS
```

## General

- In any list, the earlier items represent more current/stronger skills
