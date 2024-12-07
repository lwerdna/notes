KVM is a kernel virtual machine, a module for linux kernel that exposes /dev/kvm.

Do `lsmod | grep kvm` to see that it is loaded.

qemu is the actual virtualizer that uses kvm.

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

## copy a VM to another machine
`kvm --version` on both machines to verify match
`virsh shutdown vmname`
`virsh dumpxml vmname > /path/to/vmname.xml`
`sudo virsh domblklist vmname` to locate qcow2 files
compare `du -h path_to_qcow` with `ls -l path_to_qcow` ... sparse storage is at play
compress with:
`tar --create --verbose --file ./vmdrive.qcow2.tar.gz --gzip --sparse ~/path/to/vmdrive.qcow2`
copy .xml and .qcow2 files to other machine...

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

