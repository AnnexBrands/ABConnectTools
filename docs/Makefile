# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Serve documentation locally
serve:
	@echo "Serving documentation at http://localhost:8080"
	@echo "Press Ctrl+C to stop"
	cd $(BUILDDIR)/html && python -m http.server 8080

# Live rebuild and serve (requires sphinx-autobuild)
livehtml:
	@echo "Live serving documentation at http://localhost:8080"
	@echo "Documentation will auto-rebuild on changes. Press Ctrl+C to stop"
	sphinx-autobuild $(SOURCEDIR) $(BUILDDIR)/html --host 0.0.0.0 --port 8080

.PHONY: help serve livehtml Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)