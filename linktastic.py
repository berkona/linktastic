
import subprocess
import logging
import os


logging.basicConfig()
logger = logging.getLogger(__name__)


# Private function to create link on nt-based systems
def _link_windows(src, dest):
	subprocess.call(['cmd', '/C', 'mklink', '/H', dest, src], stdout=subprocess.PIPE)

	stdout, stderr = subprocess.PIPE.communicate()

	# TODO, find out what kind of messages Windows sends us from mklink
	logger.info(stdout)
	logger.info(stderr)


def _symlink_windows(src, dest):
	subprocess.call(['cmd', '/C', 'mklink', dest, src], stdout=subprocess.PIPE)

	stdout, stderr = subprocess.PIPE.communicate()

	# TODO, find out what kind of messages Windows sends us from mklink
	logger.info(stdout)
	logger.info(stderr)


# Create a hard link to src named as dest
# This version of link, unlike os.link, supports nt systems as well
def link(src, dest):
	if os.name == 'nt':
		_link_windows(src, dest)
	else:
		os.link(src, dest)


# Create a symlink to src named as dest, but don't fail if you're on nt
def symlink(src, dest):
	if os.name == 'nt':
		_symlink_windows(src, dest)
	else:
		os.symlink(src, dest)
