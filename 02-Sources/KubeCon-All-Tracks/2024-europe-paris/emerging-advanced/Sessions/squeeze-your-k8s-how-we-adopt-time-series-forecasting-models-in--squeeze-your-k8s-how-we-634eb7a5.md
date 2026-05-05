---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Emerging + Advanced"
themes: ["Emerging + Advanced"]
speakers: ["Irvin Lim", "Shopee", "Nicholas Kwan", "Sea Limited"]
sched_url: https://kccnceu2024.sched.com/event/1YeQQ/squeeze-your-k8s-how-we-adopt-time-series-forecasting-models-in-finops-practices-irvin-lim-shopee-nicholas-kwan-sea-limited
youtube_search_url: https://www.youtube.com/results?search_query=Squeeze+Your+K8s%3A+How+We+Adopt+Time-Series+Forecasting+Models+in+FinOps+Practices%3F+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Squeeze Your K8s: How We Adopt Time-Series Forecasting Models in FinOps Practices? - Irvin Lim, Shopee & Nicholas Kwan, Sea Limited

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Emerging + Advanced]]
- País/cidade: France / Paris
- Speakers: Irvin Lim, Shopee, Nicholas Kwan, Sea Limited
- Schedule: https://kccnceu2024.sched.com/event/1YeQQ/squeeze-your-k8s-how-we-adopt-time-series-forecasting-models-in-finops-practices-irvin-lim-shopee-nicholas-kwan-sea-limited
- Busca YouTube: https://www.youtube.com/results?search_query=Squeeze+Your+K8s%3A+How+We+Adopt+Time-Series+Forecasting+Models+in+FinOps+Practices%3F+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Squeeze Your K8s: How We Adopt Time-Series Forecasting Models in FinOps Practices?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQQ/squeeze-your-k8s-how-we-adopt-time-series-forecasting-models-in-finops-practices-irvin-lim-shopee-nicholas-kwan-sea-limited
- YouTube search: https://www.youtube.com/results?search_query=Squeeze+Your+K8s%3A+How+We+Adopt+Time-Series+Forecasting+Models+in+FinOps+Practices%3F+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vLc-nCwojIM
- YouTube title: Squeeze Your K8s: How We Adopt Time-Series Forecasting Models in FinOps... Irvin Lim & Nicholas Kwan
- Match score: 0.942
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/squeeze-your-k8s-how-we-adopt-time-series-forecasting-models-in-finops/vLc-nCwojIM.txt
- Transcript chars: 37336
- Keywords: actually, utilization, forecasting, resources, resource, models, forecast, earlier, future, online, long-term, learning, instead, certain, allows, predict, across, patterns

### Resumo baseado na transcript

okay good evening so uh today um I I'd like to share our experience with how we've adopted time series forecasting in the context of finops in kuber 0es uh starting all the way uh from a note level all the way up to our entire fleet in order to reduce cost when managing large quantities of Parts my name is Irvin and unfortunately today I won't be joined by my colleague Nicholas uh who was unable to attend Cube con today this time uh a large portion of today's

### Excerpt da transcript

okay good evening so uh today um I I'd like to share our experience with how we've adopted time series forecasting in the context of finops in kuber 0es uh starting all the way uh from a note level all the way up to our entire fleet in order to reduce cost when managing large quantities of Parts my name is Irvin and unfortunately today I won't be joined by my colleague Nicholas uh who was unable to attend Cube con today this time uh a large portion of today's sharing was also prepared by him and I would be prep presenting his findings and insight on behalf of you guys to uh today so just a quick introduction both of us are platform Engineers working within the engineering infrastructure division at shy before we get started I would like to give a brief introduction about our company so we're from shoy which is an e-commerce company operating in several markets worldwide today we are the leading e-commerce uh platform in Southeast Asia Taiwan and Brazil we are also the number one shopping app in these markets uh by aage monthly active users as well as total time spent in app in shoy we've used kubernetes to manage and orchestrate large numbers of ports that power the backend systems behind shopy today we have over 100,000 ports running across tens of thousands of notes distributed across multiple data centers worldwide and we also expect the that these numbers will continue growing as the company grows in the years to come unfortunately managing such large numbers of parts usually mean needing a large number of machines to support them as well and by extension this would cost us millions of dollars per quarter as such one of the main objectives in finops is to find solutions to optimize the usage of our existing resources in order to continue supporting an Ever growing number of containers while minimizing the physical resource requirements thus limiting the increase in financial cost involved from the underlying infrastructure by observing resource utilization patterns with within our clusters we found several common cases of resource wastage which could lead to uh under utilized resources so in shly our resources are provisioned based on the requirement to support campaign events that happen around once a month and as such most of our critical Services would need to have uh sufficient buffer in their resources and at the same time since we host our machines on premise uh provisioning a large quantity of ports on such short notice is usually uh quite impra
