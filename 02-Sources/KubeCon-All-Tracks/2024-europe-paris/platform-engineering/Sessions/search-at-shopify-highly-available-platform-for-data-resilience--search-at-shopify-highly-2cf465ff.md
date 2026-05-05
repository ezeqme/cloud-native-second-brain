---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering", "Storage Data", "SRE Reliability"]
speakers: ["Leila Vayghan", "Shopify"]
sched_url: https://kccnceu2024.sched.com/event/1YeSk/search-at-shopify-highly-available-platform-for-data-resilience-and-compliance-leila-vayghan-shopify
youtube_search_url: https://www.youtube.com/results?search_query=Search+at+Shopify%3A+Highly+Available+Platform+for+Data+Resilience+and+Compliance+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Search at Shopify: Highly Available Platform for Data Resilience and Compliance - Leila Vayghan, Shopify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Leila Vayghan, Shopify
- Schedule: https://kccnceu2024.sched.com/event/1YeSk/search-at-shopify-highly-available-platform-for-data-resilience-and-compliance-leila-vayghan-shopify
- Busca YouTube: https://www.youtube.com/results?search_query=Search+at+Shopify%3A+Highly+Available+Platform+for+Data+Resilience+and+Compliance+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Search at Shopify: Highly Available Platform for Data Resilience and Compliance.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSk/search-at-shopify-highly-available-platform-for-data-resilience-and-compliance-leila-vayghan-shopify
- YouTube search: https://www.youtube.com/results?search_query=Search+at+Shopify%3A+Highly+Available+Platform+for+Data+Resilience+and+Compliance+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=H0Cdf--4uq8
- YouTube title: Search at Shopify: Highly Available Platform for Data Resilience and Compliance - Leila Vayghan
- Match score: 0.998
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/search-at-shopify-highly-available-platform-for-data-resilience-and-co/H0Cdf--4uq8.txt
- Transcript chars: 22466
- Keywords: search, elastic, shopify, custom, controller, stateful, cluster, provide, platform, merchants, region, clusters, storage, infrastructure, pipeline, availability, documents, redundancy

### Resumo baseado na transcript

hello uh thank you for coming seems like I'm closing cucon last session of the last day uh my name is Leila I work at Shopify as an infrastructure engineer I'm on a team of eight Engineers called the search platform who develop and maintain the infrastructure that power search at Shopify today I'll be talking about search uh Shopify which is a highly available platform for data resilience and compliance in the next 20 minutes or so we will learn how the search platform team at Shopify hosts the

### Excerpt da transcript

hello uh thank you for coming seems like I'm closing cucon last session of the last day uh my name is Leila I work at Shopify as an infrastructure engineer I'm on a team of eight Engineers called the search platform who develop and maintain the infrastructure that power search at Shopify today I'll be talking about search uh Shopify which is a highly available platform for data resilience and compliance in the next 20 minutes or so we will learn how the search platform team at Shopify hosts the search infrastructure on top of kubernetes uh we will talk about the entire data pipeline that writes data from SQL to elastic search through CFA and I will talk about the system requirements for search such as high availability scalability and globalization and how we designed and implemented a platform to achieve them and I will conclude my talk with a Q&A introducing Shopify for those who don't know about us Shopify is a cloud-based Commerce platform that lets you start and manage a business by allowing you to create and customize an online store and manage inventory payments customers and Etc currently we have over 3 million businesses using our platform we have have Merchants like gym shark fashion Nova selling their products with us uh we represent over uh 170 countries around the world and have about 10% of the total us Commerce and I've had above $400 billion in global Commerce Activity one of the largest events in Commerce especially in North America is Black Friday Cyber Monday week we call it BFC M to share more stats about the scale of Shopify during the bfcm of 2023 which was a few months ago Shopify processed A45 billion requests in a day peing around 60 million requests per minute um which led to a total of $4 billion in gmv search is a fundamental part of any Commerce platform uh allowing buyers to search and filter products and also Merchants to fulfill uh orders and manage their customers uh when you go to any online store and for example search for a product your request goes to a search engine uh that's backed by a secondary data store which is different from traditional databases uh we call this secondary data store the search infrastructure the next couple of slides uh is going to be a quick refresher on the two key technology will be talking about throughout this talk the first one is elastic search it is a distributed Tech search and analytics engine built on top of Lucine that has full TX s capabilities that are well suited to the e-commerce
