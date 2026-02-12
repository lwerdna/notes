tags: #Linux 

KVM is a kernel virtual machine, a module for linux kernel that exposes /dev/kvm.

Do `lsmod | grep kvm` to see that it is loaded.

qemu is the actual virtualizer that uses KVM.

There is also a libvirt daemon running called libvirtd and can be enabled with `systemctl enable --now libvirtd`.

`virsh -c qemu:///system list --all` shows system VMs

`virsh -c qemu:///session list --all` shows my user VM

# Packages

* qemu-kvm - the main package
* libvirt - Includes the libvirtd server exporting the virtualization support
* libvirt-clients - This package contains virsh and other client-side utilities
* virtinst - contains `virt-install`, `virt-clone`
* virt-viewer - displays graphical console for a virtual machine
* virt-manager - package that has `virt-manager` utility

# Tasks

## copy or migrate a VM to another machine
Verify matching versions on each machine:
  kvm --version
  virsh shutdown foo
  virsh dumpxml foo > /path/to/foo.xml
  sudo virsh domblklist foo # locate qcow2 files

```
#compare:
du -h /var/lib/libvirt/images/foo.qcow2 # to
ls -l /var/lib/libvirt/images/foo.qcow2
# compress with:
tar --create --verbose --file ~/Downloads/foo.qcow2.tar.gz --gzip --sparse /var/lib/libvirt/images/foo.qcow2
# now copy .xml and .qcow2 files to other machine, then:
virsh define foo.xml
```

# Tools

## virsh "VIRtualization SHell"
Uses term "domain" for a virtual machine and its description.
`virsh list --all`
`virsh reboot vmname` to reboot
`virsh edit vmname`
`virsh dumpxml vmname`

## virt-manager
graphical, just run `virt-manager`

## virt-install
if root, disks go to `/var/lib/libvirt/images`
if user, disks go to `~/.local/share/libvirt/images`

