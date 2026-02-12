tags: #Linux #Bash 

TIL: the allowed login shells are in a only-writeable-by-root list in `/etc/shells`.

Some helper functions are available for reading this file, see `man getusershell`.

```C
#include <stdio.h>
#include <unistd.h>
int main(int ac, char **av)
{
	char *shell;
	while (1) {
		if((shell = getusershell()) == NULL) break;
		printf("%s\n", shell);
	}
	endusershell();
	return 0;
}
```

```
$ gcc test.c -o test
$ ./test
/bin/sh
/bin/bash
/usr/bin/bash
/bin/rbash
/usr/bin/rbash
/usr/bin/sh
/bin/dash
/usr/bin/dash
/usr/bin/screen
```

We use the mount --bind technique to override `/etc/shells` and see if `getusershell()` responds:

```
$ echo '/path/to/yomomma' > haha
$ sudo mount --bind haha /etc/shells
$ ./test
/path/to/yomomma
$ sudo umount /etc/shell
}
```

This might also be used to temporarily deny logins (even thru ssh) without disabling those services.
The check for the login shell just fails.
In dropbear, for example, see `initshells()` from compat.c.