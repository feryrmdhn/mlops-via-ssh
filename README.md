# MLops Fastapi Deployment

Setup CI/CD and docker

Create new folder in root .github/workflows then create new file <i>build-and-deploy.yml</i> (like this repo)<br/>
Create dockerfile (like this repo)

### Register Cloud Server
<ul>
    <li>Create <strong>Digital Ocean</strong> Account</li>
    <li><i>The first User will get $200 free for 2 months, but just pay for the cheapest plan of $5 at the start</i></li>
    <li>Generate and save <code>DIGITALOCEAN_ACCESS_TOKEN</code> in notes/notepad</li>
    <li>Create Droplets</li>
    <li>Choose server location. Ex: Singapore</li>
    <li>Choose plan</li>
    <li>Insert SSH key <i>.pub</i> using format <code>ed25519</code> (see setup local in next step)</li>
    <li>Submit/Save</li>
</ul>

### Setup local
<ul>
    <li>Open terminal</li>
    <li>Create SSH <code>ssh-keygen -t ed25519 -a 200 -C "example@email.com"</code></li>
    <li>There is 2 file <code>id_ed25519</code> as private key and <code>id_ed25519.pub</code> as public key</li>
    <li><strong>cd ~/.ssh</strong></li>
    <li>Set permission type <code>chmod 600 id_ed25519</code></li>
    <li>Copy <code>cat id_ed25519.pub | pbcopy</code> (on Mac) and paste into SSH key Digital Ocean</li>
</ul>

### Setup Digital Ocean UI
<ul>
    <li>Create Container Registry</li>
    <li>Copy path into <code>build-and-deploy.yml</code> Ex: <i>registry.digitalocean.com/dibimbing</i> Dont use (-,*_.)</li>
    <li>Create image, change the name, and copy into <code>build-and-deploy.yml</code></li>
</ul>

### Acces server from local
<ul>
    <li>Run <code>ssh root@ip_address_droplet_v4</code></li>
    <li><code>ls ~/.ssh</code></li>
    <li>There is file <strong>authorized_keys</strong></li>
    <li><code>nano authorized_keys</code> insert value id_ed25519.pub</li>
    <li>Close <code>ctrl + x</code> then <code>Y</code> then enter</li>
    <li>Back to directory <code>cd ..</code></li>
</ul>

### Install Docker
<ul>
    <li>Follow this guide <a href="https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04">Here</a> just follow step 1 (step 2 optional)</li>
    <li>Ensure docker is active <code>sudo systemctl status docker</code></li>
    <li>ctrl + x</li>
    <li>Type <code>exit</code> to exit from server</li>
</ul>

### Setup env github
<ul>
    <li>Select repository</li>
    <li>Go to <code>settings -> secrets and variables -> actions</code></li>
    <li>Create new repository secrets</li>
    <li><code>DIGITALOCEAN_ACCESS_TOKEN</code> is Digital Ocean Access Token that saved in notes/notepad</li>
    If forget see at sidebar <code>API -> Tokens</code>
    <li><code>HOST</code> is host ipv4 droplets, ex: 167.99.64.00</li>
    <li><code>SSH_KEY</code> is private key id_ed25519 from local</li>
    <li><code>USERNAME</code> just insert root</li>
    <li>Commit the project then push</li>
    <li>Check Actions menu on github</li>
</ul>
