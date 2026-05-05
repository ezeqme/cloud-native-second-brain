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
themes: ["Community Governance"]
speakers: ["Orlin Vasilev", "Community Manager"]
sched_url: https://kccncna2025.sched.com/event/27d4c/project-lightning-talk-k3s-project-update-orlin-vasilev-community-manager
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+K3s+Project+Update+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: K3s Project Update - Orlin Vasilev, Community Manager

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Orlin Vasilev, Community Manager
- Schedule: https://kccncna2025.sched.com/event/27d4c/project-lightning-talk-k3s-project-update-orlin-vasilev-community-manager
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+K3s+Project+Update+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: K3s Project Update.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d4c/project-lightning-talk-k3s-project-update-orlin-vasilev-community-manager
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+K3s+Project+Update+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=C3gdhC3L1k8
- YouTube title: Project Lightning Talk: K3s Project Update - Orlin Vasilev, Community Manager
- Match score: 0.799
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-k3s-project-update/C3gdhC3L1k8.txt
- Transcript chars: 4737
- Keywords: running, cluster, release, incubation, seconds, security, orland, little, thanks, minutes, sandbox, distribution, download, images, updates, released, course, highly

### Resumo baseado na transcript

Uh my name is Orland and I'm going to it that's going to be a little bit weird. I have two session one after another thanks to the organizers about two different projects. So few updates uh since last time uh we released um of course uh according to the Kubernetes release cadence we released 134 we bumped few components the release notes is huge uh I highly encourage you to check it out 135 it's around the can see and uh raise concern within your security team or actually we use that to be able to address the CVS uh and to patch them. Last time when I said that, Rudolfpho from uh security um security uh I'm sorry, external secrets operator opened uh adopter PR right away.

### Excerpt da transcript

Hi everyone and welcome. Uh my name is Orland and I'm going to it that's going to be a little bit weird. I have two session one after another thanks to the organizers about two different projects. So let's first start with K3s. Um who am I? Uh my name is Orland. I'm the K3S community manager, CNCF ambassador and principal open source technology advocate at SUSA. That's the reason why I'm here because I help out with the K3S community. Uh first of all, anyone here who doesn't know what K3S is? All right, few hands. Great. I hope the next five minutes are super useful for you and I can change your mind to try it out. Um who is using K3S on daily basis? Last time it was like almost the whole room. All right, pretty good. Thank you. So super quick, uh K3S is a sandbox project still at CNCF. It's not a Kubernetes uh fork. It's a full-fledged Kubernetes distribution. It is super lightweight. It's under 100 max and it is designed to run in constrained environments like IoT edge or you can spin clusters in your CI.

So you can test something and then just delete it. Someone says is the most downloaded and most loved Kubernetes distribution. I'm not here to argue about that. And you can have it running under two minutes or under uh 37 seconds. And thanks to the K3D folks, uh I can show you that right now. Uh so I can use that in my next slot. So um here's I hope you can see that. Can you see that? Yeah. What about now? Right. Let's put it let's try this way. So I have my runer desktop running here and I have nothing special and I'm going to do K3D cluster create. So that is going to download the images and K3D is a way to run K3S inside a container. So that is going to download the images and spin up a cluster in just a few seconds as you can see. Um and then you can uh deploy your stuff on it. So um now the cluster says it's ready but I'm going to list all plots and yeah some stuff are still running maybe the uh maybe the Wi-Fi or is the Wi-Fi or DNS but uh in a in a bit we have completely running cluster uh we can get the nodes and everything.

So uh I think it was less than 37 seconds uh hopefully. So few updates uh since last time uh we released um of course uh according to the Kubernetes release cadence we released 134 we bumped few components the release notes is huge uh I highly encourage you to check it out 135 it's around the corner uh by chance I'm part of the release team under the uh docs team once we release 135 a week or two later uh we going to have
