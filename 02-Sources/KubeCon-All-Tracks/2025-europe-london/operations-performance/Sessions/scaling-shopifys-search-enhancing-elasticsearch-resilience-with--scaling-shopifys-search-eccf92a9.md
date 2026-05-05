---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Leila Vayghan", "Shopify"]
sched_url: https://kccnceu2025.sched.com/event/1tx8I/scaling-shopifys-search-enhancing-elasticsearch-resilience-with-kubernetes-and-keda-leila-vayghan-shopify
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+Shopify%27s+Search%3A+Enhancing+Elasticsearch+Resilience+With+Kubernetes+and+KEDA+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Scaling Shopify's Search: Enhancing Elasticsearch Resilience With Kubernetes and KEDA - Leila Vayghan, Shopify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Leila Vayghan, Shopify
- Schedule: https://kccnceu2025.sched.com/event/1tx8I/scaling-shopifys-search-enhancing-elasticsearch-resilience-with-kubernetes-and-keda-leila-vayghan-shopify
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+Shopify%27s+Search%3A+Enhancing+Elasticsearch+Resilience+With+Kubernetes+and+KEDA+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Scaling Shopify's Search: Enhancing Elasticsearch Resilience With Kubernetes and KEDA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx8I/scaling-shopifys-search-enhancing-elasticsearch-resilience-with-kubernetes-and-keda-leila-vayghan-shopify
- YouTube search: https://www.youtube.com/results?search_query=Scaling+Shopify%27s+Search%3A+Enhancing+Elasticsearch+Resilience+With+Kubernetes+and+KEDA+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=r59IfCSmUBQ
- YouTube title: Scaling Shopify's Search: Enhancing Elasticsearch Resilience With Kubernetes and KE... Leila Vayghan
- Match score: 1.001
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/scaling-shopifys-search-enhancing-elasticsearch-resilience-with-kubern/r59IfCSmUBQ.txt
- Transcript chars: 23979
- Keywords: search, reindex, elastic, shopify, shards, scaling, indices, indexing, pipeline, region, rights, real-time, production, number, merchants, scaled, queries, orders

### Resumo baseado na transcript

Uh I'm part of the resiliency organization at Shopify whose uh responsibility is to ensure Shopify is always uh up and running ready and reliable for merchants uh and our buyers across the globe. My talk today will be about a project uh where we improved elastic search indexing performance as well as the reliability of our infrastructure uh by using dedicated node pools that are automatically scaled by kada scalers. [Music] We run our fleet of elastic search clusters on managed Kubernetes clusters GK on top of uh GCP and we deploy and maintain them using uh a custom Kubernetes um controller that we have built. As mentioned before, our elastic search clusters run on Kubernetes on top of GCP across different uh regions and availability zones. So both elastic search clusters uh have the uh the same data set and with this inter region uh data replication if one of the elastic search clusters goes down uh we can fail over the query traffic to the elastic search cluster that is functional until the other one has recovered at the application layer. Meaning that if we deploy our Kubernetes cluster across three uh different availability zones.

### Excerpt da transcript

Hello everyone uh and thank you all for coming. My name is Leila. I work at Shopify as a site reliability engineer. Uh I'm part of the resiliency organization at Shopify whose uh responsibility is to ensure Shopify is always uh up and running ready and reliable for merchants uh and our buyers across the globe. My talk today will be about a project uh where we improved elastic search indexing performance as well as the reliability of our infrastructure uh by using dedicated node pools that are automatically scaled by kada scalers. In the next 30 minutes we will learn how at Shopify we uh host the search infrastructure on top of Kubernetes. We'll talk about the entire data pipeline that writes data from uh SQL to elastic search through CFKA and the resilience of its architecture. Uh I will follow by presenting the problem we needed to solve and we'll share our solution for it followed by um some technical details on how to use SCADA uh scalers for scaling uh Kubernetes workloads and I will conclude the presentation with a Q&A.

Shopify is the all-in-one um commerce platform uh to start, run and get and grow a business. Uh it is the leading global commerce company that provides essential internet infrastructure for commerce uh as well as uh trusted tools to start, scale uh and run a retail business of any size. Currently we have over uh 3 million businesses using our platform. Uh we have merchants like Gym Shark and Fashion Nova selling their products with us. Uh we represent over 175 countries and have about 10% of the total US commerce. Um in the summer of 2024, we reached a trill uh trillion dollars in gross merchandise volume. One of the largest events in commerce is the Black Friday Cyber Monday week uh which we call it BFCM. uh to share more stats about the scale of Shopify. Uh during the BFCM of 2024, Shopify processed around 58 pabytes of data, served more than a trillion edge requests as well as more than 10 trillion database queries uh which led to around 12 billion dollars of global sales. Search is a fundamental part of any commerce platform that allows buyers to search and filter for products or for merchants to fulfill their orders, manage their customers and inventory.

And when you go to any online store and search for a product, your request goes to a search engine that is backed by a secondary data store, which is different from traditional databases. Uh and the search engine that we use at Shopify is Elastic Search. A quick refresher on Ela
