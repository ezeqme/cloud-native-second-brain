---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Clément Nussbaumer", "PostFinance"]
sched_url: https://kccnceu2025.sched.com/event/1tx78/day-2000-migration-from-kubeadm+ansible-to-clusterapi+talos-a-swiss-banks-journey-clement-nussbaumer-postfinance
youtube_search_url: https://www.youtube.com/results?search_query=Day-2%E2%80%99000+-+Migration+From+Kubeadm%2BAnsible+To+ClusterAPI%2BTalos%3A+A+Swiss+Bank%E2%80%99s+Journey+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Day-2’000 - Migration From Kubeadm+Ansible To ClusterAPI+Talos: A Swiss Bank’s Journey - Clément Nussbaumer, PostFinance

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Clément Nussbaumer, PostFinance
- Schedule: https://kccnceu2025.sched.com/event/1tx78/day-2000-migration-from-kubeadm+ansible-to-clusterapi+talos-a-swiss-banks-journey-clement-nussbaumer-postfinance
- Busca YouTube: https://www.youtube.com/results?search_query=Day-2%E2%80%99000+-+Migration+From+Kubeadm%2BAnsible+To+ClusterAPI%2BTalos%3A+A+Swiss+Bank%E2%80%99s+Journey+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Day-2’000 - Migration From Kubeadm+Ansible To ClusterAPI+Talos: A Swiss Bank’s Journey.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx78/day-2000-migration-from-kubeadm+ansible-to-clusterapi+talos-a-swiss-banks-journey-clement-nussbaumer-postfinance
- YouTube search: https://www.youtube.com/results?search_query=Day-2%E2%80%99000+-+Migration+From+Kubeadm%2BAnsible+To+ClusterAPI%2BTalos%3A+A+Swiss+Bank%E2%80%99s+Journey+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uQ_WN1kuDo0
- YouTube title: Day-2’000 - Migration From Kubeadm+Ansible To ClusterAPI+Talos: A Swiss Bank’s... Clément Nussbaumer
- Match score: 0.959
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/day-2000-migration-from-kubeadm-ansible-to-clusterapi-talos-a-swiss-ba/uQ_WN1kuDo0.txt
- Transcript chars: 25120
- Keywords: cluster, clusters, existing, control, create, secrets, little, provision, everything, machine, actually, management, migration, cubadm, command, encryption, replica, machines

### Resumo baseado na transcript

She's a farmer and with her family and so I get to see cows every day and then I get to play with Kubernetes uh during the day as well. Uh so let's get started with this session about our migration from Cubadium, Cubadom. So that's that's a little about what we do at post finance and with Kubernetes and cloud native technologies. But uh so cluster API in a few words, cluster API, the idea is that you have you use the declarative APIs of Kubernetes to provision and to make your cluster work. So you will configure the network card the storage you will configure everything with this declarative API and forest that's that's a game changer. you will see an issuer field and this issuer per default is kubernetes defaults services cluster local and with stalos this is not the case with stalos they default to the end points of the cluster so you have to match that on the old

### Excerpt da transcript

Hi everyone. I'm glad to be here today. My name is Clemon Bame. I come from Switzerland. I'm a Swiss software engineer working at Post Finance. And fun fact, I live on a farm with my wife. She's a farmer and with her family and so I get to see cows every day and then I get to play with Kubernetes uh during the day as well. So I'm a lucky guy. Uh so let's get started with this session about our migration from Cubadium, Cubadom. I'm not sure how you pronounce that. I will use Cubadium and towards cluster API and Telos. So how old can your clusters get? Our oldest clusters will soon turn six years old and today it is now 299 days old which gives you the title for this for for this session. Actually uh why do we bother with keeping cluster alive for so long? Why don't we always recreate new clusters and move application there? For us, the choice is uh due to the way we work with our clusters, we use quite large shared clusters on which there are lots of name spaces for lots of application developer teams.

So instead of moving 500 application teams to a new clusters to new clusters everyone every time there's a new release, we prefer to just update and upgrade the clusters in in place. And up up until now we've been quite successful with that uh with Cubadm so far. Um, Post Finance, Post Finance is a small bank or small it it's a it's a bank in Switzerland. Uh, we run uh 35 vanilla Kubernetes cluster. So, the open source distribution, we just use Cubadn Cubadm to to configure everything and run the the multiple components of Kubernetes. As I said, the oldest cluster will soon turn six years old. We run all we run all of that on two on-prem data centers. uh we do visual v virtualization and then we create the virtual machines that we need for our nodes. Uh we run chaos monkey on all clusters. This is might be a fun fact but it's really helpful for us because up to the production clusters where we run the card payment services we run chaos monkey and this helps us a lot when we have to do an an upgrade because the application have to be able to withstand a pod restart.

So that's that's a little about what we do at post finance and with Kubernetes and cloud native technologies. That being said, uh let me explain how we currently provision our clusters the starting point. So for now we provision uh DBN VMs with Terraform and we boot those VMs on on our on prem clouds on vSphere. Then we run a little a series of puppet configuration. Not sure how many of you know
