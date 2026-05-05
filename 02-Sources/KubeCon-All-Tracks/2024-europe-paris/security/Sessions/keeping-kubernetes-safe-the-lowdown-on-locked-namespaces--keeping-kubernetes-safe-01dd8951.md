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
speakers: ["Marco De Benedictis", "ControlPlane"]
sched_url: https://kccnceu2024.sched.com/event/1YeSL/keeping-kubernetes-safe-the-lowdown-on-locked-namespaces-marco-de-benedictis-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=Keeping+Kubernetes+Safe%3A+The+Lowdown+on+Locked+Namespaces+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Keeping Kubernetes Safe: The Lowdown on Locked Namespaces - Marco De Benedictis, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Marco De Benedictis, ControlPlane
- Schedule: https://kccnceu2024.sched.com/event/1YeSL/keeping-kubernetes-safe-the-lowdown-on-locked-namespaces-marco-de-benedictis-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=Keeping+Kubernetes+Safe%3A+The+Lowdown+on+Locked+Namespaces+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Keeping Kubernetes Safe: The Lowdown on Locked Namespaces.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSL/keeping-kubernetes-safe-the-lowdown-on-locked-namespaces-marco-de-benedictis-controlplane
- YouTube search: https://www.youtube.com/results?search_query=Keeping+Kubernetes+Safe%3A+The+Lowdown+on+Locked+Namespaces+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8Zwftqf8g8w
- YouTube title: Keeping Kubernetes Safe: The Lowdown on Locked Namespaces - Marco De Benedictis, ControlPlane
- Match score: 0.852
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/keeping-kubernetes-safe-the-lowdown-on-locked-namespaces/8Zwftqf8g8w.txt
- Transcript chars: 26499
- Keywords: spaces, security, cluster, namespace, actually, effectively, obviously, important, access, configuration, resource, resources, network, applications, application, control, basically, talking

### Resumo baseado na transcript

welcome everyone to this uh afternoon session about security and name spaces uh talk is named keeping kubernetes safe the low down on lock name spaces and uh yeah I quickly go about the introduction uh my name is Marco de benedictis I am a senior consultant in control plane we uh do everything Cloud native and devops and obviously security you might have seen me uh well at our booth or at the capture the flag event yesterday and today I'm based in Italy uh and uh yeah I

### Excerpt da transcript

welcome everyone to this uh afternoon session about security and name spaces uh talk is named keeping kubernetes safe the low down on lock name spaces and uh yeah I quickly go about the introduction uh my name is Marco de benedictis I am a senior consultant in control plane we uh do everything Cloud native and devops and obviously security you might have seen me uh well at our booth or at the capture the flag event yesterday and today I'm based in Italy uh and uh yeah I all the PHD in computer and control engineering uh I've been doing uh cyber security consultancy for a number of years more recently I'm also being uh quite involved with some of the uh cncf uh security tag uh activities as well as yeah I was just um that's actually a very nice thing we we actually just published a a new security certification uh the kubernetes and Cloud native security associate and I was fortunate enough to be uh one of the developers so yeah check that out um so this to Keys yeah you you might have well guessed about Nam spaces and uh uh yeah the security features that are U either namespace aware or bound to uh to Nam spaces and uh uh the reason we um I want to do this talk is basically to go through what can go wrong if our name spaces aren't configured properly from the security standpoint or someone can uh can tamper with their configuration and um what I also want to uh to leave you with is a number of mitigations you can effectively enforce in your clusters if you're running any uh in production and yeah you will see this is nothing expensive actually um The Talk itself is motivated by uh the security reviews we do the threat models we do uh in control plane where we see many customers uh relying on lot of security features which depend on uh very U very secure namespace configuration and what we see is that they don't always really realize what's the impact of a Mis configuration on a namespace level so uh yeah that's basically U yeah why I'm I'm talking about you uh about this with you so we all know about uh kubernetes name spaces uh they are not a security uh feature by by itself but uh we use them for logically grouping resources in a cluster so uh they definitely make our life easier for organizing resources in a cluster uh they are not a security feature as I said so they don't do not provide any form of isolation and uh uh yeah but we will see that many many security features depend on them whenever we uh we spin up a new cluster few names space spes are cr
