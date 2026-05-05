---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Justin Santa Barbara", "Google", "Ciprian Hacman", "Microsoft"]
sched_url: https://kccncna2025.sched.com/event/27Nlp/the-next-decoupling-from-monolithic-cluster-to-control-plane-with-nodes-justin-santa-barbara-google-ciprian-hacman-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=The+Next+Decoupling%3A+From+Monolithic+Cluster%2C+To+Control-Plane+With+Nodes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The Next Decoupling: From Monolithic Cluster, To Control-Plane With Nodes - Justin Santa Barbara, Google & Ciprian Hacman, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Justin Santa Barbara, Google, Ciprian Hacman, Microsoft
- Schedule: https://kccncna2025.sched.com/event/27Nlp/the-next-decoupling-from-monolithic-cluster-to-control-plane-with-nodes-justin-santa-barbara-google-ciprian-hacman-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=The+Next+Decoupling%3A+From+Monolithic+Cluster%2C+To+Control-Plane+With+Nodes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The Next Decoupling: From Monolithic Cluster, To Control-Plane With Nodes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nlp/the-next-decoupling-from-monolithic-cluster-to-control-plane-with-nodes-justin-santa-barbara-google-ciprian-hacman-microsoft
- YouTube search: https://www.youtube.com/results?search_query=The+Next+Decoupling%3A+From+Monolithic+Cluster%2C+To+Control-Plane+With+Nodes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7czd6oZV3CY
- YouTube title: The Next Decoupling: From Monolithic Cluster, To Control-Pl... Justin Santa Barbara & Ciprian Hacman
- Match score: 0.848
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-next-decoupling-from-monolithic-cluster-to-control-plane-with-node/7czd6oZV3CY.txt
- Transcript chars: 26777
- Keywords: cluster, control, create, management, carpenter, applications, question, autoscaler, working, upgrades, around, creating, running, basically, separate, worker, whatever, controller

### Resumo baseado na transcript

I'm a senior software engineer at Microsoft working on Kubernetes not AKS and uh I'm dealing with uh scalability platform engineering and other interesting stuff. And uh in my spare time I'm contributing to KOPS uh in particular but generally to many projects in the Kubernetes ecosystem especially cluster life cycle related. So historically you know or even to this day a Kubernetes cluster typically comprises both a control plane and worker nodes and reflecting that the installation tools the installers that we have today will create and manage u both that control plane and the nodes together it's easy to understand it's effective it looks great in docs you just have that oneline cops create cluster or g-cloud container or whatever it is that one line that like gives you a working Kubernetes cluster and it's a magical experience Um, however, So because of AI um so if we had an API uh for node program programming uh we could maybe do more magic there and it's the community is tackling a lot of these issues uh generally by moving that node management out of installer tools to the excellent Kubernetes control plane. Um Kaops is an open-source production cluster management tool that is part of the Kubernetes project.

### Excerpt da transcript

Hi everyone. Uh welcome to our talk. Uh my name is Cyprian Hackman. I'm a senior software engineer at Microsoft working on Kubernetes not AKS and uh I'm dealing with uh scalability platform engineering and other interesting stuff. And uh in my spare time I'm contributing to KOPS uh in particular but generally to many projects in the Kubernetes ecosystem especially cluster life cycle related. Thank you. And I'm Justin Santa Barbara. I am a software engineer at Google. Um I've been at Google for about seven years and working on Kubernetes and KOPS for longer than that. Uh so don't want to admit that but it's true. Um but we are two of the maintainers of Kaops. Um but this is not a um this is a maintainer track talk. It's not specifically about KOPS. Uh we're really talking about more of the Kubernetes cluster life cycle uh ideas. Uh particularly a new idea that we see evolving and we want to sort of highlight that idea and get your feedback and your input. Um I see many of the people working on it in this room.

So thank you for making the trek all the way down here to the bowels of wherever we are. Um, and we do welcome your input. Um, particularly afterwards, we'll try to save some time for sort of Q&A and heckling. Um, so yeah, we're going to talk to you about this move happening, which we see, which is basically where we're moving from installers that manage both the control plane and the nodes to a world where we think of those two as very separate uh responsibilities that might even have separate tooling uh that is sort of best of breed for each. Um we are our goal is to give you the context uh to help you to understand whether that's a good idea or not or make your own make up your own mind and uh get the lay of the land in terms of what the various projects out there are doing and what where you might want to contribute. So historically you know or even to this day a Kubernetes cluster typically comprises both a control plane and worker nodes and reflecting that the installation tools the installers that we have today will create and manage u both that control plane and the nodes together it's easy to understand it's effective it looks great in docs you just have that oneline cops create cluster or g-cloud container or whatever it is that one line that like gives you a working Kubernetes cluster and it's a magical experience Um, however, it does introduce day two friction uh that maybe isn't as necessary as if we treated those two concepts separately
