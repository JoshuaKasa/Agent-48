# **Description**
Agent 48 is a simple Malware written in Python that overwrites your MBR (Master Boot Record).</br>

It is very effective, since the user will have no time to try and kill the task.</br>
In fact if the task is killed the computer will shut down and the MBR will be overwritten

# **How it works**
THIS IS FOR EDUCATIONAL PURPOSES ONLY, this is NOT a joke, don't prank your friends with this, don't try it yourself.

Agent 48 uses the win32 modules for getting access to the main windows functions and files.</br>
When opening the Batch file, the .exe file (not in the repository) will be runned as a administrator, and the MBR will immediately be overwriten, so that the user will not be able to shut down the PC.

After the MBR is overwriten a YouTube link with the song "What a Wonderful World by Louis Armstrong" will be opened and a 3 minute timer will start.</br>
This at least gives the user a short amount of time for saving all of his important files.

When the 3 minutes timer runs out, the PC will be shutdown and when turned on again it will display a missing disc error. In simple words, this happens because the MBR bytes have been overwriten with the Python code.</br>
The error is not custom, but that can be done pretty easily by getting every byte inside the MBR and overwriting the one you want with some words.
