---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "SDLC"
themes: ["SDLC"]
speakers: ["Laurent Goderre", "Docker"]
sched_url: https://kccnceu2024.sched.com/event/1YeLx/is-your-image-really-distroless-laurent-goderre-docker
youtube_search_url: https://www.youtube.com/results?search_query=Is+Your+Image+Really+Distroless%3F+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Is Your Image Really Distroless? - Laurent Goderre, Docker

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[SDLC]]
- Temas: [[SDLC]]
- País/cidade: France / Paris
- Speakers: Laurent Goderre, Docker
- Schedule: https://kccnceu2024.sched.com/event/1YeLx/is-your-image-really-distroless-laurent-goderre-docker
- Busca YouTube: https://www.youtube.com/results?search_query=Is+Your+Image+Really+Distroless%3F+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Is Your Image Really Distroless?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeLx/is-your-image-really-distroless-laurent-goderre-docker
- YouTube search: https://www.youtube.com/results?search_query=Is+Your+Image+Really+Distroless%3F+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1iJTyf4O8T8
- YouTube title: Is Your Image Really Distroless? - Laurent Goderre, Docker
- Match score: 0.809
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/is-your-image-really-distroless/1iJTyf4O8T8.txt
- Transcript chars: 10928
- Keywords: container, docker, create, allows, configuration, postgress, security, pretty, distribution, package, instead, without, alpine, amount, software, kernel, multi-stage, dependency

### Resumo baseado na transcript

my name is l and I'm from Quebec Canada it's my first time here in Europe I'm quite excited about this I work for Docker uh I work on M maintaining Docker official images uh before joining Docker I joined the docker ecosystem in 2016 when I became a uh official Mainer of the node.js docker official image and I wrote the Alpine Linux VAR for that image as well as many security um improvements and there tooling for maintaining that image if you're here I assume the security is

### Excerpt da transcript

my name is l and I'm from Quebec Canada it's my first time here in Europe I'm quite excited about this I work for Docker uh I work on M maintaining Docker official images uh before joining Docker I joined the docker ecosystem in 2016 when I became a uh official Mainer of the node.js docker official image and I wrote the Alpine Linux VAR for that image as well as many security um improvements and there tooling for maintaining that image if you're here I assume the security is very important to you I also assume that you know that security is a lot of work so this rist image gives us the promise of reducing the amount of work that we do on security and only do the work on things that we actually use and actually need so before we can Define what dis s is we should Define what the drro is because without drro we have to compare to what a drro is so this a pretty good definition I found a l Linux distribution often abbreviated drro is an operating system made from a software collection includes a Linux kernel and often a package management system a typical Linux distribution com com comprises Linux kernel and init system new Tools in libraries documentation and many other types of software when we're talking about container image it's practically the same the only difference is the lack of a kernel because the kernel is shared with the host so this still applies in the world of containers so here's a list of com common Linux drro that you're probably aware Debian nuanu Fedora red hat which seems to have a pretty sizable representation in this room today one way that these Linux distribution differentiate themselves from one another is where one of many but one of them is how they land on the usability to security dilemma Linux without the new tools is very hard to use so each distribution has to choose how much tools they provide to their users to allow them to do the the work they do but everyone has different workflows everyone has different things they do so it's a a bit of a guessing game and some prefer to give more tools and some this solution prefer to give a more minimalist uh approach and let the user figure out and add the the additional components one thing that's really important to notice though is that this dilemma does not make one image more or less secure than the other the the distribution that fall on the usability side like every other uh Linux distribution almost have a very busy security team that constantly puts out patches and address s
