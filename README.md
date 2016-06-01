## Requirements:

* Raspberry Pi (any generation of)
* 20-30min of your time


# Step 1:

*Skip this if you already have Raspbian installed*

Start by installing Operating System on your Raspberry Pi. There are several tutorials for this, and I must say most of them are better then I would expect. I have found this two that I particularly like:

> Text form: https://www.andrewmunsell.com/blog/getting-started-raspberry-pi-install-raspbian/

> Video form: https://www.youtube.com/watch?v=oBmOymY7h1M

Please note, if you use "Noobs" install image - pick Raspbian **[Recommended]**.

I will presume you know how to discover local IP of your Raspberry and know how to SSH login into it.

It is possible that you will get an error related to your locale settings.
If you get this error and don't know how to solve it your self, simply execute the following command:

> `echo export LC_ALL=en_US.UTF-8 >> ~/.profile`

Then log out.

If that did not made locale problems go away, read this article: http://daker.me/2014/10/how-to-fix-perl-warning-setting-locale-failed-in-raspbian.html

# Step 2:

### Add official NuBox repository.

Open Terminal, copy paste following commands:

My GPG key for verification:

> `wget -O - http://peerbox.me/nubox/repo/nubox.gpg.key | sudo apt-key add -`

Repository:

> `sudo sh -c "echo 'deb http://peerbox.me/nubox/repo jessie main' >> /etc/apt/sources.list.d/nubox.list"`

# Step 3:

### Install NuBox.

Open Terminal, copy paste following commands:

> `sudo apt-get update && sudo apt-get install nubox`

While installing, you will be offered to rename the Raspberry Pi to "nubox", if you pick "y" or "yes" to confirm you will be able to find the machine on `nubox.local` address which eases using the NuBox via SSH.

# Step 4:

### Start and use NuBox.

NuBox is utilized via "nubox" command. Type "nubox -help" in terminal to see what it can do.

Start NuBox with:

> `nubox -start`

Now leave it for about 1 minute to start up and then check current status with:

> `nubox -info`

To autostart nubox (in case of frequent reboots for example) do:

> `nubox -autostart`

# Step 5:

### Minting.

If you have coins ready to mint, just unlock your wallet to start staking:
Code: [Select]

> `nubox -mint`

and enter your password.

_____________________

You can also use NuBox via Tor onion router:
NuBox can auto configure itself to become full node on Tor network.

Start NuBox via Tor:

> `nubox -tor`

If you want to autostart NuBox via Tor on reboot:

> `nubox -autostart tor`

This is usually a tad slower to connect to enough nodes but it should become a full node in about 10 minutes.

You can see what is your node's .onion address with:

> `nubox -onion`

# Optional steps:

Even though they are not yet implemented in `nubox` tool, NuBox has more tricks up it's sleeve.

For example, you can use graphical Nu client instead of nud command line daemon.

> `sudo systemctl start nu@pi.service`

`nubox` command will work properly with graphical client too, so you can still use it to monitor status.
But it is still not integrated with the rest of the system as much as nud is.
