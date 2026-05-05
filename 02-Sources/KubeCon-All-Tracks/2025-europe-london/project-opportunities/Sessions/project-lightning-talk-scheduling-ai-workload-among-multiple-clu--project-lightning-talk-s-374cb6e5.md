---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Josh Packer", "Supporter"]
sched_url: https://kccnceu2025.sched.com/event/1tcvT/project-lightning-talk-scheduling-ai-workload-among-multiple-clusters-josh-packer-supporter
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Scheduling+AI+Workload+Among+Multiple+Clusters+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Scheduling AI Workload Among Multiple Clusters - Josh Packer, Supporter

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Josh Packer, Supporter
- Schedule: https://kccnceu2025.sched.com/event/1tcvT/project-lightning-talk-scheduling-ai-workload-among-multiple-clusters-josh-packer-supporter
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Scheduling+AI+Workload+Among+Multiple+Clusters+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Scheduling AI Workload Among Multiple Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcvT/project-lightning-talk-scheduling-ai-workload-among-multiple-clusters-josh-packer-supporter
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Scheduling+AI+Workload+Among+Multiple+Clusters+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9q9oTJUqQoQ
- YouTube title: Project Lightning Talk: Scheduling AI Workload Among Multiple Clusters - Josh Packer, Supporter
- Match score: 0.943
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-scheduling-ai-workload-among-multiple-clusters/9q9oTJUqQoQ.txt
- Transcript chars: 4528
- Keywords: clusters, workload, cluster, placement, available, allows, resources, management, gpu, define, add-ons, argo, filter, multiq, federated, learning, scheduling, multiple

### Resumo baseado na transcript

My name is Joshua Packer and I'm on the steering committee uh or I'm a steering committee member for open cluster management. And today we're going to talk about scheduling AI workload among multiple clusters or fleets of clusters. This is a CRD that allows you to encapsulate other Kubernetes resources like the core ones such as a Kubernetes deployment or a replica set, but also external CRDs that you might add like an Argo CD or an Argo project application as an example. Needless to say, federated learning is about processing and building your AI models on your remote fleet, maybe keeping them in the data in specific data centers. And open cluster management with placement allows you to put that workload where you need it, define the requirements for federated learning that are needed to build and process the models in the fleet.

### Excerpt da transcript

All right. Hello everybody. My name is Joshua Packer and I'm on the steering committee uh or I'm a steering committee member for open cluster management. And today we're going to talk about scheduling AI workload among multiple clusters or fleets of clusters. And so open cluster management that I mentioned is a CNCF sandbox project. Uh it's been in sandbox for about 5 years now. It's being actively contributed to by both Red Hat and a number of other customer or companies. And uh so what it is is it's a hub and spoke topology. You have a centralized inventory at the hub. You're also able to define your workload at that hub and then distribute it out to your fleet of clusters. And so how does this work? Well, it starts with registering your clusters into that hub. that helps put it into inventory and makes it available by placing an agent and add-ons for those agents onto those clusters that you just uh that you just registered. We're then able to take those clusters and you're able to group them together.

And so the CRD we use for that is called manage cluster sets, but for the sake of this, we'll just say we are able to group your clusters for distributing workload. And so how do you distribute workload? Well, workload is distributed using a manifest work CRD. This is a CRD that allows you to encapsulate other Kubernetes resources like the core ones such as a Kubernetes deployment or a replica set, but also external CRDs that you might add like an Argo CD or an Argo project application as an example. Um, add-ons are what we use to allow you to work with that workload definition. And so the add-ons are controllers for like policies, could be deploying the Argo CD application, etc. And then the magic in all of this is placement. And what placement does it's a CRD, it allows you to dynamically filter down the clusters that you want to apply the manifest work or the workload to. And so how we do that is you can filter on simple things like laser or lasers labels. You can also do cluster claims which allows you to define resources on those spoke clusters and they'll be percolated up and used for filtering.

We also have something called placement score that allows you to score things like how much resources would be available on the system. And then we have availability. Is the cluster actually online? Therefore, should I place workload? And so we said we would talk about AI. And so some of the integrations we've done are with uh Q is the first one. And so in
