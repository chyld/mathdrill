# Math Drill

### Systemd Configuration

Check services

`systemctl --type=service --no-pager`

Create service file

`sudo vi /etc/systemd/system/mathdrill.service`

Enable service start on reboot

```
sudo systemctl enable mathdrill
sudo reboot
```

If you check status, it will say "exited". Check docker.

`docker ps`
