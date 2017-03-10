init:
	pip install -r requirements.txt
    
clean:
	rm -rf .cache
	rm -rf build
	rm -rf pip_services_runtime.egg-info
	rm -f pip_services_runtime/*.pyc
	rm -f pip_services_runtime/**/*.pyc
	rm -rf test/__pycache__
	rm -rf test/**/__pycache__
	
install:
	pip install -e .

.PHONY: test
test:
	py.test test -s

docgen:
	rm -rf build/doc
	sphinx-apidoc -f -e -o build/doc pip_services_runtime
	mv build/doc/modules.rst build/doc/index.rst
	rm -rf doc/api
	sphinx-build -b html build/doc doc/api -c .
