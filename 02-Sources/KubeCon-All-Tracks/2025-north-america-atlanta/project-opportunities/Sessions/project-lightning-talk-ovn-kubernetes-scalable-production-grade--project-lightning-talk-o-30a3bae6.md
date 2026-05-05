---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML", "Networking", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Surya Seetharaman", "Maintainer"]
sched_url: https://kccncna2025.sched.com/event/27d4Q/project-lightning-talk-ovn-kubernetes-scalable-production-grade-networking-for-kubernetes-surya-seetharaman-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+OVN-Kubernetes%3A+Scalable%2C+Production-Grade+Networking+For+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: OVN-Kubernetes: Scalable, Production-Grade Networking For Kubernetes - Surya Seetharaman, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Surya Seetharaman, Maintainer
- Schedule: https://kccncna2025.sched.com/event/27d4Q/project-lightning-talk-ovn-kubernetes-scalable-production-grade-networking-for-kubernetes-surya-seetharaman-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+OVN-Kubernetes%3A+Scalable%2C+Production-Grade+Networking+For+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: OVN-Kubernetes: Scalable, Production-Grade Networking For Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d4Q/project-lightning-talk-ovn-kubernetes-scalable-production-grade-networking-for-kubernetes-surya-seetharaman-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+OVN-Kubernetes%3A+Scalable%2C+Production-Grade+Networking+For+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5SP7RS_DnIE
- YouTube title: Project Lightning Talk: OVN-Kubernetes: Scalable, Production-Grade Networking... Surya Seetharaman
- Match score: 0.964
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-ovn-kubernetes-scalable-production-grade-networ/5SP7RS_DnIE.txt
- Transcript chars: 5614
- Keywords: networking, networks, network, features, basically, cluster, minutes, production, mentioned, cubecon, switch, userdefined, lightning, scalable, clusters, adopters, gaming, workloads

### Resumo baseado na transcript

Um I'm going to be talking about OVN Kubernetes which is a CNCF project for the next five minutes. I'm an engineer working at Red Hat on Open Shift networking and a maintainer of the OVN Kubernetes project. OVN and OBVs are Linux foundation projects and OVN Kubernetes leverages both of these concepts at its core to make networking possible on our Kubernetes clusters. We are looking for more contributors and adopters and we are a very we have a very simple architecture like I mentioned OVN Kubernetes is basically watching for Kubernetes events and objects and translating them into OVN logical constructs and what that means is for example if you have a node created in your Kubernetes cluster this is translated to a bunch of virtual routers and switches and that network topology is what makes networking possible. In addition to supporting all the core Kubernetes features like porttood networking through Geneva encapsulation tunnels, services network policies, admin network policies, we also support an advanced set of networking features like egress controls, bandwidth controls, performance through hardware offload for wire speed networking to

### Excerpt da transcript

Hello everyone. Uh this is a much bigger room than I anticipated. Um I'm going to be talking about OVN Kubernetes which is a CNCF project for the next five minutes. I'm Surya. I'm an engineer working at Red Hat on Open Shift networking and a maintainer of the OVN Kubernetes project. So OVN Kubernetes is a production grade scalable networking plug-in solution for your Kubernetes clusters. And we have two main adopters today which is Nvidia. They run it in their cloud gaming production environments which provides seamless networking for their gaming workloads and Red Hat uses it in open shift. And how many of you in the audience when I mentioned in Kubernetes thought we were cubovn can you please raise hands? Don't be shy. If you thought we were cubn let's see it all the way up. Not that many. I see a few here and there. Uh, every time I come to CubeCon, we get confused for cubeovian. But I do want to mention that we are two separate projects. That's our logo. It's a Kubernetes view with OVN and OBS in the middle.

So if there's a takeaway from my 5 minutes lightning talk, it's the fact that we are not cubeovn. We are kubernetes which kind of sounds similar and that's because we use the same terminologies or stack underneath. For those of you who do not know, we use Ovs, also known as OpenV switch, which is a production grade multi-verirtual switch, which is basically your data plane running on every node in the cluster. OVN is an abstraction on top of OBS, which makes life simple, meaning that it helps you abstract all your networking constructs into logical network topologies, which then programs the open flows on your open v switch. OVN and OBVs are Linux foundation projects and OVN Kubernetes leverages both of these concepts at its core to make networking possible on our Kubernetes clusters. We were founded in 2016, but we were late to the CNCF journey. Late would be an understatement. We became a sandbox project only last year, but that's cuz we were late to the start line to begin with. Um, but we're very happy to be here as part of the CNCF cloud native family.

And that's our QR code for our website. uh please do join us. We are looking for more contributors and adopters and we are a very we have a very simple architecture like I mentioned OVN Kubernetes is basically watching for Kubernetes events and objects and translating them into OVN logical constructs and what that means is for example if you have a node created in your Kubernetes cluster this
