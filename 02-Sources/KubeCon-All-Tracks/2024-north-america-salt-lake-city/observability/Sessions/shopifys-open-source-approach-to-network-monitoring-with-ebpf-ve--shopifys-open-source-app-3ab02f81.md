---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Observability"
themes: ["Observability", "Networking", "Community Governance"]
speakers: ["Sebastian Rabenhorst", "Matt Franklin", "Shopify"]
sched_url: https://kccncna2024.sched.com/event/1i7pj/shopifys-open-source-approach-to-network-monitoring-with-ebpf-vector-and-clickhouse-sebastian-rabenhorst-matt-franklin-shopify
youtube_search_url: https://www.youtube.com/results?search_query=Shopify%E2%80%99s+Open+Source+Approach+to+Network+Monitoring+with+eBPF%2C+Vector+and+ClickHouse+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Shopify’s Open Source Approach to Network Monitoring with eBPF, Vector and ClickHouse - Sebastian Rabenhorst & Matt Franklin, Shopify

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Networking]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Sebastian Rabenhorst, Matt Franklin, Shopify
- Schedule: https://kccncna2024.sched.com/event/1i7pj/shopifys-open-source-approach-to-network-monitoring-with-ebpf-vector-and-clickhouse-sebastian-rabenhorst-matt-franklin-shopify
- Busca YouTube: https://www.youtube.com/results?search_query=Shopify%E2%80%99s+Open+Source+Approach+to+Network+Monitoring+with+eBPF%2C+Vector+and+ClickHouse+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Shopify’s Open Source Approach to Network Monitoring with eBPF, Vector and ClickHouse.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7pj/shopifys-open-source-approach-to-network-monitoring-with-ebpf-vector-and-clickhouse-sebastian-rabenhorst-matt-franklin-shopify
- YouTube search: https://www.youtube.com/results?search_query=Shopify%E2%80%99s+Open+Source+Approach+to+Network+Monitoring+with+eBPF%2C+Vector+and+ClickHouse+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FpVjdaRVmA4
- YouTube title: Shopify’s Open Source Approach to Network Monitoring with eBPF, Vector... S. Rabenhorst, M. Franklin
- Match score: 0.914
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/shopifys-open-source-approach-to-network-monitoring-with-ebpf-vector-a/FpVjdaRVmA4.txt
- Transcript chars: 30872
- Keywords: network, metadata, shopify, cluster, actually, clusters, connections, container, custom, question, traffic, connection, within, vector, process, metrics, ebpf, observability

### Resumo baseado na transcript

right let's go ahead and get started thank you all for coming to hear us uh blather on about Network performance monitoring uh we hope to find that you'll find it an interesting topic I hope you had a great C who are we so my name is Matt Franklin I'm a senior production engineering manager at Shopify um I joined Shopify about two years ago joined the observability team and have since then gone through quite a process of moving off of a a metrics vendor to an in-house

### Excerpt da transcript

right let's go ahead and get started thank you all for coming to hear us uh blather on about Network performance monitoring uh we hope to find that you'll find it an interesting topic I hope you had a great C who are we so my name is Matt Franklin I'm a senior production engineering manager at Shopify um I joined Shopify about two years ago joined the observability team and have since then gone through quite a process of moving off of a a metrics vendor to an in-house back and seeing this process of of building new observability systems uh come to life I am Sebastian Ros I'm a senior production engineer at mat's team and I'm probably nearly five years now yeah and I have previously worked on metrics at Shopify now I work on logs and that's uh also a project um I worked on recently a little bit of context uh so at Shopify we used to have a bunch of different signals that we had different vendors for and the observability team was responsible for kind of just maintaining those those vendors um a coup few years ago the executive team pushed us to to figure out how we could build a more unified observability platform for Shopify that meets our use cases um so we inh housed our metric system we started with a migration there and then moved on to uh logs traces tracing was actually first but as part of that we found that we needed the the ability to kind of look into our event stores so traces logs and analyze those in New in different ways right so we built a tool called investigate so as Sebastian and I were looking at this process of hey we need to build a a network Performance Management tool we started to leverage that that capability um to give you some context at Shopify you know like I said we had a prior vendor that vendor had a network Performance Management tool that tool was very useful uh as many of you who are in infrastructure ructure or are responsible for production systems will know the first question that everybody asks during an incident is is it the Network's fault fair question we had some ways to answer that after migrating away from our vendor but we didn't have a really good way to to get quick answers to those questions for additional context uh Shopify we run hundreds of of kubernetes clusters those clusters run millions of containers those millions of containers make millions of DNS queries per second and tens of millions of connections per second so this all left us with okay this Mission we have a little bit of time on our hands aft
