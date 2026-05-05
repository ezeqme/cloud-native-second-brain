---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Cloud Native Novice"
themes: ["Security", "Networking", "Kubernetes Core"]
speakers: ["Paul Zerdilas-Herrera", "Nutanix", "Leon Schulze", "Palo Alto Networks"]
sched_url: https://kccnceu2026.sched.com/event/2CW18/from-it-works-to-its-secure-hardening-your-first-kubernetes-cluster-paul-zerdilas-herrera-nutanix-leon-schulze-palo-alto-networks
youtube_search_url: https://www.youtube.com/results?search_query=From+%E2%80%9CIt+Works%21%E2%80%9D+to+%E2%80%9CIt%E2%80%99s+Secure%21%E2%80%9D%3A+Hardening+Your+First+Kubernetes+Cluster+CNCF+KubeCon+2026
slides: []
status: parsed
---

# From “It Works!” to “It’s Secure!”: Hardening Your First Kubernetes Cluster - Paul Zerdilas-Herrera, Nutanix & Leon Schulze, Palo Alto Networks

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Security]], [[Networking]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Paul Zerdilas-Herrera, Nutanix, Leon Schulze, Palo Alto Networks
- Schedule: https://kccnceu2026.sched.com/event/2CW18/from-it-works-to-its-secure-hardening-your-first-kubernetes-cluster-paul-zerdilas-herrera-nutanix-leon-schulze-palo-alto-networks
- Busca YouTube: https://www.youtube.com/results?search_query=From+%E2%80%9CIt+Works%21%E2%80%9D+to+%E2%80%9CIt%E2%80%99s+Secure%21%E2%80%9D%3A+Hardening+Your+First+Kubernetes+Cluster+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre From “It Works!” to “It’s Secure!”: Hardening Your First Kubernetes Cluster.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW18/from-it-works-to-its-secure-hardening-your-first-kubernetes-cluster-paul-zerdilas-herrera-nutanix-leon-schulze-palo-alto-networks
- YouTube search: https://www.youtube.com/results?search_query=From+%E2%80%9CIt+Works%21%E2%80%9D+to+%E2%80%9CIt%E2%80%99s+Secure%21%E2%80%9D%3A+Hardening+Your+First+Kubernetes+Cluster+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oW946hLuKNc
- YouTube title: From “It Works!” to “It’s Secure!”: Hardening Your First Kub... Paul Zerdilas-Herrera & Leon Schulze
- Match score: 0.833
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/from-it-works-to-its-secure-hardening-your-first-kubernetes-cluster/oW946hLuKNc.txt
- Transcript chars: 24585
- Keywords: secure, literally, cluster, basically, access, deploying, probably, running, security, deploy, figure, attacker, inside, attack, actually, application, weekend, understand

### Resumo baseado na transcript

The weather is not really helping us, but you know, let's make the most out of it. So literally I'm more coming out more of the out of the security world. >> So Dave got a little problem because Dave, like we said, he's kind of new. He has no clue about really deploying something with Kubernetes and even less about how to secure it, right? He's excited to uh be congratulated by his teammate, his manager about learning Kubernetes so fast, about deploying his first app so fast. So, basically um I'm not sure how familiar we guys are with network security.

### Excerpt da transcript

Good, good morning everyone. Thank you very much for being here. Um, it's actually a pleasure to see so many people here. We're definitely not expecting that. Uh, so thank you for being here. Um, second day of CubeCon. The weather is not really helping us, but you know, let's make the most out of it. Let's enjoy it. My name is Paul. I work for Nutanix as a solution engineer. I specialize in our Kubernetes platform, NKP, Nutanics Platform. And today I have here with me my friend Leon. Yeah. Hi guys and girls of course and everyone else. Uh my name is Leon. I'm working for Palo Alto Networks as a sec ops guy. Uh domain consultant it's called. So literally I'm more coming out more of the out of the security world. And yeah so before we dive into the actual uh presentation just want to take a minute to give you a bit of context of why we're here. Um so all of this started like a year and a half ago. Um, I was super excited. Uh, we're having a couple of beers with uh my friend Leon and I'm like, "Hey, you know, this Kubernetes is fun.

I'm deploying clusters, exposing applications, breaking clusters. Uh, this is fun." And as a good German friend of mine, he was like, "Hey, Paul, is this even secure? Did you even think about security when deploying your stuff?" Right. And I'm like, "I have no idea. I have never thought of it." And so we said, okay, let's actually work on this and try to share some of our findings with all of you guys. Uh we're going to do this in a very simple way to make this easy. Um and we have a story. We've divided this in three acts. Uh from it works to secure. So let's get started. All right. Just as a short disclaimer, we're providing you also some statistics during the session. These statistics are coming from different vendors, different research institutes. So the numbers we provide you are not made up. Okay. All right. So I want to introduce you to someone. His name is Dave. Uh Dave is early in his career, junior developer. Um just started at a small startup. Let's say a fintech startup. Uh just got his badge, his notebook, some company merchandise.

And Dave is dreaming big, right? He's >> like like all of us >> like all of us on day one. >> So um yeah he's full of ambition but zero idea what's coming. >> So Wednesday morning I don't know if you can relate to that probably most of you can his manager walks in and is like hey emergency man I need something from you build me something right so in this case some internal support tool u
