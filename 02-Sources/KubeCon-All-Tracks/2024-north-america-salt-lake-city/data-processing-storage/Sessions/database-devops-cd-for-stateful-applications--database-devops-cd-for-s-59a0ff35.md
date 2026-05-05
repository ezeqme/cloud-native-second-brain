---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Data Processing + Storage"
themes: ["Storage Data"]
speakers: ["Stephen Atwell", "Harness.io", "Christopher Crow", "Pure Storage"]
sched_url: https://kccncna2024.sched.com/event/1i7na/database-devops-cd-for-stateful-applications-stephen-atwell-harnessio-christopher-crow-pure-storage
youtube_search_url: https://www.youtube.com/results?search_query=Database+DevOps%3A+CD+for+Stateful+Applications+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Database DevOps: CD for Stateful Applications - Stephen Atwell, Harness.io & Christopher Crow, Pure Storage

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]]
- País/cidade: United States / Salt Lake City
- Speakers: Stephen Atwell, Harness.io, Christopher Crow, Pure Storage
- Schedule: https://kccncna2024.sched.com/event/1i7na/database-devops-cd-for-stateful-applications-stephen-atwell-harnessio-christopher-crow-pure-storage
- Busca YouTube: https://www.youtube.com/results?search_query=Database+DevOps%3A+CD+for+Stateful+Applications+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Database DevOps: CD for Stateful Applications.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7na/database-devops-cd-for-stateful-applications-stephen-atwell-harnessio-christopher-crow-pure-storage
- YouTube search: https://www.youtube.com/results?search_query=Database+DevOps%3A+CD+for+Stateful+Applications+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oXrHyOrUwB8
- YouTube title: Database DevOps: CD for Stateful Applications - Stephen Atwell & Christopher Crow
- Match score: 0.813
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/database-devops-cd-for-stateful-applications/oXrHyOrUwB8.txt
- Transcript chars: 34424
- Keywords: database, change, application, version, changes, staging, production, actually, schema, running, environment, pipeline, around, barbecue, everything, columns, column, little

### Resumo baseado na transcript

hi everyone uh he's Chris Crow I'm stepen Atwell we're here to talk about uh database devops and the benefits of leveraging uh continuous delivery for stateful applications yeah and I'm uh Chris Crow with uh with portworks and Stephen and I have been working on a few different different talks just about integrating various data tests inside of delivery pipelines uh using various tools and and all sorts of things it's kind of been a fun talk we uh gosh started this a couple of years ago we were

### Excerpt da transcript

hi everyone uh he's Chris Crow I'm stepen Atwell we're here to talk about uh database devops and the benefits of leveraging uh continuous delivery for stateful applications yeah and I'm uh Chris Crow with uh with portworks and Stephen and I have been working on a few different different talks just about integrating various data tests inside of delivery pipelines uh using various tools and and all sorts of things it's kind of been a fun talk we uh gosh started this a couple of years ago we were at on kubernetes Day last year but this um I guess project started a little a little before that based on uh one of your previous employers and a particular problem that they had that I never quite explained right for however many times we've done this yeah so at a past employer of mine um we were building a a bi solution with a custom reporting layer and a custom database and very very very configurable and the most important bugs in that product were also the hardest to find and the only reliable way we ever found to find them uh basically amounted to copying down every customer's configuration standing it up on the old version of the new version comparing the numbers and you know when I was there we we we spent several years at one point going and getting that all automated and when Chris and I started talking uh he he showed me how easy it is with kubernetes suddenly to go and automate the pieces of that that were the hardest um and right after I I told him the story like two days later we had a meeting and he showed up with a working version um and we've talking been talking about that and and variance of it ever since so I had more time on my hands back then now I have a nine-month old at home so that's a whole yeah different different level of um yeah time to be able to play with technology hence why uh Steven is running the the laptop this particular particular time but yeah that's the thing I find the most interesting or one of the most fun things for me about kubernetes is being able to have my entire app packaged on there and have it be uh have a lot of tools to actually make that portable and it occurs to me if I'm going to look at any of the slides I have to look over your shoulder here CU this is going to get awkward so uh somebody dial 91 and then uh if I fall down dial one again yeah so Chris and I like interacting with the audience so let's do a quick poll who here likes barbecue put up your hand if you like barbecue okay we got we got a few cool so
