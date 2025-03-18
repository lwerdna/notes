## Load an assembly from file:

```c#
using System.Reflection; // for class Assembly

// in mono repl:
LoadAssembly("foo.exe"); // in mono repl
    
// using reflection:
using System.Reflection;
Assembly.LoadFile("/path/to/foo.exe");
```

## Load an assembly from bytes

```c#
// read bytes
var assembly = Assembly.Load(bytes);
```

## Get Classes In Assembly

```c#
var foo = Assembly.LoadFile("/path/to/foo.exe");
foo.GetTypes()

```

