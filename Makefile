
all: rebuild
	
	

rebuild:
	./lightning rebuild
	

show:
	./lightning show

deploy: unipi hpc

unipi:
	cp content/unipi.yaml content/site.yaml
	make rebuild
	rsync -e "ssh" -rca www/* ceccarel@osiris.di.unipi.it:~/public_html


hpc:
	cp content/hpc.yaml content/site.yaml
	make rebuild
	rsync -e "ssh" -rca www/* ceccarelli@pomino.isti.cnr.it:~/public_html

		
