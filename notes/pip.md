List files in package: `pip show -f <package>`

Install specific version: `pip install unicorn==1.0.2rc4`

Upgrade a package: `pip cache purge; pip install numpy --upgrade`

## publishing

authoritative how-to: https://packaging.python.org/tutorials/packaging-projects/

* **package** - collection of modules
* `__init__.py` makes python treat the containing directory as a package
* A.B.C.D is package A, **subpackage** B, subpackage C, module D and all-together A.B.C.D is a **submodule**
* `sound.effects.echo.echofilter(arg0, arg1)` has **package prefix** `sound.effects` and module `echo`
* in the `from package import item` item can be module, package, class, function, variable
* in the `import A.B.C` form, C can be a module or package, but not a class, function, variable
* the `__all__` variable in `__init.py__` controls what module names are imported when the user does `from foo import *`

* submodules importing from neighboring submodules? see `6.4.2. Intra-package References`
