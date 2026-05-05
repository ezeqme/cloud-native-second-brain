---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "SDLC"
themes: ["SDLC"]
speakers: ["Pete Hodgson", "PartnerSlate"]
sched_url: https://kccncna2024.sched.com/event/1i7rl/migratory-patterns-making-architectural-transitions-with-confidence-and-grace-pete-hodgson-partnerslate
youtube_search_url: https://www.youtube.com/results?search_query=Migratory+Patterns%3A+Making+Architectural+Transitions+with+Confidence+and+Grace+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Migratory Patterns: Making Architectural Transitions with Confidence and Grace - Pete Hodgson, PartnerSlate

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[SDLC]]
- Temas: [[SDLC]]
- País/cidade: United States / Salt Lake City
- Speakers: Pete Hodgson, PartnerSlate
- Schedule: https://kccncna2024.sched.com/event/1i7rl/migratory-patterns-making-architectural-transitions-with-confidence-and-grace-pete-hodgson-partnerslate
- Busca YouTube: https://www.youtube.com/results?search_query=Migratory+Patterns%3A+Making+Architectural+Transitions+with+Confidence+and+Grace+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Migratory Patterns: Making Architectural Transitions with Confidence and Grace.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7rl/migratory-patterns-making-architectural-transitions-with-confidence-and-grace-pete-hodgson-partnerslate
- YouTube search: https://www.youtube.com/results?search_query=Migratory+Patterns%3A+Making+Architectural+Transitions+with+Confidence+and+Grace+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oOHnDhPH3YQ
- YouTube title: Migratory Patterns: Making Architectural Transitions with Confidence and Grace - Pete Hodgson
- Match score: 1.002
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/migratory-patterns-making-architectural-transitions-with-confidence-an/oOHnDhPH3YQ.txt
- Transcript chars: 36859
- Keywords: feature, systems, writing, production, actually, migrations, postgress, change, expand, traffic, contract, parallel, confidence, vector, experience, database, write, called

### Resumo baseado na transcript

a long time ago I worked at a big US Bank and back then we deployed to production every quarter so every three months we would deploy our code to production we being the bank uh so that would mean every three months we'd deploy the mobile API for the mobile app I was working on and also all of the website changes for the last three months and also all of the software updates for all of the ATMs in the ATM Network and also the cobal code and

### Excerpt da transcript

a long time ago I worked at a big US Bank and back then we deployed to production every quarter so every three months we would deploy our code to production we being the bank uh so that would mean every three months we'd deploy the mobile API for the mobile app I was working on and also all of the website changes for the last three months and also all of the software updates for all of the ATMs in the ATM Network and also the cobal code and the Fortran code and the vax assembly and the main frames that was all done on one long weekend they turned off everything and had a lot of stressful uh conversations and tapping on keyboards and then hopefully turned it back on before Monday morning uh or maybe Tuesday Morning uh so this talk is about avoiding that experience anyone who's been through those kind of like big bang migrations where you take a lot of outage will know that it is not fun um if you haven't congratulations uh so I want to talk about why those kind of big bang migrations are so painful uh I'm going to talk about some patterns that you can use instead of doing these big bang migrations and we going do that using um a real world example or a few real world examples um so I am the CTO at a startup this startup exists in the year 2024 uh therefore we're doing things with AI I'm not going to talk to you about AI don't worry there's been a lot of conversations about AI uh but we we we're doing something with AI so we had this generative AI service and uh this was using a technique called rag you don't need to know what that means but it essentially means we were we were talking to a we needed us like this specialized database this thing called a vector store uh that we could ask questions and then do our AI magic with the results from this from this Vector store and we needed to load information into that vector store uh using this separate service or separate system that was kind of ingesting data in this pipeline so we had a thing that was reading from the vector store and thing it was loading data into the vector store and for the proof of Concepts that we initially built we used a technology called pine cone for that database um and over time we decided for various reasons that I'm not going to talk about uh that we wanted to shift from Pine Cone to postgress which is uh the database that we use for like everything else at our organization so I'm going to talk a little bit about how we did that um and you know to summarize what we were doing is w
