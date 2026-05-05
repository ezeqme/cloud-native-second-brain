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
themes: ["Security", "Kubernetes Core", "Community Governance"]
speakers: ["Constanze Roedig", "Technische Universität Wien", "James Callaghan", "ControlPlane"]
sched_url: https://kccnceu2024.sched.com/event/1YeOX/brewing-the-kubernetes-storm-center-open-source-threat-intelligence-for-the-cloud-native-ecosystem-constanze-roedig-technische-universitat-wien-james-callaghan-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=Brewing+the+Kubernetes+Storm+Center%3A+Open+Source+Threat+Intelligence+for+the+Cloud+Native+Ecosystem+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Brewing the Kubernetes Storm Center: Open Source Threat Intelligence for the Cloud Native Ecosystem - Constanze Roedig, Technische Universität Wien & James Callaghan, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Constanze Roedig, Technische Universität Wien, James Callaghan, ControlPlane
- Schedule: https://kccnceu2024.sched.com/event/1YeOX/brewing-the-kubernetes-storm-center-open-source-threat-intelligence-for-the-cloud-native-ecosystem-constanze-roedig-technische-universitat-wien-james-callaghan-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=Brewing+the+Kubernetes+Storm+Center%3A+Open+Source+Threat+Intelligence+for+the+Cloud+Native+Ecosystem+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Brewing the Kubernetes Storm Center: Open Source Threat Intelligence for the Cloud Native Ecosystem.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOX/brewing-the-kubernetes-storm-center-open-source-threat-intelligence-for-the-cloud-native-ecosystem-constanze-roedig-technische-universitat-wien-james-callaghan-controlplane
- YouTube search: https://www.youtube.com/results?search_query=Brewing+the+Kubernetes+Storm+Center%3A+Open+Source+Threat+Intelligence+for+the+Cloud+Native+Ecosystem+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YDIW2CY8WPI
- YouTube title: Brewing the Kubernetes Storm Center: Open Source Threat Intelligence for the Cloud Native Ecosystem
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/brewing-the-kubernetes-storm-center-open-source-threat-intelligence-fo/YDIW2CY8WPI.txt
- Transcript chars: 30516
- Keywords: attack, cluster, threat, actually, clusters, baseline, create, however, interested, events, objects, center, intelligence, theoretical, running, sticks, instrumentation, observed

### Resumo baseado na transcript

thank you so much for your interest in in this topic that we want to talk about which was in fact something that that a couple of us discussed last cubec Con in Chicago and that's the question why do we as a cloud native Community not have a truly open and free way to collect and share threat intelligence with each other amongst ourselves and the other question is what would a t to change that and this is what this talk is about and in reference to the

### Excerpt da transcript

thank you so much for your interest in in this topic that we want to talk about which was in fact something that that a couple of us discussed last cubec Con in Chicago and that's the question why do we as a cloud native Community not have a truly open and free way to collect and share threat intelligence with each other amongst ourselves and the other question is what would a t to change that and this is what this talk is about and in reference to the Sans internet Storm Center we were bold enough to call it the kubernetes Storm Center maybe some of you know that podcast it is it's mostly about endpoints and like maybe printers and Adobe exploits and uh what they do is they have a Global Network of Honey pots from which they report what's currently going on what's being exploited and what we we want to do in analogy to that is we want to use a network of Honey clusters um instrumented with evf to collect that threat intelligence and disseminate it my name is consens Ric I uh work at the Technical University as of Vienna teaching computer science and doing all sorts of practical stuff and with me is hello everyone I am James Callahan uh like Constance I have a background as a theoretical physicist however around 10 years ago I became interested in cyber security and now I work as a principal consultant at control plane uh working mainly in security architecture in my spare time I make music and I also make very bad spinal tap jokes on slide decks uh so if anyone actually gets that very very Niche reference please come and talk to me afterwards because we'll probably get on very very well on the topic of bad jokes two theoretical physicists walk into cucon armed with a host of um practical experience of the real world like uh modeling the universe in n greater than four dimensions um we thought it would be good to do some real world practical experiments I mean how badly can it go right on that note I mean we're not going to take any liability for anything um but we should so this is the agenda for the next 35 minutes and we should always start with why so why do we think this is relevant and I hope that and think that most of you will have been in that situation where you deployment your product was almost ready for production then you had a threat model going on and there's this discussion well we found that there is attack Vector a attack path a to a Target but also attack Vector B attack path B to the same Target and then internally you have your teams
