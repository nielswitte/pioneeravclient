## XBMC Pioneer AV control

Forked from https://github.com/encinas/pioneeravclient. To allow basic control of your Pioneer AV from XBMC.
For example change the volume while using passthrough.

1. Checkout or download and unzip this repository to you `/storage` directory of XBMC
2. Change the values in config.py to match your situation
3. Update your XBMC keymap to use the functions
4. Start XBMC and now you can use 2 for raising the volume, 5 for muting/unmuting and 8 for lowering the volume.

### Keymap
Put the following code in `/storage/.xbmc/userdata/keymaps/remote.xml`. Create the file if it does not exist yet.

```xml
<keymap>
  	<global>
    	<remote>
    		<two>RunScript(/storage/pioneeravclient/volume_up.py)</two>
    		<five>RunScript(/storage/pioneeravclient/volume_mute.py)</five>
    		<eight>RunScript(/storage/pioneeravclient/volume_down.py)</eight>
    	</remote>
    </global>
</keymap>	
```

## Python client to remotely control a Pioneer AV

### Supported devices
The following devices are known to work. Others may work as well, but require some modifications to the `__init__.py` file

 * VSX-527
 * VSX-528
 * VSX-822
 * VSX-921
 * VSX-1023

### Source
 * Original source code: https://github.com/encinas/pioneeravclient
 * Free software: BSD license
 * Documentation: http://pioneeravclient.rtfd.org.