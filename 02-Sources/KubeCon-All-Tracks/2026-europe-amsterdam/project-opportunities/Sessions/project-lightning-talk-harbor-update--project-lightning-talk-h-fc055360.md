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
speakers: ["Prasanth Baskar", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFxP/project-lightning-talk-harbor-update-prasanth-baskar-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Harbor+Update+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Harbor Update - Prasanth Baskar, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Prasanth Baskar, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFxP/project-lightning-talk-harbor-update-prasanth-baskar-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Harbor+Update+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Harbor Update.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFxP/project-lightning-talk-harbor-update-prasanth-baskar-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Harbor+Update+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jJVZrXuJZ4Q
- YouTube title: Project Lightning Talk: Harbor Update - Prasanth Baskar, Maintainer
- Match score: 0.807
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-harbor-update/jJVZrXuJZ4Q.txt
- Transcript chars: 4022
- Keywords: harbor, updates, registry, basically, started, projects, quickly, satellite, please, everyone, contributor, recently, version, release, performance, upstream, limits, support

### Resumo baseado na transcript

Um as a I'm a core contributor to harbor and I also contribute to various uh registry based uh CNC projects. And this version includes a few features requested by the community people uh which are a new option for disabling uh tags that is landing onto the S3 and different stoages to improve the performance of the garbage collection that is in harbor and the

### Excerpt da transcript

Hello everyone. Um I am Prashant and I'm here to uh deliver updates on project harbor. Um so let's get started. Who am I? Um as a I'm a core contributor to harbor and I also contribute to various uh registry based uh CNC projects. You can see all of them here. And then um let's quickly jump over to updates. Um so uh we recently released version 2.15. It's the latest release of Harbor. And this version includes a few features requested by the community people uh which are a new option for disabling uh tags that is landing onto the S3 and different stoages to improve the performance of the garbage collection that is in harbor and the other one is upstream proxy con uh cache registry connection limits which is basically uh if you're using harbor as a proxy cache then you don't want to waste your uh rate limits in docker hub or any other upstream registry. So we added that feature and then we also have support for cosine v3 signatures. Uh so yeah and what is it planned for the next release cycle is replacing the radius which is a component in harbor for um improving the performance.

We are going to replace it with valky and then uh we're going to support u trivia results like including the config uh secrets and all the things you get from a TV scan not just vulnerabilities. So these are the updates. Let's quickly jump over to the sub projects of haraba. Um harour has two sub projects. One is uh harbor satellite and the other one is harbor cla. So let's quickly uh see what are the updates in them. Uh the first one is harbor satellite. So harbor satellite is basically a stateless secretless zero test registry which has a very minimal footprint uh designed to be running on the edge and edge based devices gap devices and everything. And we I also have a talk uh coming on uh Kubernetes on edge day which will be like 12:25 p.m. today. So I'm going to run over to that. And so yeah to know more about that come to uh the talk and har we are celebrating like uh 100k plus downloads and if you haven't tried harla yet please check it out. Uh there's a QR code which you can try it out. Basically, it's a harbor has a UI and it's for automating the management of Harbor and to do a lot more config um in a way that is like automatable.

So, it's much more easy and integrable in your workflows. So, yeah, and thanks to the people who built harvest CLI. So, these are the people I'm uh uh thanking them. And so, also thanks to these two guys which are Lakshit and Patrick. they help
