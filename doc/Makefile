# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = python-skel
SOURCEDIR     = src
BUILDDIR      = .

# Subdirectories of the source directory that are supposed to be there
# but that may be empty and may thus be missing after a git checkout.
STATIC_SOURCEDIRS = $(SOURCEDIR)/_static $(SOURCEDIR)/_templates


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

$(STATIC_SOURCEDIRS):
	mkdir $@

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: $(STATIC_SOURCEDIRS) Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile
