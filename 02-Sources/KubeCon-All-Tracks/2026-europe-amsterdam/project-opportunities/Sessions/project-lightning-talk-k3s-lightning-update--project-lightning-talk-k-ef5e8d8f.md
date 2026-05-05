---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Manuel Buil", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFyQ/project-lightning-talk-k3s-lightning-update-manuel-buil-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+K3s+Lightning+Update+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: K3s Lightning Update - Manuel Buil, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Manuel Buil, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFyQ/project-lightning-talk-k3s-lightning-update-manuel-buil-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+K3s+Lightning+Update+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: K3s Lightning Update.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyQ/project-lightning-talk-k3s-lightning-update-manuel-buil-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+K3s+Lightning+Update+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ouMh2xk0XFI
- YouTube title: Project Lightning Talk: K3s Lightning Update - Manuel Buil, Maintainer
- Match score: 0.869
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-k3s-lightning-update/ouMh2xk0XFI.txt
- Transcript chars: 4653
- Keywords: lightning, maintainers, better, meetings, gateway, update, thanks, consume, resources, especially, incubation, please, secrets, deploying, snapshots, important, inclusive, naming

### Resumo baseado na transcript

Good, so I'm Manuel, I'm one of the K3s maintainers, and thanks for coming for to this lightning talk. Um, this is lightning update of what we've been done in the last month, and what we want to do in the next month. So, these inclusive naming and security self-assessment is just two examples of what we've been doing. We have users that are complaining because, you know, the gateway API CRDs are not part of core Kubernetes for different reasons, and each project installing a K3s comes with them, and they might have different versions. You know, for the maintainers in the room, probably this is a problem that you're having as well.

### Excerpt da transcript

Good, so I'm Manuel, I'm one of the K3s maintainers, and thanks for coming for to this lightning talk. Um, this is lightning update of what we've been done in the last month, and what we want to do in the next month. So, for the ones not familiar with K3s, K3s is a fully conformant Kubernetes distribution. It's it's very lean because, yeah, we have a binary, you deploy it, and it doesn't consume a lot of resources. It's simple and fast. You have your Kubernetes cluster running in less than 2 minutes. It's optimized, especially for IoT edge kind of hardware where you don't have a lot of resources, and it's open. We are part of CNCF right now as a sandbox project, um, and we want now to go into incubation. So, if you don't mind asking, um, can you raise your hand if you're using K3s? Great. So, now let me ask you for a favor. Our adopters list is ridiculously small. So, if you're not shy, please, could you open a PR and and and, yeah, put your name there. It will help us a lot in this process of incubation, for example, and also, um, it gives us a lot of energy to continue working.

Um, yeah. So, just to give you to give you some some recent development updates, we we moved to go 1.25. Um, we have now a NYX snapshotter. This was contributed by, um, somebody uh, that is now part of the maintainers list. If that person is here, thank you. Um, we enhanced the kind metrics. Kind is a project that allows us to talk to, uh, different databases that is also part of K3s, and now you can get more information of what's going on. The secrets encryption enablement, like before you had to decide at the beginning when deploying if you wanted your secrets to be encrypted or not. Now, you can you can switch that, um, after deploying it, I don't know, 1 year after. Um, the retention flag for S3 snapshots, before we could you we we only had that flag for the the snapshots that you create, uh, locally. Now, you will also have it for for S3. Uh, containerd 2.2, very very important 2.2.2, actually. Uh, very important for new feature, especially when it comes to DRA and connecting to GPUs, things like that.

And then in our we took a big effort lately, thanks to to Orlin, who is here, um, on being a better CNCF citizen. So, um, now we have an inclusive naming. We have a security self-assessment that you can check. Um, we have project meetings. We are I think we are pretty open. Um, so don't be scared to to come and into these meetings and and join us. So, these inclusive naming a
