---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Nick Turner", "Amazon", "Steve Wong", "VMware"]
sched_url: https://kccnceu2022.sched.com/event/ytow/sig-cloud-provider-portable-k8s-across-all-clouds-roadmap-and-updates-nick-turner-amazon-steve-wong-vmware
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Cloud+Provider%3A+Portable+K8s+Across+all+Clouds%2C+Roadmap+and+Updates+CNCF+KubeCon+2022
slides: []
status: parsed
---

# SIG Cloud Provider: Portable K8s Across all Clouds, Roadmap and Updates - Nick Turner, Amazon & Steve Wong, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Nick Turner, Amazon, Steve Wong, VMware
- Schedule: https://kccnceu2022.sched.com/event/ytow/sig-cloud-provider-portable-k8s-across-all-clouds-roadmap-and-updates-nick-turner-amazon-steve-wong-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Cloud+Provider%3A+Portable+K8s+Across+all+Clouds%2C+Roadmap+and+Updates+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre SIG Cloud Provider: Portable K8s Across all Clouds, Roadmap and Updates.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytow/sig-cloud-provider-portable-k8s-across-all-clouds-roadmap-and-updates-nick-turner-amazon-steve-wong-vmware
- YouTube search: https://www.youtube.com/results?search_query=SIG+Cloud+Provider%3A+Portable+K8s+Across+all+Clouds%2C+Roadmap+and+Updates+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FNcnQ5QlUco
- YouTube title: SIG Cloud Provider: Portable K8s Across all Clouds, Roadmap and Updates - Nick Turner & Steve Wong
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/sig-cloud-provider-portable-k8s-across-all-clouds-roadmap-and-updates/FNcnQ5QlUco.txt
- Transcript chars: 20349
- Keywords: controller, provider, migration, cubelet, providers, manager, actually, component, volume, effort, support, general, status, running, little, specific, google, balancers

### Resumo baseado na transcript

welcome to kubecon 2022 in valencia this session is about the current state of the kubernetes cloud provider i'm steve wong of vmware and i'm joined by nick turner of amazon we'll quickly cover what the cloud provider does just in case we have some audience members who are new to kubernetes then move on to general project status followed by lightning talks from individual cloud provider implementations finally we'll wrap up with futures and coverage of how to join the cloud provider sigs community the cloud provider is the

### Excerpt da transcript

welcome to kubecon 2022 in valencia this session is about the current state of the kubernetes cloud provider i'm steve wong of vmware and i'm joined by nick turner of amazon we'll quickly cover what the cloud provider does just in case we have some audience members who are new to kubernetes then move on to general project status followed by lightning talks from individual cloud provider implementations finally we'll wrap up with futures and coverage of how to join the cloud provider sigs community the cloud provider is the mechanism that allows kubernetes applications to be portable across various public and on-prem clouds the goal is an experience where any well-written app can run anywhere and for the most part can't even tell where it's running sig cloud provider works closely with a few other sigs to make this happen for example most of the storage related abstraction is managed by sig storage with a little integration activity across the sigs being monitored by sig cloud provider in the early days kubernetes was a monolith when it came to cloud providers the kubernetes binary included a bunch of code for cloud specific cloud providers and it was bigger than it needed to be this had a number of sub-optimal aspects listed here for example a user investigating startup logs on a google cloud might see entries saying could not find a aws ecb the old model slowed the time to future feature and patch delivery and we've been moving to out of tree code for cloud providers for about two years now new deployments should be using auditry versions of the cloud providers now and if you're running a legacy version you need to be planning for a migration and nick is going to tell you more about that migration status so nick take it away yeah um so i'm going to talk a little bit about just kind of general status of cloud provider migration and what components that involves um uh it's it's actually kind of funny i just ran into lucas caldstrom who was a very early member or even the genesis of cloud provider a couple hours ago and we were talking and he actually started doing this work six years ago and he was thinking like how long is this going to take and he in his pessimistic estimate he was thinking about a year year and a half and it ended up not being quite that short and there's a lot of reasons for that but it was more complex than people realized and i think one problem was that there wasn't a lot of motivation for cloud providers to move out of tree because
