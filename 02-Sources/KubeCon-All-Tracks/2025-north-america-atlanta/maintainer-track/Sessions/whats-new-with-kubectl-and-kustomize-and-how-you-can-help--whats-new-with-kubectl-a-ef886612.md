---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Marly Salazar", "Independent", "Arda Guclu", "Red Hat", "Maciej Szulik", "Eddie Zaneski", "Defense Unicorns"]
sched_url: https://kccncna2025.sched.com/event/27NoU/whats-new-with-kubectl-and-kustomize-and-how-you-can-help-marly-salazar-independent-arda-guclu-red-hat-maciej-szulik-eddie-zaneski-defense-unicorns
youtube_search_url: https://www.youtube.com/results?search_query=What%27s+New+With+Kubectl+and+Kustomize+%E2%80%A6+and+How+You+Can+Help%21+CNCF+KubeCon+2025
slides: []
status: parsed
---

# What's New With Kubectl and Kustomize … and How You Can Help! - Marly Salazar, Independent; Arda Guclu, Red Hat; Maciej Szulik & Eddie Zaneski, Defense Unicorns

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Marly Salazar, Independent, Arda Guclu, Red Hat, Maciej Szulik, Eddie Zaneski, Defense Unicorns
- Schedule: https://kccncna2025.sched.com/event/27NoU/whats-new-with-kubectl-and-kustomize-and-how-you-can-help-marly-salazar-independent-arda-guclu-red-hat-maciej-szulik-eddie-zaneski-defense-unicorns
- Busca YouTube: https://www.youtube.com/results?search_query=What%27s+New+With+Kubectl+and+Kustomize+%E2%80%A6+and+How+You+Can+Help%21+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre What's New With Kubectl and Kustomize … and How You Can Help!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NoU/whats-new-with-kubectl-and-kustomize-and-how-you-can-help-marly-salazar-independent-arda-guclu-red-hat-maciej-szulik-eddie-zaneski-defense-unicorns
- YouTube search: https://www.youtube.com/results?search_query=What%27s+New+With+Kubectl+and+Kustomize+%E2%80%A6+and+How+You+Can+Help%21+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RggqaCSdOGA
- YouTube title: What's New with Kubectl and Kustomize … and How You Can Help!
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/whats-new-with-kubectl-and-kustomize-and-how-you-can-help/RggqaCSdOGA.txt
- Transcript chars: 32953
- Keywords: actually, couple, around, customize, additional, preferences, talking, multicluster, cuddle, probably, everything, create, cluster, little, command, maintainers, having, questions

### Resumo baseado na transcript

okay welcome everyone uh my name is Ma I'm joined here with Eddie and Marley and we will quickly go through around World Tour for what uh 6i has been up to for the past couple of months uh Our intention is to answer as many questions as you might have so if you already are thinking through the question that would be the best option we try to go through the slides rather quickly um to be able to answer your questions uh so 6 I uh is currently

### Excerpt da transcript

okay welcome everyone uh my name is Ma I'm joined here with Eddie and Marley and we will quickly go through around World Tour for what uh 6i has been up to for the past couple of months uh Our intention is to answer as many questions as you might have so if you already are thinking through the question that would be the best option we try to go through the slides rather quickly um to be able to answer your questions uh so 6 I uh is currently led by four uh four people Eddie and myself are here unfortunately Natasha and Katrina uh could not be with us today uh and what 6i basically does is we are responsible for uh development and standardization of the broadly said CLI framework so Cube cdle and all the libraries and tools that are uh built to help you build your own uh C tools not only Cube cutle but literally everything else including plugins for cube cutle um the sub project that we own as I mentioned aside from Cube cuddle customize uh and crew uh there's also kui which is a graphical interface for uh for cube cuddle uh there are libraries like CLI runtime and CLI experimental which help you and also us to build the clis that are comparable with uh with Cube cdle and additional sub projects uh you can find us on uh on kubernetes slack under hash 6 CLI we also have a mailing list both of these are rather low volume so feel free to to jump and follow around and ask questions or propose uh topics if you're a person that prefers in direct communication we also hold uh bi-weekly meetings on Wednesdays all alternatively uh on the other Wednesdays we are holding either customize or CU cutle box prop which is a goals uh also an amazing place to to join and if you're interested in working and picking up particular issues that we're going through uh it's also a nice place to uh to join us uh okay so we had a couple of releases since last time um release 1.27 had some enhancements we added default container annotations that are used by Q Kettle as well as sub resource support for qettle uh aggregated Discovery helps like speed things up like we pull an API server that has a ton of resources on it it takes forever um open API V3 also came um for the explain and we got apply prune got redesigned and we also have the cube Kettle create sub plugins so uh some of the highlights from 1.27 is debug we added a couple of uh new profiles for it um didn't we have sisman also is that that one's for the next one okay uh General Baseline and restricted um and there's some more
