.PHONY: pullgit local cleanup

pullgit:
	ansible-playbook --ask-become-pass -t pullCode site.yml
local:
	ansible-playbook --ask-become-pass -t useLocal site.yml
cleanup:
	ansible-playbook --ask-become-pass -t cleanup site.yml
