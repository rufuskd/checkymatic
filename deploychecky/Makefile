.PHONY: pullgit local

pullgit:
	ansible-playbook --ask-become-pass -t pullCode site.yml
local:
	ansible-playbook --ask-become-pass -t useLocal site.yml
