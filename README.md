# unam-settings
Settings app for Unam Session

# How to use
1. Make folder /usr/share/unam OS/Apps/unam settings

```shell
sudo mkdir /usr/share/unam\ OS /usr/share/unam\ OS/Apps /usr/share/unam\ OS /Apps/unam\ settings
```

2. Copy glade and python file to the new folder, along with the image 

```shell
sudo cp -a full-logo.png /usr/share/unam\ OS/Apps/unam\ settings
sudo cp -a unam-settings.py /usr/share/unam\ OS/Apps/unam\ settings
sudo cp -a unam-settings.glade /usr/share/unam\ OS/Apps/unam\ settings
```

3. Move script to /usr/bin

```shell
sudo mv unam-settings-3 /usr/bin/unam-settings
```

4. Add execution privileges to unam-settings
```shell
sudo chmod +x /usr/bin/unam-settings
```

### unam-settings in action

![us](https://github.com/Unam-OS/unam-settings/blob/master/Screenshot%2027-04-2017-14_19_23.png?raw=true)

![us-2](https://github.com/Unam-OS/unam-settings/blob/master/Screenshot%2027-04-2017-14_19_23.png?raw=true)
