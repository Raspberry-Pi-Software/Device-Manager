# Device Manager
A Simple Device Manager For Managing Devices On Your Raspberry Pi (supported model)
> ⚠️ Device Manager runs on a **Python 3.11 or later** installation. Make sure your Python installation is up to date!

> ✖️ If you have any problems or issues while *installing and initializing on a **supported model***, make an issue [here](https://github.com/Raspberry-Pi-Software/Device-Manager/issues).

Device Manager is made in Qt. It is an easy way to manage devices, update drivers, mount/unmount disks and more! It's backend is written in Bash and it's frontend is written in Python. It's backend is initialised by a service file which executes this (`rpisft exec device-manager --executor=backend <command>`) command for the frontend to communicate with it.


# Use The Device Manager
## In package tool:
Use this command to install Device Manager onto your Pi using the Package Tool:
```bash
rpisft install device-manager
```
Use this command to uninstall Device Manager from your Pi using the Package Tool:
```bash
rpisft uninstall device-manager
```
## In Terminal (manual install)
Use this command to install the device manager tool onto your Pi:
```bash
git clone https://github.com/Raspberry-Pi-Software/Device-Manager && cd Device-Manager && sudo bash post-install;
```
Use this command to remove the device manager tool from your Pi:
```bash
cd Device-Manager && sudo bash uninstall;
```
The usage for this tool is:
```bash
rpisft exec device-manager
```
This command will open the client UI for device manager. __***There is no way to open a Device Manager session without the Qt UI initialised.***__
