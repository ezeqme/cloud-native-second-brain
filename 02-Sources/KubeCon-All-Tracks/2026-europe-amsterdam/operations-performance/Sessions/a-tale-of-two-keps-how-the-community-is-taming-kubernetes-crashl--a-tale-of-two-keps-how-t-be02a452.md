---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Yang Li", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2CVyf/a-tale-of-two-keps-how-the-community-is-taming-kubernetes-crashloopbackoff-yang-li-google
youtube_search_url: https://www.youtube.com/results?search_query=A+Tale+of+Two+KEPs%3A+How+the+Community+is+Taming+Kubernetes%27+CrashLoopBackoff+CNCF+KubeCon+2026
slides: []
status: parsed
---

# A Tale of Two KEPs: How the Community is Taming Kubernetes' CrashLoopBackoff - Yang Li, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Yang Li, Google
- Schedule: https://kccnceu2026.sched.com/event/2CVyf/a-tale-of-two-keps-how-the-community-is-taming-kubernetes-crashloopbackoff-yang-li-google
- Busca YouTube: https://www.youtube.com/results?search_query=A+Tale+of+Two+KEPs%3A+How+the+Community+is+Taming+Kubernetes%27+CrashLoopBackoff+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre A Tale of Two KEPs: How the Community is Taming Kubernetes' CrashLoopBackoff.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVyf/a-tale-of-two-keps-how-the-community-is-taming-kubernetes-crashloopbackoff-yang-li-google
- YouTube search: https://www.youtube.com/results?search_query=A+Tale+of+Two+KEPs%3A+How+the+Community+is+Taming+Kubernetes%27+CrashLoopBackoff+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FlTb383gXbU
- YouTube title: A Tale of Two KEPs: How the Community is Taming Kubernetes' CrashLoopBackoff - Yang Li, Google
- Match score: 0.988
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/a-tale-of-two-keps-how-the-community-is-taming-kubernetes-crashloopbac/FlTb383gXbU.txt
- Transcript chars: 14231
- Keywords: second, container, restart, minute, seconds, behavior, actually, minutes, cublet, default, cluster, network, change, original, recovery, completely, database, global

### Resumo baseado na transcript

Uh over the years I have been an application developer, a cluster administrator and a contributor to the open source project. Um currently I'm a technical solution engineer at Google Cloud helping users scale their infrastructure on GKE. Now, keep your hands up if you ever wanted to fix a Kubernetes behavior but didn't know how to navigate the cap process. Um when we talked to the original Kubernetes maintainers, the answer was simple. The current behavior was not designed beyond the motivation to throttle misbehaving containers. Um at the application layer people wrote bash wrappers scripts to hide the crash from Kubernetes completely.

### Excerpt da transcript

So hello everyone. Uh my name is Yang. Uh I have been working with Kubernetes since 2017. Uh over the years I have been an application developer, a cluster administrator and a contributor to the open source project. Um currently I'm a technical solution engineer at Google Cloud helping users scale their infrastructure on GKE. So today I want to tell you a story about crash back loop uh crash loop back off and caps. So as we know crash loop back off means some container is crashing repeatedly and kubad as increasing delays before restarting it so that it won't waste node resources. That delay can grow up to five minutes and caps are Kubernetes enhancement proposals. When we have a non-trivial change to be done in the project, CAP help us helps us communicate and coordinate the change. So this is a story about how the comm community community navigate years of debate to finally tame the five minute war. So first of all uh let's do a quick show of hands. How many of you have deploy a port watch it crash and found yourself starting at the arrow?

Okay that's majority of the room. Now, keep your hands up if you ever wanted to fix a Kubernetes behavior but didn't know how to navigate the cap process. Okay, I see you. You are in the right room. Um, so if you have raised your hand, you are part of a long history. The crash loop back off behavior was introduced way back in 2015. You may wonder why exact five minute? Why an exponential curve? Um when we talked to the original Kubernetes maintainers, the answer was simple. There was no deep benchmarking. The current behavior was not designed beyond the motivation to throttle misbehaving containers. It was just a quick defensive mechanism to project the node. So the delay doubles every time up to 300 seconds and you are stuck in in that five minute pennet box until your container runs cleanly for 10 minutes. Now people didn't like this. By 2017, the issue 572 91 was opened requesting to make the behavior adjustable. As I just checked this morning, it has over 360 positive reactions and is it is the third most reacted issues in the core repository.

So if you read through the over 100 comments, users were actually begging for three different things. First, the success exit. They argued, "My container did it job and exited with code zero. Why is Kublat punishing it?" Second, early recovery. People dealing with short two second network glitch um felt that waiting five minutes to reconnect was just too long. Third late re
