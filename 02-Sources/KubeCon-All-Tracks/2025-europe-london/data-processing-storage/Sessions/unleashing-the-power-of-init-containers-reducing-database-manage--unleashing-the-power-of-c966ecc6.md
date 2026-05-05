---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Data Processing + Storage"
themes: ["AI ML", "Storage Data", "Runtime Containers"]
speakers: ["Muhammad Junaid Muzammil", "Yelp"]
sched_url: https://kccnceu2025.sched.com/event/1txF4/unleashing-the-power-of-init-containers-reducing-database-management-toil-at-yelp-muhammad-junaid-muzammil-yelp
youtube_search_url: https://www.youtube.com/results?search_query=Unleashing+the+Power+of+Init+Containers%3A+Reducing+Database+Management+Toil+at+Yelp+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Unleashing the Power of Init Containers: Reducing Database Management Toil at Yelp - Muhammad Junaid Muzammil, Yelp

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[AI ML]], [[Storage Data]], [[Runtime Containers]]
- País/cidade: United Kingdom / London
- Speakers: Muhammad Junaid Muzammil, Yelp
- Schedule: https://kccnceu2025.sched.com/event/1txF4/unleashing-the-power-of-init-containers-reducing-database-management-toil-at-yelp-muhammad-junaid-muzammil-yelp
- Busca YouTube: https://www.youtube.com/results?search_query=Unleashing+the+Power+of+Init+Containers%3A+Reducing+Database+Management+Toil+at+Yelp+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Unleashing the Power of Init Containers: Reducing Database Management Toil at Yelp.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txF4/unleashing-the-power-of-init-containers-reducing-database-management-toil-at-yelp-muhammad-junaid-muzammil-yelp
- YouTube search: https://www.youtube.com/results?search_query=Unleashing+the+Power+of+Init+Containers%3A+Reducing+Database+Management+Toil+at+Yelp+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nTmwmd4fcGI
- YouTube title: Unleashing the Power of Init Containers: Reducing Database Management To... Muhammad Junaid Muzammil
- Match score: 0.905
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/unleashing-the-power-of-init-containers-reducing-database-management-t/nTmwmd4fcGI.txt
- Transcript chars: 20375
- Keywords: container, cassendra, containers, cluster, upgrade, process, clusters, cassandra, change, running, disruptions, version, versions, enabled, another, stateful, streaming, whether

### Resumo baseado na transcript

Many times we see bigger impacts or greater results achieved from small wellexecuted things that are put creatively together. And today I want to highlight one such small less appreciated and talked about but extremely powerful Kubernetes feature that is the init container. From operational perspective, all of our Cassendra clusters run on Kubernetes. Uh at Yelp, we use an in-house platform as a service called Bastard that provides the necessary abstraction on top of Kubernetes uh for managing different services. We run our own custom Cassendra operator that handles all the Kubernetes interaction uh for the Cassendra clusters. Any updates to these configurations are then converted into a Kubernetes custom resource.

### Excerpt da transcript

Hello everyone and welcome to a sunny CubeCon 2025 in London. I hope you are having an amazing day of learning today. Many times we see bigger impacts or greater results achieved from small wellexecuted things that are put creatively together. And today I want to highlight one such small less appreciated and talked about but extremely powerful Kubernetes feature that is the init container. and share how we at Yelp leverage inate containers to reduce the operational overhead of our Cassendra clusters and enhance the engineering efficiency. So introducing myself first I am Muhammad a tech lead in the database reliability engineering group at Yelp where I primarily look around the NoSQL databases uh and in particular Cassandra Here is what we will try to cover today. Uh I will try setting up the stage by sharing some information about the background in which we operate and give you a bird eyee view of how we use Cassandra at Yelp. Then we'll dive into three different uh problems that were solved by inate containers.

The first was about cluster scaling and here we will specifically be looking at the horizontal cluster scaling aspects. Secondly, I will talk about the Cassendra cluster upgrades and the impact init containers had in making the overall upgrade process easier and smoother. And thirdly, I will touch on the cluster recovery aspects from backups. uh in the end I will try wrapping up some key takeaways for you so that init containers is easier for you for your use cases. So starting off with the context how many of you have heard about Yelp? Can you raise your hand? Yeah, that's quite interesting. Uh those who don't know, Yelp is a community-driven platform that connects people with great local businesses. And millions of people rely on Yelp for the useful and trusted content about the business informations, reviews, and photos to inform their spending decisions. As of December 2024, there have been 308 million cumulative reviews with 29 million average monthly unique users in 2024. So here is another question.

How many of you have worked with Cassendra or have heard about Cassendra database? Okay. So again those not familiar Apache Cassandra is a white column distributed non- relational database and how we use it how we use it at Yelp. So if you visit any Yelp page there will be some portion of data that is served by Cassendra. So you can imagine how extensively Cassendra is used at Yelp. So we manage over 70 clusters in uh production environments f
