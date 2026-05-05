---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Operations"
themes: ["Kubernetes Core"]
speakers: ["Noaa Barki", "Shimon Tolts", "Datree"]
sched_url: https://kccncna2021.sched.com/event/lV4r/what-we-learned-from-reading-100+-kubernetes-post-mortems-noaa-barki-shimon-tolts-datree
youtube_search_url: https://www.youtube.com/results?search_query=What+We+Learned+from+Reading+100%2B+Kubernetes+Post-Mortems+CNCF+KubeCon+2021
slides: []
status: parsed
---

# What We Learned from Reading 100+ Kubernetes Post-Mortems - Noaa Barki & Shimon Tolts, Datree

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Operations]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Noaa Barki, Shimon Tolts, Datree
- Schedule: https://kccncna2021.sched.com/event/lV4r/what-we-learned-from-reading-100+-kubernetes-post-mortems-noaa-barki-shimon-tolts-datree
- Busca YouTube: https://www.youtube.com/results?search_query=What+We+Learned+from+Reading+100%2B+Kubernetes+Post-Mortems+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre What We Learned from Reading 100+ Kubernetes Post-Mortems.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV4r/what-we-learned-from-reading-100+-kubernetes-post-mortems-noaa-barki-shimon-tolts-datree
- YouTube search: https://www.youtube.com/results?search_query=What+We+Learned+from+Reading+100%2B+Kubernetes+Post-Mortems+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Bxnu3llBN20
- YouTube title: What We Learned from Reading 100+ Kubernetes Post-Mortems - Noaa Barki & Shimon Tolts, Datree
- Match score: 0.863
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/what-we-learned-from-reading-100-kubernetes-post-mortems/Bxnu3llBN20.txt
- Transcript chars: 26958
- Keywords: policies, policy, organization, mistake, define, important, devops, production, pipeline, configuration, developers, happen, actually, happened, always, memory, developer, cluster

### Resumo baseado na transcript

hi cubeco hi hi noah how are you hi simon how are you i'm very excited to be at the kubecon conference even though it's virtual it's still really exciting it's super exciting thank you all for coming and join us so um let me just yeah so we're going to be here and we'll share our presentation with you and talk to you about you know what we've learned from reading 100 plus plus kubernetes postmortems and experiencing unfortunately but you know it happens to everyone so yeah yeah

### Excerpt da transcript

hi cubeco hi hi noah how are you hi simon how are you i'm very excited to be at the kubecon conference even though it's virtual it's still really exciting it's super exciting thank you all for coming and join us so um let me just yeah so we're going to be here and we'll share our presentation with you and talk to you about you know what we've learned from reading 100 plus plus kubernetes postmortems and experiencing unfortunately but you know it happens to everyone so yeah yeah but first i think it's the first time that we meet so hi everyone my name is noah noah barki i am a full stock developer for more than five years and i am also a tech writer and one of the leaders of github israel community which is the largest github community in the whole universe universe universe so hi everyone i'm shimon i'm one of the co-founders and the ceo of the tree i'm also an aws community hero but we're here in cncf so i'm one of the core organizers of cncf tel aviv here out from israel we have a vibrant community and if you happen to stop by you should definitely come and see the cncf in tel aviv so a little bit about us and how we ended up here talking about kubernetes postpartums you know so we're a startup company and but what we actually deal with on a daily basis is we help companies prevent misconfigurations from reaching production in kubernetes environments so this means we have an open source cli that actually can run on your laptop or in your ci cd against kubernetes manifests and help charts and it can detect misconfigurations such as missing a cpu limit or a liveness probe readiness probe and then yeah um required labels and yeah yeah yes and we will talk about some of those things that they you should definitely apply and but you know from working with the community and working with our customers we were able to see a lot of those um incidents that happened and to learn a lot from those a post-mortems so here in the tree policies is you know is what we do and we integrate directly in within the development pipeline so we get to observe and see a lot of those mistakes that happen and today hopefully it will educate you a little bit about how you can prevent and avoid having those um misconfigurations that can lead you into a you know possible outage or security incident yes assuming you're very correct and i want to add that as a developer at the tree probably my job was not only to understand about kubernetes and how it works under the hood but also to und
