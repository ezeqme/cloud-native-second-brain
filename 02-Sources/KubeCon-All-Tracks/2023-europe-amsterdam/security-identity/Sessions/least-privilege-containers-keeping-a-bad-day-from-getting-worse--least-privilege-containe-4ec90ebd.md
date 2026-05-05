---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["AI ML", "Security", "Runtime Containers"]
speakers: ["Greg Castle", "Vinayak Goyal", "Google"]
sched_url: https://kccnceu2023.sched.com/event/1HyX4/least-privilege-containers-keeping-a-bad-day-from-getting-worse-greg-castle-vinayak-goyal-google
youtube_search_url: https://www.youtube.com/results?search_query=Least+Privilege+Containers%3A+Keeping+a+Bad+Day+from+Getting+Worse+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Least Privilege Containers: Keeping a Bad Day from Getting Worse - Greg Castle & Vinayak Goyal, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Greg Castle, Vinayak Goyal, Google
- Schedule: https://kccnceu2023.sched.com/event/1HyX4/least-privilege-containers-keeping-a-bad-day-from-getting-worse-greg-castle-vinayak-goyal-google
- Busca YouTube: https://www.youtube.com/results?search_query=Least+Privilege+Containers%3A+Keeping+a+Bad+Day+from+Getting+Worse+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Least Privilege Containers: Keeping a Bad Day from Getting Worse.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyX4/least-privilege-containers-keeping-a-bad-day-from-getting-worse-greg-castle-vinayak-goyal-google
- YouTube search: https://www.youtube.com/results?search_query=Least+Privilege+Containers%3A+Keeping+a+Bad+Day+from+Getting+Worse+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uouH9fsWVIE
- YouTube title: Least Privilege Containers: Keeping a Bad Day from Getting Worse - Greg Castle & Vinayak Goyal
- Match score: 0.909
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/least-privilege-containers-keeping-a-bad-day-from-getting-worse/uouH9fsWVIE.txt
- Transcript chars: 28527
- Keywords: container, running, containers, non-root, capabilities, actually, feature, process, security, pretty, directory, basically, runtime, hopefully, unprivileged, username, access, server

### Resumo baseado na transcript

hey everyone I'm Greg this has been ayak and uh we're talking to you today about least privileged containers and some work we did on gke so this is going to be a little bit weird because uh this is being pre-recorded but we're going to go with it anyway so hands up if you've heard this security advice don't run containers as root and then keep your hand up if you've actually done it if you've actually implemented that advice and your container is on running as root I'm

### Excerpt da transcript

hey everyone I'm Greg this has been ayak and uh we're talking to you today about least privileged containers and some work we did on gke so this is going to be a little bit weird because uh this is being pre-recorded but we're going to go with it anyway so hands up if you've heard this security advice don't run containers as root and then keep your hand up if you've actually done it if you've actually implemented that advice and your container is on running as root I'm going to guess that most people put their hands down for the second part and we've been saying this sort of stuff for a long time and I mean we as in the collective sort of kubernetes security container community you can actually watch Liz rice give a keynote in 2018 uh at this exact conference about how you shouldn't run containers as a key root as root um is it working that advice and I think the short answer really is no unfortunately so cystic uh wrote a report that said uh 76 of containers that they see run as root and I think they've got pretty good visibility of what's actually happening on a lot of machines and that pretty much matches my uh my experience too so we're going to talk about what we did with gke and kubernetes itself we migrated a majority of our containers of of the the gke platform system containers so the containers that actually run gke and uh we migrated most of us non-route what today we're going to talk about why we would even bother doing that what's the point of running as non-root basically how you do it what our strategy was how we sort of went about uh moving all these containers some design choices we had to make all of the little bumps in the road that we hit and uh and then we're also going to talk about a future feature that's coming that should help make this a little bit easier so why do we even care about this what does it matter if containers run as non-root or not if you look think about how a container sort of looks at a high level there's a there's a container with a container runtime and a host kernel and optionally there might be some stuff mapped into that container like hostpath and host Network that kind of thing so if you're a bad guy who's compromised that container and you're looking for a way to get at that host and get it other containers that are running on that host then you've got a few different ways that you can attack there you can use vulnerabilities in the runtime or the kernel or you could uh escalate through some of these uh sor
