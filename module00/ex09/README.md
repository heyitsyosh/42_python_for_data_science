<h1 align="center">
	My first python package
</h1>

# Build and install
## Method 1 - Install directly from source
``` 
pip install .
```

## Method 2 - Build and install a distribution
```
python -m build
```
```python
# Install one of the generated files:
pip install dist/ft_package-0.0.1-py3-none-any.whl   # wheel
pip install dist/ft_package-0.0.1.tar.gz             # sdist
```
