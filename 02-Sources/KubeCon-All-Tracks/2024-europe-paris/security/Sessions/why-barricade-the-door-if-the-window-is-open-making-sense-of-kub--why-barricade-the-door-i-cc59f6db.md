---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Shay Berkovich", "Wiz"]
sched_url: https://kccnceu2024.sched.com/event/1YePj/why-barricade-the-door-if-the-window-is-open-making-sense-of-kubernetes-initial-access-vectors-shay-berkovich-wiz
youtube_search_url: https://www.youtube.com/results?search_query=Why+Barricade+the+Door+if+the+Window+Is+Open%3F+Making+Sense+of+Kubernetes+Initial+Access+Vectors+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Why Barricade the Door if the Window Is Open? Making Sense of Kubernetes Initial Access Vectors - Shay Berkovich, Wiz

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Shay Berkovich, Wiz
- Schedule: https://kccnceu2024.sched.com/event/1YePj/why-barricade-the-door-if-the-window-is-open-making-sense-of-kubernetes-initial-access-vectors-shay-berkovich-wiz
- Busca YouTube: https://www.youtube.com/results?search_query=Why+Barricade+the+Door+if+the+Window+Is+Open%3F+Making+Sense+of+Kubernetes+Initial+Access+Vectors+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Why Barricade the Door if the Window Is Open? Making Sense of Kubernetes Initial Access Vectors.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YePj/why-barricade-the-door-if-the-window-is-open-making-sense-of-kubernetes-initial-access-vectors-shay-berkovich-wiz
- YouTube search: https://www.youtube.com/results?search_query=Why+Barricade+the+Door+if+the+Window+Is+Open%3F+Making+Sense+of+Kubernetes+Initial+Access+Vectors+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aeOKwTDAxj4
- YouTube title: Why Barricade the Door if the Window Is Open? Making Sense of Kubernetes Initial Access Vectors
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/why-barricade-the-door-if-the-window-is-open-making-sense-of-kubernete/aeOKwTDAxj4.txt
- Transcript chars: 25205
- Keywords: cluster, access, course, talking, clusters, detect, initial, attacker, misconfiguration, security, malicious, config, authenticated, protect, probably, inside, control, typically

### Resumo baseado na transcript

hello everybody Welcome bonjour welcome to my talk why barricade the door if the window is open why indeed the next half an hour we're going to talk about various ways uh to get into the kubernetes and also we'll try to make sense of those ways to come up with some kind of framework that will help us think about them um okay my name is Shay Shay bovitz I am a threat researcher in whiz you might know me through one of these projects uh right now I'm

### Excerpt da transcript

hello everybody Welcome bonjour welcome to my talk why barricade the door if the window is open why indeed the next half an hour we're going to talk about various ways uh to get into the kubernetes and also we'll try to make sense of those ways to come up with some kind of framework that will help us think about them um okay my name is Shay Shay bovitz I am a threat researcher in whiz you might know me through one of these projects uh right now I'm as I said I'm happy to be the part of the amazing wi threat research team where I'm responsible among other things for uh the main of kubernetes threat research okay let's talk about clusters um so I was told that every good talk need is to have a hook to something to engage the audience to explain the motivation um but I think in this case we don't really need that much motivation because it's kind of obvious right the same way that you don't want to get burlers in your house you don't want to get attacker to give them access into your cluster be it your first cluster that you're staging through some kind of click in the cloud UI by choosing the default options or be it your cluster number 5,000 that you're staging through some kind of fancy terraform um your primary security concern the First Security concern is to make sure that it's not easy to get into your cluster of course before you run some kind of fancy KPM and uh audit Security Solutions and so we'll use this house as a metaphor for the cluster by the way did somebody recognize what's this house which movie is this from that's right yeah McAllister's house so we'll use the misfortunes of that those wet Bandits marf and Harry I think their name was uh that were trying to get into the house um and Kevin was trying to F them off so we'll use those analogies uh as an analogist to the potential attackers that try to get into your clusters uh just something to to make the talk more engaging and more perhaps intuitive as well so now the first reason is obvious of course but there are a couple more reasons more subtle so the um for example these are the numbers from our 2023 security report it takes 22 minutes for attacker or for malicious scans to reach newly staged eks cluster okay so if you have the cluster that reachable publicly assume attackers know about about it okay that's your assumption and then there's another even more subtle reason again from the same security report um I'll explain about report first so we took a bunch of data from the consente
