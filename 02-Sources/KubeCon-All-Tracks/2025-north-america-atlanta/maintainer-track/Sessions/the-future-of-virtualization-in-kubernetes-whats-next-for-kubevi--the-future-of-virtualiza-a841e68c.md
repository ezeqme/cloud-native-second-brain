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
speakers: ["Vladik Romanovsky", "Red Hat"]
sched_url: https://kccncna2025.sched.com/event/27Nlm/the-future-of-virtualization-in-kubernetes-whats-next-for-kubevirt-vladik-romanovsky-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=The+Future+of+Virtualization+in+Kubernetes%3A+What%27s+Next+for+KubeVirt+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The Future of Virtualization in Kubernetes: What's Next for KubeVirt - Vladik Romanovsky, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Vladik Romanovsky, Red Hat
- Schedule: https://kccncna2025.sched.com/event/27Nlm/the-future-of-virtualization-in-kubernetes-whats-next-for-kubevirt-vladik-romanovsky-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=The+Future+of+Virtualization+in+Kubernetes%3A+What%27s+Next+for+KubeVirt+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The Future of Virtualization in Kubernetes: What's Next for KubeVirt.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nlm/the-future-of-virtualization-in-kubernetes-whats-next-for-kubevirt-vladik-romanovsky-red-hat
- YouTube search: https://www.youtube.com/results?search_query=The+Future+of+Virtualization+in+Kubernetes%3A+What%27s+Next+for+KubeVirt+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=w0LPBf8H4xc
- YouTube title: The Future of Virtualization in Kubernetes: What's Next for KubeVirt - Vladik Romanovsky, Red Hat
- Match score: 0.915
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-future-of-virtualization-in-kubernetes-whats-next-for-kubevirt/w0LPBf8H4xc.txt
- Transcript chars: 15836
- Keywords: cubert, virtual, migration, another, process, feature, design, machine, support, network, cluster, operations, features, working, machines, effectively, builds, object

### Resumo baseado na transcript

And, uh, today I would like to share some of the, um, of the progress that Cubert had over the past year. Uh, some of the changes in the community, uh, that, uh, occurred and the features that we've been working on and the in general our plans for the future. Uh as cubert evolved we adopted some of uh some of the concepts from kubernetes and uh special interest group is one of them. Uh over the years we established a number of um uh sigs for compute and storage and networking and and many others. development cycle a little bit and we decided to adopt the uh enhancement proposal uh process uh from Kubernetes and kind of adjust it to cubert and uh essentially it means that um for new features and [snorts] major code changes, we now require developers That means that during the design uh phase we're going to review uh the the design proposals uh shape them and then during the development we are going to focus on reviewing the pull requests that are associated with the design propos with the approved

### Excerpt da transcript

Um, hi everyone. Uh, welcome. Thank you all for coming. Uh, my name is Vlatty Kromanski. I'm one of the, uh, maintainers of the Cubert project. And, uh, today I would like to share some of the, um, of the progress that Cubert had over the past year. Uh, some of the changes in the community, uh, that, uh, occurred and the features that we've been working on and the in general our plans for the future. So for those who are not familiar, Cubert is an operator that extends the Kubernetes API server. All right. So sorry about it. Um for those who are not familiar, Cubert is an operator that extends the Kubernetes API server to allow um users to run virtual machines um um alongside pods. And this is all the same uh this is all using the same familiar Kubernetes APIs. And uh we achieved this by um uh running our virtualization stack in a pod. And this pod is unprivileged and untrusted component uh um that all the security um all the security policies apply to it as it would to any other uh default pod in the um in Kubernetes.

Um recently we uh submitted our application for uh for graduation in CNCF. This project uh this project started around 2016 and then we joined CNCF in 2019. So it's been a long journey and for us this is a huge milestone and I provide a link here to our application for those who are interested in uh tracking the progress. Uh as cubert evolved we adopted some of uh some of the concepts from kubernetes and uh special interest group is one of them. Uh over the years we established a number of um uh sigs for compute and storage and networking and and many others. And this year we realized that there's a need for another one that will be dedicated uh for um um taking ownership and maintaining uh the shared parts of the of the project such as controllers and the APIs and uh for this we created the uh the control plane SIG. Um this year uh so Cubert already has a number of working groups in place for example for code quality and uh for testing. Uh and this year we created another one uh for confidential computing and a special one for the array integration.

And uh you can find all of the uh uh meetings and events that are related to uh to the SIGs and working groups on our calendar. Uh you can follow the the QR code here. Uh this year we also had our annual uh virtual uh cubert summit and there were about 260 attendees um which is roughly 17% increase from last year. There were 12 sessions from different organizations and um I have a QR code here
