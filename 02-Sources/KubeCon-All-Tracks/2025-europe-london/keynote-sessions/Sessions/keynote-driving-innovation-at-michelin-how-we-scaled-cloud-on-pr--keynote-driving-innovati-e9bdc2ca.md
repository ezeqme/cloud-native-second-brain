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
themes: ["AI ML", "Runtime Containers", "SRE Reliability"]
speakers: ["Gabriel Quennesson", "Container as a Service Tech Lead", "Michelin", "Arnaud Pons", "Container as a Service Product Architect", "Michelin"]
sched_url: https://kccnceu2025.sched.com/event/1w69M/keynote-driving-innovation-at-michelin-how-we-scaled-cloud-on-prem-infrastructure-while-cutting-costs-gabriel-quennesson-container-as-a-service-tech-lead-michelin-arnaud-pons-container-as-a-service-product-architect-michelin
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Driving+Innovation+at+Michelin%3A+How+We+Scaled+Cloud+%26+On-Prem+Infrastructure+While+Cutting+Costs+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: Driving Innovation at Michelin: How We Scaled Cloud & On-Prem Infrastructure While Cutting Costs - Gabriel Quennesson, Container as a Service Tech Lead, Michelin & Arnaud Pons, Container as a Service Product Architect, Michelin

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Gabriel Quennesson, Container as a Service Tech Lead, Michelin, Arnaud Pons, Container as a Service Product Architect, Michelin
- Schedule: https://kccnceu2025.sched.com/event/1w69M/keynote-driving-innovation-at-michelin-how-we-scaled-cloud-on-prem-infrastructure-while-cutting-costs-gabriel-quennesson-container-as-a-service-tech-lead-michelin-arnaud-pons-container-as-a-service-product-architect-michelin
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Driving+Innovation+at+Michelin%3A+How+We+Scaled+Cloud+%26+On-Prem+Infrastructure+While+Cutting+Costs+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: Driving Innovation at Michelin: How We Scaled Cloud & On-Prem Infrastructure While Cutting Costs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1w69M/keynote-driving-innovation-at-michelin-how-we-scaled-cloud-on-prem-infrastructure-while-cutting-costs-gabriel-quennesson-container-as-a-service-tech-lead-michelin-arnaud-pons-container-as-a-service-product-architect-michelin
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Driving+Innovation+at+Michelin%3A+How+We+Scaled+Cloud+%26+On-Prem+Infrastructure+While+Cutting+Costs+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lFaSEevdZvU
- YouTube title: Keynote: Driving Innovation at Michelin: How We Scaled Cloud & On-Prem In... G. Quennesson & A. Pons
- Match score: 0.859
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-driving-innovation-at-michelin-how-we-scaled-cloud-on-prem-inf/lFaSEevdZvU.txt
- Transcript chars: 4069
- Keywords: cluster, platform, several, vendor, infrastructure, application, source, finally, manage, clusters, basically, solution, strategy, product, michin, software, object, repositories

### Resumo baseado na transcript

so hello everyone uh I'm arop this is Gabrielle kenes we are from michan company leader TI manufacturer and uh we are part of coner as a service uh platform on TT which is responsible to deliver kubernetes platform to our internal project teams and we are here to share with you how we scale cloud and un Prem uh infrastructure while cutting costs so first these are some uh metrics uh about kubernetes footprint in michan so we um manage 62 clusters in 42 different locations many due to

### Excerpt da transcript

so hello everyone uh I'm arop this is Gabrielle kenes we are from michan company leader TI manufacturer and uh we are part of coner as a service uh platform on TT which is responsible to deliver kubernetes platform to our internal project teams and we are here to share with you how we scale cloud and un Prem uh infrastructure while cutting costs so first these are some uh metrics uh about kubernetes footprint in michan so we um manage 62 clusters in 42 different locations many due to deployment of cluster in each of our Factory and we have 450 business application deploy units uh with um 36,000 PS so basically our kis jour started back in 2018 and we've gone through several iteration of our platform since then and back in 203 2023 sorry um we were using a vendor based solution at this time uh two stream of event converge the first is that uh our vendor um switch its strategy and basically the product that we were using up until now will no longer be available and it turn it would force us into a cluster migration because the vendor will not provide us with a migration pass from one product to this new product the second is that Michin matured on its open source strategy and around this time Michin created its open source project office and finally Michin always had an ambition to uh make it Specialists within the company Thrive and in this regard uh opting for a make instead of BU strategy can go a long way so at the end of 2023 we we did decided to rebuild our platform from the ground dump only only using only open-source software which AR will now introduce you to so this is a global picture the implemented solution based on open source project uh we can see in the middle of the picture the cluster II management cluster uh which is used to manage work CL clusters uh in this management cluster we have deed several uh components so the first one is Aro CD to make um gups at scale uh we also use cluster and providers to manage different infrastructure for work cluster life cycle we have a crossplane uh component to um under prerequisits for infrastructure and some um add-ons Deploy on these clusters and we have a custom component which is U here to make the link between cluster RPI cluster object and uh CD cluster secret object form on the bottom of the screen we can see that we have several repositories so the first one there are G repositories the first one is uh used to store cluster inventories cluster definitions and their addons we also have an AGD co
