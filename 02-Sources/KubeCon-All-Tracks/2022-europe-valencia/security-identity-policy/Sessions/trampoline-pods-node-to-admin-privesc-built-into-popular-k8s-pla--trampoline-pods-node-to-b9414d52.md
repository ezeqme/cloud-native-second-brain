---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Security + Identity + Policy"
themes: ["AI ML", "Security", "Platform Engineering", "Networking"]
speakers: ["Yuval Avrahami", "Shaul Ben Hai", "Palo Alto Networks"]
sched_url: https://kccnceu2022.sched.com/event/ytlb/trampoline-pods-node-to-admin-privesc-built-into-popular-k8s-platforms-yuval-avrahami-shaul-ben-hai-palo-alto-networks
youtube_search_url: https://www.youtube.com/results?search_query=Trampoline+Pods%3A+Node+to+Admin+PrivEsc+Built+Into+Popular+K8s+Platforms+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Trampoline Pods: Node to Admin PrivEsc Built Into Popular K8s Platforms - Yuval Avrahami & Shaul Ben Hai, Palo Alto Networks

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[AI ML]], [[Security]], [[Platform Engineering]], [[Networking]]
- País/cidade: Spain / Valencia
- Speakers: Yuval Avrahami, Shaul Ben Hai, Palo Alto Networks
- Schedule: https://kccnceu2022.sched.com/event/ytlb/trampoline-pods-node-to-admin-privesc-built-into-popular-k8s-platforms-yuval-avrahami-shaul-ben-hai-palo-alto-networks
- Busca YouTube: https://www.youtube.com/results?search_query=Trampoline+Pods%3A+Node+to+Admin+PrivEsc+Built+Into+Popular+K8s+Platforms+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Trampoline Pods: Node to Admin PrivEsc Built Into Popular K8s Platforms.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytlb/trampoline-pods-node-to-admin-privesc-built-into-popular-k8s-platforms-yuval-avrahami-shaul-ben-hai-palo-alto-networks
- YouTube search: https://www.youtube.com/results?search_query=Trampoline+Pods%3A+Node+to+Admin+PrivEsc+Built+Into+Popular+K8s+Platforms+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PGsJ4QTlKlQ
- YouTube title: Trampoline Pods: Node to Admin PrivEsc Built Into Popular K8s Plat... Yuval Avrahami & Shaul Ben Hai
- Match score: 0.909
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/trampoline-pods-node-to-admin-privesc-built-into-popular-k8s-platforms/PGsJ4QTlKlQ.txt
- Transcript chars: 34296
- Keywords: cluster, permissions, actually, powerful, attack, container, trampoline, question, account, obviously, platforms, impact, escape, attacker, permission, platform, escapes, single

### Resumo baseado na transcript

hello everyone yeah let's get started uh so keep the session on time so my name is indian i'm from google i'm the moderator of this session so it's my honor to introduce uh yuval from palo alto networks talk about the kubernetes security about over privileged containers thank you can everyone hear me in the back yeah awesome so i'm involved today we're going to talk about the trampoline parts and previous escalation kubernetes i'm pretty excited having done a live talk in a couple of years so let's now only 25 run trampoline demon sets and a really similar thing happened uh with the impact of container escapes now it's worth mentioning that this talks about the impact of container escapes due to due to kubernetes native attacks if any platforms has some

### Excerpt da transcript

hello everyone yeah let's get started uh so keep the session on time so my name is indian i'm from google i'm the moderator of this session so it's my honor to introduce uh yuval from palo alto networks talk about the kubernetes security about over privileged containers thank you can everyone hear me in the back yeah awesome so i'm involved today we're going to talk about the trampoline parts and previous escalation kubernetes i'm pretty excited having done a live talk in a couple of years so let's get started with me today was supposed to be should be high he couldn't come at the end but he was an equal part of making this research and a presentation so a bit about the scholar myself we are security researchers at prismacloud in palo alto networks so we do vulnerability research and threat hunting in the cloud we look for security issues in the cloud ecosystem and we try to find the threat actors that are exploiting them and we're also nba fans and we made a couple of predictions for the conference finals when we made this talk i got three out of four right i'm pretty happy about that and a bit about what we'll be discussing today so today we're going to discuss start off by discussing container escapes this threat that we keep hearing about and try to understand what's the real impact what's the real blast radius we'll then talk about the concept that we defined as a trampoline pods and see how they allow privileged escalation in kubernetes in general but also in the most popular kubernetes platforms out there based on a case study that we've been conducting in the last couple of months we'll then talk about some recommendations on how you can address privilege escalation in kubernetes and we'll finish it off with the arbuck police which is an open source tool we're now releasing that can help you address privileged escalation okay so container escapes obviously containers are great for packaging and deploying software right that's why we all use them but they're not the strongest security boundary mostly because of their shield kernel and we can expect that container escapes are likely to continue to happen only in 2022 we had at least six vulnerabilities both in the kernel and in container run times that would have allowed for container escape but containers can also escape because of a misconfiguration right the most well known one is a privileged containers and there are threat actors in the wild that are actually trying to capitalize on those issues
