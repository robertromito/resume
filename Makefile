build:
	mkdir -p dist
	./generate.py
	cd dist/ && \
	pandoc resume_full.md -o resume_full.pdf && \
	pandoc resume_visual.md -o resume_visual.pdf

clean:
	rm -f dist/*

.PHONY: build clean
