---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Customizing + Extending Kubernetes"
themes: ["GitOps Delivery", "Kubernetes Core"]
speakers: ["Kim Schlesinger", "DigitalOcean"]
sched_url: https://kccnceu2022.sched.com/event/yto4/gitops-to-automate-the-setup-management-and-extension-a-k8s-cluster-kim-schlesinger-digitalocean
youtube_search_url: https://www.youtube.com/results?search_query=GitOps+to+Automate+the+Setup%2C+Management+and+Extension+a+K8s+Cluster+CNCF+KubeCon+2022
slides: []
status: parsed
---

# GitOps to Automate the Setup, Management and Extension a K8s Cluster - Kim Schlesinger, DigitalOcean

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Kim Schlesinger, DigitalOcean
- Schedule: https://kccnceu2022.sched.com/event/yto4/gitops-to-automate-the-setup-management-and-extension-a-k8s-cluster-kim-schlesinger-digitalocean
- Busca YouTube: https://www.youtube.com/results?search_query=GitOps+to+Automate+the+Setup%2C+Management+and+Extension+a+K8s+Cluster+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre GitOps to Automate the Setup, Management and Extension a K8s Cluster.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yto4/gitops-to-automate-the-setup-management-and-extension-a-k8s-cluster-kim-schlesinger-digitalocean
- YouTube search: https://www.youtube.com/results?search_query=GitOps+to+Automate+the+Setup%2C+Management+and+Extension+a+K8s+Cluster+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rra7TkYOnko
- YouTube title: GitOps to Automate the Setup, Management and Extension a K8s Cluster - Kim Schlesinger, DigitalOcean
- Match score: 0.902
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/gitops-to-automate-the-setup-management-and-extension-a-k8s-cluster/rra7TkYOnko.txt
- Transcript chars: 61450
- Keywords: flux, cluster, sealed, secrets, terraform, create, command, digitalocean, github, secret, called, created, provider, control, workshop, repository, account, chapter

### Resumo baseado na transcript

hey good morning everybody thank you so much for being here so this session is called gitops to automate the setup management and extension of a kubernetes cluster and i'm going to talk about how the session is going to be structured and how we might need to move around a little bit in the room but first my name is kim schlesinger i am a developer advocate at digitalocean i focus on our kubernetes education and prior to digital ocean i was a site reliability engineer at a company this workshop but you select the size of the nodes i've picked a basic amd droplet with 2 v cpus and 4 gigs of ram and then you specify whether or not you want those nodes to auto scale and then you say the minimum

### Excerpt da transcript

hey good morning everybody thank you so much for being here so this session is called gitops to automate the setup management and extension of a kubernetes cluster and i'm going to talk about how the session is going to be structured and how we might need to move around a little bit in the room but first my name is kim schlesinger i am a developer advocate at digitalocean i focus on our kubernetes education and prior to digital ocean i was a site reliability engineer at a company called fairwinds and i'm actually a career changer so before all of that i was a primary school teacher and i was an instructional coach and curriculum designer so i like bringing tech and education together and what we're going to be doing today is uh i've created a repo for you that we're going to be working through so let's take a look at this so this is the repo there are five chapters in the repo and the goal of this workshop is for you to have some experience getting like an aha moment either with infrastructure as code or with git ops and so if you look through the chapters you see the first chapter is we're going to set up a cluster using terraform the next thing that we'll do is we'll install and set up flux cd for continuous delivery the next thing is that we'll use a project called seal secrets to encrypt kubernetes secrets so that you can store your secrets in a public git repo the next thing that we'll do is we'll use a project called crossplane to make the cluster that we've spun up a universal control plane so that we can create other cloud resources from within that cluster and then finally we'll tear down our cluster um so if you're using a cloud provider like digitalocean that you don't get charged for any usage that you want don't don't want to be charged for and so i know that workshops are really tricky and my goal is for you to have an experience but the internet can be really unreliable at this venue uh and so here's how we're gonna do this um so if you are someone who is interested in watching me do a demo of all of this and you maybe wanna follow along or you just wanna observe then uh in a few moments i'm going to invite you to move toward the front of the room so we might need to shift if you're someone who's sitting in the audience and you're thinking i already know a little bit of this like maybe i'm already familiar with terraform but i'm really interested in digging into flux or cross plane you're absolutely welcome to skip ahead to those chapters th
