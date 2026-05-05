---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Observability"
themes: ["AI ML", "Observability", "Storage Data"]
speakers: ["Zain Asgar", "Natalie Serrino", "New Relic"]
sched_url: https://kccncna2021.sched.com/event/lV4c/data-science-for-infrastructure-observe-understand-automate-zain-asgar-natalie-serrino-new-relic
youtube_search_url: https://www.youtube.com/results?search_query=Data+Science+for+Infrastructure%3A+Observe%2C+Understand%2C+Automate+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Data Science for Infrastructure: Observe, Understand, Automate - Zain Asgar & Natalie Serrino, New Relic

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]], [[Storage Data]]
- País/cidade: United States / Los Angeles
- Speakers: Zain Asgar, Natalie Serrino, New Relic
- Schedule: https://kccncna2021.sched.com/event/lV4c/data-science-for-infrastructure-observe-understand-automate-zain-asgar-natalie-serrino-new-relic
- Busca YouTube: https://www.youtube.com/results?search_query=Data+Science+for+Infrastructure%3A+Observe%2C+Understand%2C+Automate+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Data Science for Infrastructure: Observe, Understand, Automate.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV4c/data-science-for-infrastructure-observe-understand-automate-zain-asgar-natalie-serrino-new-relic
- YouTube search: https://www.youtube.com/results?search_query=Data+Science+for+Infrastructure%3A+Observe%2C+Understand%2C+Automate+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EG4isSqD3IE
- YouTube title: Data Science for Infrastructure: Observe, Understand, Automate - Zain Asgar & Natalie Serrino
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/data-science-for-infrastructure-observe-understand-automate/EG4isSqD3IE.txt
- Transcript chars: 26873
- Keywords: actually, basically, injection, application, running, script, automate, simple, request, pretty, metrics, requests, understand, machine, learning, natalie, information, attacks

### Resumo baseado na transcript

hey everyone we're going to talk about data science for infrastructure um so three steps we think are the three steps observe understand and automate um before we get started uh just a really quick overview uh i'm zane and this is natalie i'm a gm at new relic and formerly the co-founder and ceo of pixie labs we got acquired by new relic and both of us are working on the pixie project now and natalie is a prince engineer on our team so we're both machine learning people

### Excerpt da transcript

hey everyone we're going to talk about data science for infrastructure um so three steps we think are the three steps observe understand and automate um before we get started uh just a really quick overview uh i'm zane and this is natalie i'm a gm at new relic and formerly the co-founder and ceo of pixie labs we got acquired by new relic and both of us are working on the pixie project now and natalie is a prince engineer on our team so we're both machine learning people by my background and have basically spent the last decade building scalable data and machine learning systems and we really wanted to try to understand how to apply our our knowledge from that space into observability and infrastructure so when we started um you know in the space we started to think that this is just another data problem it's easy for machines to really you know very quickly generate gigabytes of data but it's really hard for us to actually get complete coverage especially in distributed environments where it's hard to instrument all your applications it's also hard to make sure that all the data you collect is relevant and it is difficult to then distill this information into something that's usable to automate workflows so we wanted to take what we learned from the data space and um apply it to the infrastructure and we kind of realized that there's a few different problems that need to get solved so one of them you know i think you've probably heard about this from everybody is collecting the right data is is very difficult and you know we say it's half the battle here but in reality it could be way more than half the battle um and one of the other takeaways from you know our data and machine learning days as that simple models on good data or relevant data usually outperform very complex models that are built on like skewed or inaccurate and accurate data the other thing we really learned is that it's really important to be able to audit and understand what's happening in your data pipelines and that you don't just have like ad hoc systems uh running your infrastructure so for this we kind of think about how to break down the steps into three different three different stages the first step is to unders observe your data the next step is to understand it and the third steps to automate and we'll kind of walk through each of the steps and see what that means so for data-driven automation the first step is that you gather the raw data so this might be something like gettin
