---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Matt Turner", "Liam White", "Tetrate"]
sched_url: https://kccnceu2023.sched.com/event/1HycX/apiserver-only-clusters-for-fun-and-profit-matt-turner-liam-white-tetrate
youtube_search_url: https://www.youtube.com/results?search_query=Apiserver-Only+Clusters+for+Fun+and+Profit+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Apiserver-Only Clusters for Fun and Profit - Matt Turner & Liam White, Tetrate

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Matt Turner, Liam White, Tetrate
- Schedule: https://kccnceu2023.sched.com/event/1HycX/apiserver-only-clusters-for-fun-and-profit-matt-turner-liam-white-tetrate
- Busca YouTube: https://www.youtube.com/results?search_query=Apiserver-Only+Clusters+for+Fun+and+Profit+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Apiserver-Only Clusters for Fun and Profit.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HycX/apiserver-only-clusters-for-fun-and-profit-matt-turner-liam-white-tetrate
- YouTube search: https://www.youtube.com/results?search_query=Apiserver-Only+Clusters+for+Fun+and+Profit+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CDaMBBW6IgQ
- YouTube title: Apiserver-Only Clusters for Fun and Profit - Matt Turner & Liam White, Tetrate
- Match score: 0.81
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/apiserver-only-clusters-for-fun-and-profit/CDaMBBW6IgQ.txt
- Transcript chars: 28018
- Keywords: actually, controller, server, istio, control, cluster, resources, database, manager, pattern, resource, basically, controllers, deployment, reconciles, replica, another, running

### Resumo baseado na transcript

okay thank you everyone and Welcome to our talk on API server only clusters for fun and hopefully for some profit so to introduce us my name is Matt Turner I'm a software engineer at tetrate and we have my esteemed inestinable colleague uh head of platform former istio maintainer software engineer very embarrassed person Liam White so yeah we both work at tetrate which is a company that uses service mesh to do identity based application micro segmentation uh sort of Enterprise scale so for high Insurance environments um

### Excerpt da transcript

okay thank you everyone and Welcome to our talk on API server only clusters for fun and hopefully for some profit so to introduce us my name is Matt Turner I'm a software engineer at tetrate and we have my esteemed inestinable colleague uh head of platform former istio maintainer software engineer very embarrassed person Liam White so yeah we both work at tetrate which is a company that uses service mesh to do identity based application micro segmentation uh sort of Enterprise scale so for high Insurance environments um dealing with the organizational and Technical scaling problems that you'll have trying to do hybrid cloud multi-region and xero Trust at Large Scale so we know I guess a fair amount about istio and kubernetes and we've uh hopefully got an interesting talk for you today based on those Tech so let's remind ourselves first how a kubernetes cluster hangs together uh apologies to the kubernetes experts in the room I see some some literal Upstream uh contributors in the audience but I need to do this to get us all speaking the same language and this is maybe a mental model that not everybody has so this is uh I guess this is a diagram of a classic kubernetes cluster exploded with all the components of the control plane for folks who've not seen them before so let's just run through an example right so if I submit a deployment I write some yaml because it's kubernetes that's what we do and I submit that yaml file into the cluster via the API so first of all we hit the API server right the thing that serves the API and our request is authenticated you know are you a user of this cluster can you prove it then it's validated in some other ways uh some authenticate some authorization sorry happens you know okay I know who you are now do you have permission to create new deployments and then eventually this deployment is is serialized and written to the database and at this point there's kind of a pause there's no more synchronous actions that take place this resources you know at rest in the database it's stored persistently it's actually encoded us some protobufs and it sort of sits there now at this point the deployment controller which is a piece of code this has a watch on that type of resource in the database and it wakes up and it processes it now I'm using controller in this case as a kind of abstract term I mean like a particular Loop of code that runs and processes this kind of resource uh physically this Loop of code is in the controller man
