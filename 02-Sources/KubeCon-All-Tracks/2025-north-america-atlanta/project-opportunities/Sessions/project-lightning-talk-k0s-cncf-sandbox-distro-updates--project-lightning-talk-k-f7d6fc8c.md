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
themes: ["Runtime Containers"]
speakers: ["Jussi Nummelin", "Technical lead"]
sched_url: https://kccncna2025.sched.com/event/27d50/project-lightning-talk-k0s-cncf-sandbox-distro-updates-jussi-nummelin-technical-lead
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+k0s%3A+CNCF+Sandbox+Distro+Updates+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: k0s: CNCF Sandbox Distro Updates - Jussi Nummelin, Technical lead

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Runtime Containers]]
- País/cidade: United States / Atlanta
- Speakers: Jussi Nummelin, Technical lead
- Schedule: https://kccncna2025.sched.com/event/27d50/project-lightning-talk-k0s-cncf-sandbox-distro-updates-jussi-nummelin-technical-lead
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+k0s%3A+CNCF+Sandbox+Distro+Updates+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: k0s: CNCF Sandbox Distro Updates.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d50/project-lightning-talk-k0s-cncf-sandbox-distro-updates-jussi-nummelin-technical-lead
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+k0s%3A+CNCF+Sandbox+Distro+Updates+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=My5ijmfBQGY
- YouTube title: Project Lightning Talk: k0s: CNCF Sandbox Distro Updates - Jussi Nummelin, Technical lead
- Match score: 0.863
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-k0s-cncf-sandbox-distro-updates/My5ijmfBQGY.txt
- Transcript chars: 3817
- Keywords: actually, single, binary, sandbox, whether, controller, release, basically, control, contributors, windows, distro, welcome, containerd, runtime, couple, course, devices

### Resumo baseado na transcript

So we've basically distilled or tried to distill Kubernetes into the kind of simplest form that we could figure out. So you can take the same exact binary, run it on Red Hat, run it on Ubuntu, run it on Alpine, whatever has a decently modern enough kernel and it just works and gets you a Linux node uh sorry Kubernetes node. So, hop by and and see some demos, meet the faults behind the project, and we'd love to hear your your feedback.

### Excerpt da transcript

Welcome everyone. I'm Yusi. I'll be your tour guide today for this super super quick tour on Kzer. So Kzer is a a cube distro and a CNCF sandbox project. So we've basically distilled or tried to distill Kubernetes into the kind of simplest form that we could figure out. a single binary statically compiled runs basically anywhere. So you can take the same exact binary, run it on Red Hat, run it on Ubuntu, run it on Alpine, whatever has a decently modern enough kernel and it just works and gets you a Linux node uh sorry Kubernetes node. Uh it comes with all batteries included things the usual things like containerd as the runtime couple of options for CNI sets up cute proxies everything you just run the single binary. Of course, you have the option to swap out certain things like like provide your own container runtime dime installs selium as a CNI if you want or some other CNIs and and whatnot. So you really get a a single binary to run in all of your different use cases whether it's on premise whether it's on cloud whether it's on edge devices it just works.

One of the architectural kind of choices we made basically on day one, we wanted to really separate the control plane from the worker plane. So by default when you run Kzer's as a controller mode, you actually get only the controller. You don't get cublet running on the node. You don't get containerd running on the node or anything like that. So you can't really run any workloads on the controller nodes even if you want to. It's actually not only about whether you want to run workloads on a controller node or not, but it this actually this pattern really enables quite cool use cases for example for edge computing because what I can do now is I can actually run my control plane in say public cloud for example and I can run the workers on edge devices somewhere far far in the network edge and I don't have to worry about Okay, how do I control the nodes because I can't access the controllers on there? Like I mentioned, all the use cases launched with the one single binary. So we started as an open source project in 2020.

That's or that's when the first open source release was done. Since then, we've seen very steady usage and and community growth. And then we joined in the CNCF sandbox on February 25. So we're young project from that point of view. And we already have plans in motion to to get to the into incubation state hopefully very very soon, but no promises. One of the things we we've seen especia
