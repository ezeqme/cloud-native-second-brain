---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Serverless"
themes: ["Serverless"]
speakers: ["Janani Pathangi", "Murugappan Chetty", "Optum"]
sched_url: https://kccnceu2021.sched.com/event/iE2r/event-processing-at-optum-the-cloud-events-way-janani-pathangi-murugappan-chetty-optum
youtube_search_url: https://www.youtube.com/results?search_query=Event+Processing+at+Optum%2C+the+Cloud+Events+Way+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Event Processing at Optum, the Cloud Events Way - Janani Pathangi & Murugappan Chetty, Optum

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Serverless]]
- Temas: [[Serverless]]
- País/cidade: Virtual / Virtual
- Speakers: Janani Pathangi, Murugappan Chetty, Optum
- Schedule: https://kccnceu2021.sched.com/event/iE2r/event-processing-at-optum-the-cloud-events-way-janani-pathangi-murugappan-chetty-optum
- Busca YouTube: https://www.youtube.com/results?search_query=Event+Processing+at+Optum%2C+the+Cloud+Events+Way+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Event Processing at Optum, the Cloud Events Way.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE2r/event-processing-at-optum-the-cloud-events-way-janani-pathangi-murugappan-chetty-optum
- YouTube search: https://www.youtube.com/results?search_query=Event+Processing+at+Optum%2C+the+Cloud+Events+Way+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gXuW9mvj6xM
- YouTube title: Event Processing at Optum, the Cloud Events Way - Janani Pathangi & Murugappan Chetty, Optum
- Match score: 0.777
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/event-processing-at-optum-the-cloud-events-way/gXuW9mvj6xM.txt
- Transcript chars: 22623
- Keywords: events, source, native, broker, functions, sources, application, function, processing, platform, various, health, fitbit, infrastructure, formats, process, format, organization

### Resumo baseado na transcript

hi welcome all today we would like to share even processing at optum the cloud events way i'm janani pathangi distinguished engineer 20 years in usa and currently i lead the optum functions platform and i also have murugapan sevakan shetty here with me he is a principal engineer and tech lead and a k native open source contributor we would like to have a quick introduction about our organization united health group united health group is a highly diversified health and well-being company it's headquartered in the united states a database host container namespaces storage chargeback etc we ran into some of the challenges with the growing even sources with more than sources that we ingest today and we also have to support multiple data formats and sometimes some of the overlooked overlapping formats and there is no control over the source so these are some of the challenges and let's see how we re-architected that with cloud events now the first thing that we did was to identify the different formats and for each format we defined the cloud event type and the build parser and processor functions for it and the second thing was to build the k native event source to ingest the data into the broker now with this re-architecture the entire process is resilient to any upstream or downstream

### Excerpt da transcript

hi welcome all today we would like to share even processing at optum the cloud events way i'm janani pathangi distinguished engineer 20 years in usa and currently i lead the optum functions platform and i also have murugapan sevakan shetty here with me he is a principal engineer and tech lead and a k native open source contributor we would like to have a quick introduction about our organization united health group united health group is a highly diversified health and well-being company it's headquartered in the united states and ranked seventh of the fortune 500. we have two business platform united healthcare which will focus on health benefits and optum is a health services innovation company across optum we are able to serve many constituents of health system and we are grateful to serve and partner with 9 out of the 10 1400 companies 9 out of the 10 u.s hospital and serve 125 million consumers from infrastructure and technology perspective we have an annual spend of about 3.5 billion dollars on technology and innovation 99 percentage of our workloads run in our own data center with over 1 trillion transactions annually and these workloads will vary all the way from mainframe big data accelerators distributed sql containers and now with serverless ecosystem this is the agenda we plan to cover today we want to give a quick introduction about serverless at optum challenges with even processing why we started to explore cloud events and some of the autumn use cases with cloud events supplemented with demo and we would like to conclude with summary so now let's look into the optum functions it's an on-prem fully managed multi-tenant serverless platform which supports stateless event driven request based compute workloads currently it's offered cross dc active active without a ha capability from adoption standpoint we are increasing and thousand more than thousand functions deployed today with more than 500 developers using this across the organization to solve some of our enterprise use cases for example edl jobs today run as functions we are able to serve mission loading machine learning models and also have some of our infrastructure housekeeping jobs running on this platform so how do we make the open source stack to an enterprise service we started with the open source stack here kubernetes istio k native and we added more enterprise capability on top of them and as you can see here to the left hand side we started with enterprise integration with vau
