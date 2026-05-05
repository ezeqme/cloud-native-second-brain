---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Cloud Native Novice"
themes: ["Security"]
speakers: ["Whitney Lee", "VMware", "Viktor Farcic", "Upbound"]
sched_url: https://kccnceu2024.sched.com/event/1YeNK/choose-your-own-adventure-the-struggle-for-security-whitney-lee-vmware-viktor-farcic-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Choose+Your+Own+Adventure%3A+The+Struggle+for+Security+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Choose Your Own Adventure: The Struggle for Security - Whitney Lee, VMware & Viktor Farcic, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Security]]
- País/cidade: France / Paris
- Speakers: Whitney Lee, VMware, Viktor Farcic, Upbound
- Schedule: https://kccnceu2024.sched.com/event/1YeNK/choose-your-own-adventure-the-struggle-for-security-whitney-lee-vmware-viktor-farcic-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Choose+Your+Own+Adventure%3A+The+Struggle+for+Security+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Choose Your Own Adventure: The Struggle for Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNK/choose-your-own-adventure-the-struggle-for-security-whitney-lee-vmware-viktor-farcic-upbound
- YouTube search: https://www.youtube.com/results?search_query=Choose+Your+Own+Adventure%3A+The+Struggle+for+Security+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SdaHy60OcWs
- YouTube title: Choose Your Own Adventure: The Struggle for Security - Whitney Lee & Viktor Farcic
- Match score: 0.877
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/choose-your-own-adventure-the-struggle-for-security/SdaHy60OcWs.txt
- Transcript chars: 25685
- Keywords: policy, secret, secrets, application, cluster, production, admission, policies, choose, running, allowed, argo, called, controller, gatekeeper, deployment, runtime, write

### Resumo baseado na transcript

uh welcome to choose your own adventure oh you know what I forgot my clicker I was so excited to get up here I think it's in my bag that's the way to start yeah usually Victor's the one that messes up the first time in this presentation I won't disappoint this time oh no all right here we go meet hero hero is application source code on a developer's laptop hero longs to be a real application running and production serving end users and we're going to help hero

### Excerpt da transcript

uh welcome to choose your own adventure oh you know what I forgot my clicker I was so excited to get up here I think it's in my bag that's the way to start yeah usually Victor's the one that messes up the first time in this presentation I won't disappoint this time oh no all right here we go meet hero hero is application source code on a developer's laptop hero longs to be a real application running and production serving end users and we're going to help hero along the way so our job is to help hero navigate hundreds of cncf projects choose which ones to use integrate them with one another can with so hero can live their dream my name is Whitney this is Victor Victor and I together host a show called you choose on Victor's YouTube channel called devops toolkit so you choose is a Choose Your Own Adventure style Journey Through the cncf landscape and each episode represents a different system design choice so for that system design choice We Gather all the relevant cncf Tech that can do that thing then we invite a maintainer or super user on from each Tech and they each get only five minutes to present about their technology so we put them head-to-head then we have a nice discussion then we put it to the vote and whatever technology the community chooses is the technology that we build into our ongoing demo so the current demo environment we have for this talk is based off of choices made in you choose so we have an AWS eks cluster running it's been and it's been defined with crossplane resources we are using gitops and specifically we're using Argo CD because that's what you the Community chose so our application already is deployed in our demo environments and also our end users can access it because you chose Contour as the Engish solution so wait it sounds like hero already is running in production and serving in users so what are we doing here Heroes already living their dream well the problem is hero is not running in a secure production environment right now heroes in danger the user are in danger the systems in danger oh no we need your help so please scan this QR code during this presentation we're going to have live voting and so for you to be able to vote for which Tech you want to see implemented in our ongoing demo by Victor you need to scan this QR code and we're going to go through three system design choices today we're going to talk about we're uh admission controller policy we're going to talk about and examine tools from runtime Poli poli
