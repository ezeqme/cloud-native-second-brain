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
themes: ["AI ML", "Networking", "Kubernetes Core", "Community Governance"]
speakers: ["Morgan Foster", "Nir Rozenbaum", "Red Hat", "Shachar Tal", "Palo Alto Networks"]
sched_url: https://kccnceu2026.sched.com/event/2EF5t/aim-at-the-gate-introducing-the-ai-gateway-working-group-in-kubernetes-morgan-foster-nir-rozenbaum-red-hat-shachar-tal-palo-alto-networks
youtube_search_url: https://www.youtube.com/results?search_query=AI%27m+at+the+Gate%21+Introducing+the+AI+Gateway+Working+Group+in+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# AI'm at the Gate! Introducing the AI Gateway Working Group in Kubernetes - Morgan Foster & Nir Rozenbaum, Red Hat; Shachar Tal, Palo Alto Networks

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Morgan Foster, Nir Rozenbaum, Red Hat, Shachar Tal, Palo Alto Networks
- Schedule: https://kccnceu2026.sched.com/event/2EF5t/aim-at-the-gate-introducing-the-ai-gateway-working-group-in-kubernetes-morgan-foster-nir-rozenbaum-red-hat-shachar-tal-palo-alto-networks
- Busca YouTube: https://www.youtube.com/results?search_query=AI%27m+at+the+Gate%21+Introducing+the+AI+Gateway+Working+Group+in+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre AI'm at the Gate! Introducing the AI Gateway Working Group in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF5t/aim-at-the-gate-introducing-the-ai-gateway-working-group-in-kubernetes-morgan-foster-nir-rozenbaum-red-hat-shachar-tal-palo-alto-networks
- YouTube search: https://www.youtube.com/results?search_query=AI%27m+at+the+Gate%21+Introducing+the+AI+Gateway+Working+Group+in+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JiQJcXvvajg
- YouTube title: AI'm at the Gate! Introducing the AI Gateway Working G... Morgan Foster, Nir Rozenbaum & Shachar Tal
- Match score: 0.796
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/aim-at-the-gate-introducing-the-ai-gateway-working-group-in-kubernetes/JiQJcXvvajg.txt
- Transcript chars: 28661
- Keywords: gateway, policy, payload, backend, request, resource, processors, working, inference, processing, egress, around, processor, trying, policies, problems, shahar, routing

### Resumo baseado na transcript

Uh in this talk we are introducing a new working group, a newish working group. It's a very provocative name in these days when everything's called AI something. So instead I'll say he worked on the gateway inference extension heavily and he knows all about optimizing inference at scale which is a very big brand thing to know about. More specifically, we aim to develop new declarative APIs and standards for how to handle AI workload networking in Kubernetes. We also want to make sure the proposed architecture is composable, pluggable, customizable, and allows ordered execution of payload processing pipelines. So next we're going to talk about Shahar is going to talk about what it looks like to get access to the contents of that request and make policy around it because it has some interesting problems.

### Excerpt da transcript

So welcome everybody to our talk. Uh in this talk we are introducing a new working group, a newish working group. Uh where we are trying to build an AI gateway. It's a very provocative name in these days when everything's called AI something. So what the heck is an AI gateway? And today we're going to tell you specifically what we mean by that and how we are trying to achieve supporting those use cases. >> But first you should tell everybody who you are. >> Yes. Yes. I'm getting to it. >> Okay. Uh so uh first of all I want to say we were supposed to have three speakers with us. Uh one of our co-chairs near Rosenbomb and also one of our uh contributors Shahar Tal uh they are stuck uh in the Middle East. They cannot travel because of the conflict that's happening there. Um it's uh really >> very annoying and sad. >> Yes. Uh and so um instead they provided us with videos uh and I will turn off my slack at some point. They provided us with videos uh with their sections of the talk which is great. Near is um amazing in every possible way.

If I told you how amazing he was you would it would sound like cliches. So instead I'll say he worked on the gateway inference extension heavily and he knows all about optimizing inference at scale which is a very big brand thing to know about. And Shahar is a distinguished engineer. I think they should give you a monle when you become a distinguished engineer at Palo Alto Networks. >> It's a little difficult to wear a monle if you already have glasses though. That might be why they >> uh you glue them on maybe. >> E >> I don't know. We'll solve this problem. uh >> we'll ask an AI about it at least. >> And so Shahar is uh has authored a a great deal of our payload processing proposal which he'll talk about. He's a very precise thinker, a lovely person to talk to. Every time I talk to Shahar, I feel a little smarter than before I talked to him. And of course, we have Flynn here. Uh >> I was going to say you're kind of stuck with me because Shahar and Near couldn't be here. Um I am also one of the chairs of the AI AI gateway working group.

their ways. I think I got invited to do that because I have not drunk the AI Kool-Aid as much as some other people have. So, it's very very interesting. And of course, we have Morgan who is also our newest chair in fact. >> Hello. >> How long have you couple months maybe? >> Uh yeah, I started working on the group uh I think in uh something like October of last year. And so I >> about the ti
