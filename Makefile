
# Variables
VENV           = ./venv
DIST           = ./dist
SYSTEM_PYTHON  = $(shell which python)
PYTHON         = $(VENV)/bin/python
PYTHONC        = $(VENV)/bin/python -m py_compile 
SHELL          := /bin/bash

PYTHON_SRC  =  ./src/turing_machine
PYTHON_SRCS = $(shell find $(PYTHON_SRC) -name '*.py')
PYTHON_OBJS = $(PYTHON_SRCS:.py=.pyc)
PYTHON_ENTRY_POINT = $(PYTHON_SRC)/main.py
PYTHON_PROJECT_SRC = $(shell pwd)/src
PYTHON_PROJECT_NAME = turing_machine

CSRC = ./src 
CBUILD =  ./build

all : 	help
	@#

$(VENV): requirements.txt
	@$(SYSTEM_PYTHON) -m venv $@
	@$(PYTHON) -m pip install --upgrade pip
	@$(PYTHON) -m pip install -r requirements.txt
	@cd venv/lib/*; cd site-packages; echo $(PYTHON_PROJECT_SRC) > $(PYTHON_PROJECT_NAME).pth

# Rules
%.pyc : %.py 
	@$(PYTHON) -m compileall -b -o 2 $<

# Commands
.PHONY: install clean run build python help c

#: Installs the python virtualenv
install: $(VENV)

#: Cleans the workspace
clean:
	@# Help: Cleans the project
	@rm -rf $(VENV) $(DIST) $(PYTHON_OBJS) *.egg-info 
	@find . -name "__pycache__" | xargs rm -rf

#: Runs the application
run: $(VENV)  
	@$(PYTHON) $(PYTHON_ENTRY_POINT)

#: Builds the work space
build: $(VENV)
	@$(PYTHON) -m build --outdir $(DIST)

#: Shows the variables		
info:	
	@echo PYTHON_SRCS = $(PYTHON_SRCS)
	@echo PYTHON_OBJS = $(PYTHON_OBJS)
	@echo SYSTEM_PYTHON = $(SYSTEM_PYTHON)	
	@echo PYTHON = $(PYTHON)	

#: Runs python command in the virtualenv
python:
	$(PYTHON)	

#: Buikds the c project
c:
	@cmake -S $(CSRC) -B $(CBUILD)
	@cmake --build $(CBUILD)

#: Generate list of targets with descriptions                                                                
help:                                                                                                                    
	@grep -B1 -E "^[a-zA-Z0-9_-]+\:([^\=]|$$)" Makefile \
     | grep -v -- -- \
     | sed 'N;s/\n/###/' \
     | sed -n 's/^#: \(.*\)###\(.*\):.*/\2###\1/p' \
     | column -t  -s '###'
