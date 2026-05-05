---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Community Governance"]
speakers: ["Michael Hoffmann", "Aiven GmbH", "Giedrius Statkevičius", "Vinted"]
sched_url: https://kccnceu2024.sched.com/event/1Yhii/from-ui-to-storage-unraveling-the-magic-of-thanos-query-processing-michael-hoffmann-aiven-gmbh-giedrius-statkevicius-vinted
youtube_search_url: https://www.youtube.com/results?search_query=From+UI+to+Storage%3A+Unraveling+the+Magic+of+Thanos+Query+Processing+CNCF+KubeCon+2024
slides: []
status: parsed
---

# From UI to Storage: Unraveling the Magic of Thanos Query Processing - Michael Hoffmann, Aiven GmbH & Giedrius Statkevičius, Vinted

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Michael Hoffmann, Aiven GmbH, Giedrius Statkevičius, Vinted
- Schedule: https://kccnceu2024.sched.com/event/1Yhii/from-ui-to-storage-unraveling-the-magic-of-thanos-query-processing-michael-hoffmann-aiven-gmbh-giedrius-statkevicius-vinted
- Busca YouTube: https://www.youtube.com/results?search_query=From+UI+to+Storage%3A+Unraveling+the+Magic+of+Thanos+Query+Processing+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre From UI to Storage: Unraveling the Magic of Thanos Query Processing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhii/from-ui-to-storage-unraveling-the-magic-of-thanos-query-processing-michael-hoffmann-aiven-gmbh-giedrius-statkevicius-vinted
- YouTube search: https://www.youtube.com/results?search_query=From+UI+to+Storage%3A+Unraveling+the+Magic+of+Thanos+Query+Processing+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ZGQIitaKoTM
- YouTube title: From UI to Storage: Unraveling the Magic of Thanos Query Processing
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/from-ui-to-storage-unraveling-the-magic-of-thanos-query-processing/ZGQIitaKoTM.txt
- Transcript chars: 24340
- Keywords: engine, actually, promus, component, promethus, storage, presentation, distributed, queries, querer, question, execution, implement, another, remote, select, thanos, results

### Resumo baseado na transcript

Welcome to our presentation thank you for coming um even though it's late uh during the day um we will be giving you a presentation called from UI to storage unraveling unraveling the magic of Fus query processing and we hope that it will be entertaining and useful for you and yeah isn't there a better way to start a presentation then by talking about ourselves first just to pick your interest uh I'm GIS I'm a cability engineer at Vinted Vinted is a mostly a secondhand fashion Marketplace uh tries to answer your queries yeah what even is a tanos um to put into one sentence it's a system of microservices designed to scale promus and you can deploy tanas besides your running promus to Archive data into object storage and Achieve very high

### Excerpt da transcript

Welcome to our presentation thank you for coming um even though it's late uh during the day um we will be giving you a presentation called from UI to storage unraveling unraveling the magic of Fus query processing and we hope that it will be entertaining and useful for you and yeah isn't there a better way to start a presentation then by talking about ourselves first just to pick your interest uh I'm GIS I'm a cability engineer at Vinted Vinted is a mostly a secondhand fashion Marketplace uh it's quite popular and especially in France and Paris so you you are probably familiar with it if you live here um so we run a huge Thanos teack invented for all of our monitoring needs I've been personally a fos maintainer for almost uh not almost but for five years and and and Counting so it's been a quite a long journey and I'm still enjoying it and I hope that I will keep enjoying it for the next five years and I also write a blog at gas. blog about infrastructure monitoring related topics programming go um so if that's interest you please feel free to jump on it and with me I have Michael who will now talk about himself a little bit and do the rest of presentation hi I'm Michael uh an SRE at Ivan The Trusted open source data platform for everyone uh we have a booth go check it out uh though only for two more weeks I decided to start a new Journey at Cloud flare which is pretty cool uh I've been a tanos maintainer for like 6 months or something mostly fixing the oddb here and there and playing with the query engine which is a fairly captivating project but uh enough about us so why did we decide to give this talk want to introduce you to tanos of course and we figured it might be a nice angle to approach this from the point of view of a query execution and um we hope to give you a birs iie about how data flows to tanos while it tries to answer your queries yeah what even is a tanos um to put into one sentence it's a system of microservices designed to scale promus and you can deploy tanas besides your running promus to Archive data into object storage and Achieve very high retention rates uh typical months to years instead of days in fact um yesterday I learned that the original working title for the project was PR LTS which tells you everything and it also allows you to Cluster up your prous deployments horizontally and still keep a single pane of Glass by proxying queries and merging results tanos is the incubating cncf project which is the reason we allowed to s
