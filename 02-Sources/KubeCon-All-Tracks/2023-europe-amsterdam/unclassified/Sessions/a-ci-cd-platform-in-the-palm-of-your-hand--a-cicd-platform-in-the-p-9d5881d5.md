---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Unclassified"
themes: ["Platform Engineering"]
speakers: ["Claudia Beresford", "Weaveworks"]
sched_url: https://kccnceu2023.sched.com/event/1HyVW/a-cicd-platform-in-the-palm-of-your-hand-claudia-beresford-weaveworks
youtube_search_url: https://www.youtube.com/results?search_query=A+CI%2FCD+Platform+in+the+Palm+of+Your+Hand+CNCF+KubeCon+2023
slides: []
status: parsed
---

# A CI/CD Platform in the Palm of Your Hand - Claudia Beresford, Weaveworks

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Unclassified]]
- Temas: [[Platform Engineering]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Claudia Beresford, Weaveworks
- Schedule: https://kccnceu2023.sched.com/event/1HyVW/a-cicd-platform-in-the-palm-of-your-hand-claudia-beresford-weaveworks
- Busca YouTube: https://www.youtube.com/results?search_query=A+CI%2FCD+Platform+in+the+Palm+of+Your+Hand+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre A CI/CD Platform in the Palm of Your Hand.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyVW/a-cicd-platform-in-the-palm-of-your-hand-claudia-beresford-weaveworks
- YouTube search: https://www.youtube.com/results?search_query=A+CI%2FCD+Platform+in+the+Palm+of+Your+Hand+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2g_TXw5bkLY
- YouTube title: A CI/CD Platform in the Palm of Your Hand - Claudia Beresford, Weaveworks
- Match score: 0.819
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/a-ci-cd-platform-in-the-palm-of-your-hand/2g_TXw5bkLY.txt
- Transcript chars: 30772
- Keywords: running, actually, cluster, liquid, raspberry, github, flintlock, runners, runner, actions, containers, action, already, control, operating, kernel, microbm, create

### Resumo baseado na transcript

so what I'm going to talk about today so to begin with I'm going to introduce you something called micro VMS and explain what they are I'm then going to talk about the liquid metal project which is maintained and sponsored by weaveworks I'm going to talk about why the liquid metal project and microvms is are useful and then I'm going to demo the thing so let's begin with an introduction to micro VMS so let me just expand my notes a little bit bigger there we go microamps

### Excerpt da transcript

so what I'm going to talk about today so to begin with I'm going to introduce you something called micro VMS and explain what they are I'm then going to talk about the liquid metal project which is maintained and sponsored by weaveworks I'm going to talk about why the liquid metal project and microvms is are useful and then I'm going to demo the thing so let's begin with an introduction to micro VMS so let me just expand my notes a little bit bigger there we go microamps are exactly what they sound like they are smaller VMS they are smaller subset a virtualization tailored for a specific need so you don't have any unnecessary overhead this makes them almost almost as fast you put up and tear down as containers so if you think of your standard VM it has to be ready to run any operating system for any possible UK use case you don't know what people are going to throw at it it's going to be ready for anything which means the hypervisor has to do a lot of work and allocate a ton of resources to accommodate any of these possible scenarios uh with a micro VM you tell the hypervisor to basically half-ass it and only set up the exact things that you need so like if you don't need any hardware device devices or you need one or two you only do those things um so microbeans are designed to give you the best of both worlds so uh VMS give security containers give you speed so in this case you have the speed of almost as fast as a container with the security of having your own kernel your own operating because I know containers have your own operating system but here you have your own sandbox environments to do whatever it is that you like um and because you're excluding a lot of unnecessary um functionality you have a lesser attack surface anyway so those are microbms so what is the liquid metal project and why are microbm is relevant for it so liquid metal are a is a set of tools to declaratively provision kubernetes clusters on lightweight VMS so micro VMS um so there this is built and maintained and sponsored by weaveworks and it's comprised of these four components that I'm going to go through right now so the first one is Flintlock and I'm now regretting not having any notes here because I had to keep looking up to see what's on the slide so Flintlock creates and manages uh the life cycle of microbms so it's a grp series I've written ago and it runs on a bare metal host it can technically Run Anywhere But Here I'm talking about bare metal hosts and you say I would
