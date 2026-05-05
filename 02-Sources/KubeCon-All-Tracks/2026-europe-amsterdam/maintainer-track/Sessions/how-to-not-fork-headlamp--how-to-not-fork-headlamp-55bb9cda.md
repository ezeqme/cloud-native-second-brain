---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Joaquim Rocha", "Amutable"]
sched_url: https://kccnceu2026.sched.com/event/2EF5q/how-to-not-fork-headlamp-joaquim-rocha-amutable
youtube_search_url: https://www.youtube.com/results?search_query=How+To+%28Not%29+Fork+Headlamp+CNCF+KubeCon+2026
slides: []
status: parsed
---

# How To (Not) Fork Headlamp - Joaquim Rocha, Amutable

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Joaquim Rocha, Amutable
- Schedule: https://kccnceu2026.sched.com/event/2EF5q/how-to-not-fork-headlamp-joaquim-rocha-amutable
- Busca YouTube: https://www.youtube.com/results?search_query=How+To+%28Not%29+Fork+Headlamp+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre How To (Not) Fork Headlamp.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF5q/how-to-not-fork-headlamp-joaquim-rocha-amutable
- YouTube search: https://www.youtube.com/results?search_query=How+To+%28Not%29+Fork+Headlamp+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nxkidRtUGn8
- YouTube title: How To (Not) Fork Headlamp - Joaquim Rocha, Amutable
- Match score: 0.756
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/how-to-not-fork-headlamp/nxkidRtUGn8.txt
- Transcript chars: 23876
- Keywords: headlamp, plug-in, plugins, history, changes, change, commits, module, commit, everything, actually, desktop, essentially, usually, course, rebase, folder, sometimes

### Resumo baseado na transcript

I'm here to give a talk about headlamp and uh how to fork headlamp and to also fork it. I work at immutable and I uh am a maintainer of headlamp together with other folks like Renee here and uh yeah, I'm also a community cig. I didn't know how to how to how to phrase this but uh I see it as a natural successor of of Kubernetes dashboard being under the CGUI again uh uh which is a project that uh that was archived earlier this year as many of you may know. uh part so Kubernetes API related part so we have a nice way of using uh of of being able to list uh the pods uh the CRDs and all that um yeah and of course we also some APIs that are specific to knowing You don't have to now care about the API, the the Kubernetes API because we already offer a way to list and to do many things that are expected to to be needed by plugins, right? So uh we may have a security fix lined up but we may have the release only in like a week depending on the security fix right.

### Excerpt da transcript

Thank you very much for being here. I'm here to give a talk about headlamp and uh how to fork headlamp and to also fork it. We'll see. Uh my name is Raim. I work at immutable and I uh am a maintainer of headlamp together with other folks like Renee here and uh yeah, I'm also a community cig. So, what is this talk about? I was told by somebody that the title was somehow edgy. Uh, it's it's not really supposed to be or maybe. Uh, so yeah. So, so what we're going to see is uh what is headlamp? Uh what is the headlamp plug-in system? Uh and then do you really need to fork headlamp? And then spoiler alert, ways to to fork headlamp. All right. So, headlamp. So, who knew about headlamp before this CubeCon? I should have said the other way. Sorry. Uh, who didn't know about Headlamp before the CubeCon? Okay. Okay. So, so I don't have to do a very big introduction. So, let's do a quick one. Graphical user interface for Kubernetes. More from the operator point of view. So, you see your workloads and everything. Uh I actually thought, okay, I'll just pull it up.

Let's see and uh live into my home lab uh in my home. So yeah, so it's a it's a Kubernetes uh graphical UI. Uh usually super fast, right? But we we're at the conference uh Wi-Fi. Uh you can see your workloads. Uh you can um open port forwards, all all of that thing, all of those things. Uh, and we'll see also how it's extensible. So, for example, I'm running Flux in my home lab. So, I have this Flux plugin which allows me to uh, you know, see what's going on, if everything is okay. I can also, you know, I push uh, um, I push an update and then I can just sync or I can pause the sync. Tells me when is going to be the next reconciliation. All of these sort of things. I mean the talk is not about flux but it's to show you that everything is kind of seamless uh seamlessly integrated as a plug-in right so uh besides that headlamp is officially part of the kubernetes project uh under the sigui uh you can run it as a desktop application like I just did or you can uh run it as like in cluster or as a deployed service we also have an extension for docker an extension for podman desktop uh backstage extension we try to try to get it everywhere Okay.

Um, it's vendor independent. So, it's not, you know, it's not it's not depending on any flavor of Kubernetes and you don't have to install anything in Kubernetes uh to run it. Uh, usually people want to know what about authentication and all that. We don't have an authenti
