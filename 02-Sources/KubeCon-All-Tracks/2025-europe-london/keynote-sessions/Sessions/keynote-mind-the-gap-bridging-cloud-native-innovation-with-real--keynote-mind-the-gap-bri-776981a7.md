---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Keynote Sessions"
themes: ["Keynote Sessions"]
speakers: []
sched_url: https://kccnceu2025.sched.com/event/1txBp/keynote-mind-the-gap-bridging-cloud-native-innovation-with-real-world-use
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Mind+the+Gap%3A+Bridging+Cloud+Native+Innovation+with+Real-World+Use+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: Mind the Gap: Bridging Cloud Native Innovation with Real-World Use

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Keynote Sessions]]
- País/cidade: United Kingdom / London
- Speakers: N/A
- Schedule: https://kccnceu2025.sched.com/event/1txBp/keynote-mind-the-gap-bridging-cloud-native-innovation-with-real-world-use
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Mind+the+Gap%3A+Bridging+Cloud+Native+Innovation+with+Real-World+Use+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: Mind the Gap: Bridging Cloud Native Innovation with Real-World Use.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txBp/keynote-mind-the-gap-bridging-cloud-native-innovation-with-real-world-use
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Mind+the+Gap%3A+Bridging+Cloud+Native+Innovation+with+Real-World+Use+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JqG1wey7-Ao
- YouTube title: Keynote: Mind the Gap: Bridging Cloud Native Innovation with Real-World Use
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-mind-the-gap-bridging-cloud-native-innovation-with-real-world/JqG1wey7-Ao.txt
- Transcript chars: 15966
- Keywords: proteins, backstage, platform, everyone, clusters, security, cluster, looking, ensemble, running, workloads, pepton, created, avocado, privacy, private, compute, server

### Resumo baseado na transcript

HS HSBC embarked on our Kubernetes journey back in 2018 and since then we've now run to running hundreds of clusters supporting workloads for markets in the UK, China, Hong Kong, Mexico and many others as well as our retail wholesale and institutional business running on premises and in the major hyperscalers. Today I want to talk about the retail banks microservices API solution the service hosting platform. At the scale we operate at, cost is also a huge challenge and we've had to develop ways of holding teams accountable for their spending, giving them the tools they need to manage the financial footprint of each workload. So it's our responsibility as a platform to make sure the core service is optimized and the onus however remains with the tenant to keep a tight reign on costs by provisioning elastically based on demand and only using what they need. The industry trend at the moment is very much towards a more democratic and devolved tenency model with smaller clusters allowing engineering teams the flexibility that they demand. And we're looking at improving our shared responsibility model, providing better guardrails for our tenants so that doing the right thing becomes easy and that that the security and availability of our workloads becomes even easier to test, optimize, and maintain.

### Excerpt da transcript

Good morning everyone. HS HSBC embarked on our Kubernetes journey back in 2018 and since then we've now run to running hundreds of clusters supporting workloads for markets in the UK, China, Hong Kong, Mexico and many others as well as our retail wholesale and institutional business running on premises and in the major hyperscalers. Today I want to talk about the retail banks microservices API solution the service hosting platform. This started life as an experiment in the public cloud adoption team to see if our existing on premises platform could be migrated to cloud. And by 2019, our first three clusters were hosting live workloads. And we were ready to start on our migration project. We're currently servicing around 600 million discrete hits a day to our platform, which is running at the moment 7,000 production services with many more still to migrate from our legacy platform, all running across only a dozen or so clusters. As you can see, we scaled up very quickly and we soon encountered the sorts of problems that you only see in smaller you don't see in smaller clusters.

Rather than waiting to become a victim of our own success, we had to shard our workloads based across individual markets, an approach that also helps us to manage our blast radius along business lines. Our clusters are very stable thankfully, but change can still be a bit of a pain problem. So to mitigate these issues during upgrades, we run our clusters in a blue green configuration, rehydrating the new cluster from backups and only cutting over when we're confident that the new cluster is stable. At the scale we operate at, cost is also a huge challenge and we've had to develop ways of holding teams accountable for their spending, giving them the tools they need to manage the financial footprint of each workload. responsibility is shared. So it's our responsibility as a platform to make sure the core service is optimized and the onus however remains with the tenant to keep a tight reign on costs by provisioning elastically based on demand and only using what they need. The industry trend at the moment is very much towards a more democratic and devolved tenency model with smaller clusters allowing engineering teams the flexibility that they demand.

In our case, however, we work in a highly regulated organization with hundreds of IT controls that we need to satisfy. But with a high degree of consistency across our workloads that we support, a more centralized model still makes sens
